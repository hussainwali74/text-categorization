from multiprocessing import Pool
import pandas as pd
from fuzzywuzzy import fuzz
import json

# Read category_dict from JSON
with open('categories_dict.json') as f:
    category_dict = json.load(f)
  
df = pd.read_csv('source.csv', low_memory=False)

df_missing = df[df['Sub_Category'].isna()]  
df_filled = df[~df['Sub_Category'].isna()]


def process_chunk(df):  
   
    for category, variations in category_dict.items():
        category = str(category).lower()
        new_variations = list(set([category,*variations]))

        masks = []
        lower_name = df['Name'].str.lower()
        for variation in new_variations:
            variation = str(variation).lower()
            masks.append(lower_name.str.contains(variation, case=False, regex=False))

        # Combine the masks using the logical OR operator
        combined_mask = pd.concat(masks, axis=1).any(axis=1)

        # Apply the combined mask to the DataFrame
    df.loc[combined_mask, 'Sub_Category'] = category.capitalize()
    
    df_rem = df[df['Sub_Category'].isna()]
    df_done = df[~df['Sub_Category'].isna()]
    
    # -----------------------------------------------------------------
    #               FUZZY
    # -----------------------------------------------------------------
    for index, row in df_rem.iterrows():   
        name = row['Name']
           
        if pd.api.types.is_string_dtype(name):
            name = name.str.lower()
        else: 
            name = str(name).lower() 

        highest_score = 0
        highest_category = None

        for category, variations in category_dict.items():
            category = str(category).lower()
            new_variations = list(set([category,*variations]))
            
            for variation in new_variations:
                variation = str(variation).lower()
                
                score = fuzz.token_set_ratio(name, variation.lower())
                if score > highest_score:
                    highest_score = score
                    highest_category = category
                    
        if highest_score > 70:  
            df_rem.loc[index, 'Sub_Category'] = highest_category.capitalize()  
        df = pd.concat([df_rem,df_done])
    return df

if __name__ == '__main__':
    with Pool(5) as p:  # Use 5 processes
        df_processed = p.map(process_chunk, [df_missing[i:i+10000] for i in range(0, df_missing.shape[0], len(df_missing))])[0] 
    # Concatenate the processed DataFrame with df_filled
    df = pd.concat([df_processed, df_filled])  
df.to_csv('data_output.csv', index=False)
        
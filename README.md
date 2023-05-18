# Category Classification
This script reads in a CSV file called source.csv, classifies rows into categories based on a categories dictionary, and outputs the classified CSV to data_output.csv.
## Instructions
1. Make sure you have the required libraries installed:
`pip install pandas fuzzywuzzy multiprocessing`
2. Place source.csv and categories_dict.json in the same directory as the script.
3. categories_dict.json should be a JSON dictionary mapping category names to lists of keywords, for example:
json
{
  "Fruits": ["apple", "banana", "orange"],
  "Vegetables": ["carrot", "broccoli", "spinach"] 
}
4. Run the script:
python category_classification.py
5. The output will be written to data_output.csv. It will contain the original CSV data with an added Sub_Category column containing the classified categories.
6. Adjust the fuzz.token_set_ratio() threshold as needed to control how strict or loose the fuzzy matching is. The default is 70.
7. The script utilizes multiprocessing to speed up the classification process. Adjust the number of processes initialized in the Pool() call as needed for your system. The default is 5 processes.
8. Let me know if you have any issues or questions! I'm happy to help explain or clarify any part of this README or the script.
## About the Script
This script reads the source CSV, splits it into rows missing a category and rows that already have a category. It then processes the missing rows in chunks using multiprocessing, classifying each row into a category based on:
1. Exact keyword/phrase matches from the categories dictionary
2. Fuzzy matching ratios calculated with fuzz.token_set_ratio()
The processed and original DataFrame chunks are then concatenated back together and exported, resulting in the full source CSV populated with categories.
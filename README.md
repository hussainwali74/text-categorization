![Category Classification](img.png)

# Category Classification

This is a script to categorize rows of a CSV file into custom categories using both exact and fuzzy matching. The classification is driven by a user-defined dictionary of categories and keywords and is designed for efficiency with multiprocessing.

## Features

- **Category classification**: Assign categories to rows in a CSV file based on keyword and fuzzy text matching.
- **Customizable dictionary**: Categories and keywords are defined in a `categories_dict.json` file.
- **Fuzzy matching**: Uses `fuzzywuzzy`’s token set ratio for flexible matching.
- **Multiprocessing**: Parallelizes the classification for large datasets.
- **Simple input/output**: Reads from `source.csv`, outputs to `data_output.csv`.
- **Easy configuration**: Adjustable fuzzy matching threshold and number of processes.

## Getting Started

### 1. Install Dependencies

Make sure you have the required Python libraries:

```bash
pip install pandas fuzzywuzzy multiprocessing
```

### 2. Prepare Data Files

- Place `source.csv` (the data to classify) and `categories_dict.json` (the category dictionary) in the same directory as the script.

Example `categories_dict.json`:

```json
{
  "Fruits": ["apple", "banana", "orange"],
  "Vegetables": ["carrot", "broccoli", "spinach"]
}
```

### 3. Run the Script

```bash
python category_classification.py
```

### 4. Output

- The script generates `data_output.csv` with an added `Sub_Category` column for classified categories.

## Configuration

- **Fuzzy Matching Threshold**: Adjust the threshold in the script to make matching stricter or looser (default: 70).
- **Multiprocessing**: Set the number of processes in the `Pool()` initialization (default: 5). Increase for larger datasets/systems with more cores.

## How it Works

1. The script reads `source.csv`.
2. It splits data into rows with and without existing categories.
3. Rows missing a category are classified using:
   - Exact keyword/phrase matches from `categories_dict.json`
   - Fuzzy matching via `fuzz.token_set_ratio()`
4. The results are merged and exported as `data_output.csv`.

## Troubleshooting

- Ensure `source.csv` and `categories_dict.json` are in the same directory as the script.
- Check that all required libraries are installed.
- Adjust the multiprocessing settings if you encounter performance issues.
- For any questions or issues, feel free to open an issue or contact the maintainer.

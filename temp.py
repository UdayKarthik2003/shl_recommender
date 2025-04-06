import pandas as pd

# Load the uploaded CSV using ISO-8859-1 which often works with Windows-encoded Excel files
file_path = "/mnt/data/assessments.csv"

# Try reading with ISO-8859-1 encoding
try:
    df = pd.read_csv(file_path, encoding="ISO-8859-1")
    df.columns = ['name', 'category', 'description'][:len(df.columns)]  # Rename columns if they exist
    cleaned_path = "/mnt/data/assessments_cleaned.csv"
    df.to_csv(cleaned_path, index=False, encoding="utf-8")
    cleaned_path
except Exception as e:
    str(e)

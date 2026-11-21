import pandas as pd

# Load the dataset
df = pd.read_csv("sales_data.csv")

print("===== DATASET OVERVIEW =====")

# Display first 5 rows
print("\n----- FIRST 5 RECORDS -----")
print(df.head())

# Dataset dimensions
print("\n----- DATASET SHAPE -----")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Column names
print("\n----- COLUMN NAMES -----")
print(df.columns.tolist())

# Data types
print("\n----- DATA TYPES -----")
print(df.dtypes)

# Missing values
print("\n----- MISSING VALUES -----")
print(df.isnull().sum())

# Duplicate records
print("\n----- DUPLICATE RECORDS -----")
print("Duplicates:", df.duplicated().sum())

# Statistical summary
print("\n----- STATISTICAL SUMMARY -----")
print(df.describe())

print("\nData inspection completed successfully!")
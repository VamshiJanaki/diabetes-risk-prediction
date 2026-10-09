import pandas as pd

# Load the dataset
df = pd.read_csv("diabetes.csv", header=None)

# Add column names
df.columns = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "DiabetesPedigreeFunction",
    "Age",
    "Outcome"
]

# Display the first 5 rows
print("First 5 rows:")
print(df.head())

# Display dataset information
print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nDataset information:")
df.info()

print("\nMissing values:")
print(df.isnull().sum())

print("\nOutcome counts:")
print(df["Outcome"].value_counts())

print("\nZero values in medical measurements:")

columns_to_check = [
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI"
]

for column in columns_to_check:
    zero_count = (df[column] == 0).sum()
    print(f"{column}: {zero_count}")
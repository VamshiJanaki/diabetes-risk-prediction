
import pandas as pd

# Load the original dataset
df = pd.read_csv("diabetes.csv", header=None)

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

# Replace zero values with missing values
columns_to_fix = [
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI"
]

for column in columns_to_fix:
    df[column] = df[column].replace(0, float("nan"))

# Fill missing measurements with their column medians
for column in columns_to_fix:
    df[column] = df[column].fillna(df[column].median())

print("Missing values after preprocessing:")
print(df.isnull().sum())

print("\nDataset shape after preprocessing:")
print(df.shape)

# Save the cleaned dataset
df.to_csv("diabetes_clean.csv", index=False)

print("\nCleaned dataset saved as diabetes_clean.csv")

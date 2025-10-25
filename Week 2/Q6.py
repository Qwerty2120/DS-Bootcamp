import pandas as pd

# Step 1: Load dataset
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

# Step 2: Check for missing values
print("Missing values before replacement:")
print(df[['Min.Price', 'Max.Price']].isna().sum())

# Step 3: Replace missing values with mean
df['Min.Price'].fillna(df['Min.Price'].mean(), inplace=True)
df['Max.Price'].fillna(df['Max.Price'].mean(), inplace=True)

# Step 4: Verify replacement
print("\nMissing values after replacement:")
print(df[['Min.Price', 'Max.Price']].isna().sum())



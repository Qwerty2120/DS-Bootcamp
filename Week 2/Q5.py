import pandas as pd

# Step 1: Read the dataset
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

# Step 2: Select every 20th row starting from row 0
every_20th_row = df.iloc[::20, :]   # slicing syntax: start:end:step

# Step 3: Filter required columns
filtered_df = every_20th_row[['Manufacturer', 'Model', 'Type']]

# Step 4: Display result
print(filtered_df)

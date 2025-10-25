import numpy as np

# Step 1: Load dataset (include all 5 columns)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
iris_2d = np.genfromtxt(url, delimiter=",", dtype=str)

# Step 2: Remove empty rows (UCI file has one blank line at the end)
iris_2d = iris_2d[iris_2d[:, 0] != '']

# Step 3: Apply filter
# Convert first 4 columns to float before comparison
mask = (iris_2d[:, 2].astype(float) > 1.5) & (iris_2d[:, 0].astype(float) < 5.0)
filtered_rows = iris_2d[mask]

# Step 4: Display result
print("Filtered rows (petal_length > 1.5 and sepal_length < 5.0):")
for row in filtered_rows:
    print(row)

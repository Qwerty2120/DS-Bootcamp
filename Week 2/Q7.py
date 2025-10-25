import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4),
                  columns=['A', 'B', 'C', 'D'])

print("Original DataFrame:")
print(df)

# Step 2: Filter rows where the row sum > 100
filtered_df = df[df.sum(axis=1) > 100]

print("\nRows where row sum > 100:")
print(filtered_df)


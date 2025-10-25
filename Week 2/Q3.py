import numpy as np

# Define array A
A = np.array([2, 5, 7, 10, 13, 8, 4])

# Define the range
lower_bound = 5
upper_bound = 10

# Apply boolean mask
filtered = A[(A >= lower_bound) & (A <= upper_bound)]

print("Array A:", A)
print(f"Numbers between {lower_bound} and {upper_bound}:", filtered)

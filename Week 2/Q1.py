import numpy as np

# Define two custom arrays
A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8, 9],
              [10, 11, 12]])

# Stack vertically (one on top of the other)
vertical_stack = np.vstack((A, B))

# Stack horizontally (side by side)
horizontal_stack = np.hstack((A, B))

print("Array A:")
print(A)
print("\nArray B:")
print(B)

print("\nVertically Stacked Array:")
print(vertical_stack)

print("\nHorizontally Stacked Array:")
print(horizontal_stack)









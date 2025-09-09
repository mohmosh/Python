import numPy as np

# Create an array with numbers from 10 to 50 (inclusive)
array = np.arange(10, 51)

# Find maximum and minimum values
max_value = np.max(array)
min_value = np.min(array)

# Multiply all elements by 3
multiplied_array = array * 3

print("Array:", array)
print("Maximum Value:", max_value)
print("Minimum Value:", min_value)
print("Array after multiplying by 3:", multiplied_array)
import pandas as pd
import numpy as np
import re

# Function to convert the string representation of tuples in the DataFrame cells into actual tuples
def to_tuple(s):
    # Using regular expressions to find numbers in the string, converting them to floats, and then to a tuple
    return tuple(map(float, re.findall(r"[\d\.\-]+", s)))

# Load the Excel file
excel_path = 'matrix/B2_matrix.xlsx'  # Update this path to your actual Excel file location
data = pd.read_excel(excel_path)

# Adjusting for the inclusion of the first row
rows, cols = data.shape
# We need to adjust the size of the matrices since we are including the header row as part of the data now
Ex = np.zeros((rows, cols-1))  # Initialize Ex matrix, considering the first row as data
En = np.zeros((rows, cols-1))  # Initialize En matrix
He = np.zeros((rows, cols-1))  # Initialize He matrix

# Iterate over the DataFrame including the first row this time
for i in range(rows):
    for j in range(1, cols):  # Still skip the first column since it's an index or header
        val_tuple = to_tuple(data.iloc[i, j])  # Convert the cell value to a tuple
        Ex[i, j-1], En[i, j-1], He[i, j-1] = val_tuple  # Assign values to the matrices

# The matrices are now filled with the Ex, En, and He values, including the first row
print("Ex Matrix:")
print(Ex)
print("\nEn Matrix:")
print(En)
print("\nHe Matrix:")
print(He)

from scipy.stats import norm
import numpy as np

# Define matrices Ex, En, He
Ex = np.array([
    [248, 282, 350, 418, 452],
    [26, 31.5, 42.5, 53.5, 59],
    [318, 352, 420, 488, 522]
])

En = np.array([
    [28.87, 28.87, 28.87, 28.87, 28.87],
    [4.671, 4.671, 4.671, 4.671, 4.671],
    [28.87, 28.87, 28.87, 28.87, 28.87]
])

He = np.array([
    [0.1, 0.1, 0.1, 0.1, 0.1],
    [0.2, 0.2, 0.2, 0.2, 0.2],
    [0.2, 0.2, 0.2, 0.2, 0.2]
])

# Group and parameter counts
m, n = Ex.shape  # This uses the numpy way to get the shape

# Initialize R matrix
R = np.zeros((m, n))

# Number of samples
M = 100

# Sample values
samples = np.array([0, 0, 0])

# Loop through each group and parameter
for a in range(m):
    for b in range(n):
        # Generate random samples
        X = norm.rvs(loc=En[a, b], scale=He[a, b], size=M)
        # Calculate Y values
        Y = np.exp(-((samples[a] - Ex[a, b]) ** 2) / (2 * X ** 2))
        # Calculate mean of Y
        R[a, b] = np.mean(Y)

np.set_printoptions(linewidth=np.inf)

# print(matrix)
# R contains the result
# print(m,n)
print(R)


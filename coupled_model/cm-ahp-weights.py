import numpy as np

def calculate_Ex0(Ex):
    m = Ex.shape[1]
    product_Ex = np.prod(Ex, axis=1) ** (1/m)
    Ex0 = product_Ex / np.sum(product_Ex)
    return Ex0

def calculate_En0(Ex, En):
    m = Ex.shape[1]
    product_Ex = np.prod(Ex, axis=1) ** (1/m)
    En0_numerator = product_Ex * (np.sum((En / Ex) ** 2, axis=1) ** (1/(2*m)))
    En0_denominator = np.sum(product_Ex * (np.sum((En / Ex) ** 2, axis=1) ** (1/(2*m))))
    En0 = En0_numerator / En0_denominator
    return En0

def calculate_He0(Ex, He):
    m = Ex.shape[1]
    product_Ex = np.prod(Ex, axis=1) ** (1/m)
    He0_numerator = product_Ex * (np.sum((He / Ex) ** 2, axis=1) ** (1/(2*m)))
    He0_denominator = np.sum(product_Ex * (np.sum((He / Ex) ** 2, axis=1) ** (1/(2*m))))
    He0 = He0_numerator / He0_denominator
    return He0

def weight_matrix(Ex, En, He):
    Ex0 = calculate_Ex0(Ex)
    En0 = calculate_En0(Ex, En)
    He0 = calculate_He0(Ex, He)
    return np.column_stack((Ex0, En0, He0))

def calculate_lambda_max(Ex, weights):
    m = Ex.shape[1]
    lambda_max_numerator = np.sum(np.sum(Ex * weights, axis=1) / weights, axis=0)
    lambda_max = (1/m) * lambda_max_numerator
    return lambda_max

# Calculate the Consistency Index (CI)
def calculate_CI(lambda_max, m):
    CI = (lambda_max - m) / (m - 1)
    return CI

def calculate_CR(CI, RI):
    if RI == 0:  # Avoid division by zero if RI is 0
        return 0
    CR = CI / RI
    return CR

RI_dict = {
    1: 0,
    2: 0,
    3: 0.52,
    4: 0.89,
    5: 1.12,
    6: 1.26,
    7: 1.36,
    8: 1.41,
    9: 1.46,
    10: 1.49,
    11: 1.52,
    12: 1.54,
    13: 1.56,
    14: 1.58,
    15: 1.59,
    16: 1.5943,
    17: 1.6064,
    18: 1.6133,
    19: 1.6207,
    20: 1.6292,
    21: 1.6385,
    22: 1.6403,
    23: 1.6462,
    24: 1.6497,
    25: 1.6556,
    26: 1.6587,
    27: 1.6631,
    28: 1.667,
    29: 1.6693,
    30: 1.6724,
}

if __name__ == '__main__':
    # Example matrices (actual data should replace these)
    Ex = np.array([
        [1.00, 2.33],
        [0.44, 1.00]
    ]) # Actual Ex_ij values

    En = np.array([
        [0.00, 0.33],
        [0.067, 0.00]
    ])  # Actual En_ij values

    He = np.array([
        [0.00, 0.087],
        [0.019, 0.00]
    ])
    # Actual He_ij values

    # Calculate Ex0, En0, and He0
    weights = weight_matrix(Ex, En, He)

    # Calculate lambda_max for Ex0, En0, and He0
    lambda_max_Ex = calculate_lambda_max(Ex, weights[:, 0])
    lambda_max_En = calculate_lambda_max(En, weights[:, 1])
    lambda_max_He = calculate_lambda_max(He, weights[:, 2])

    # Calculate CI for Ex0, En0, and He0
    CI_Ex = calculate_CI(lambda_max_Ex, m=Ex.shape[1])
    CI_En = calculate_CI(lambda_max_En, m=En.shape[1])
    CI_He = calculate_CI(lambda_max_He, m=He.shape[1])

    # Get RI for the given matrix size
    RI = RI_dict.get(Ex.shape[1], "Undefined")  # RI is undefined for sizes not in RI_dict

    # Calculate CR for Ex0, En0, and He0
    CR_Ex = calculate_CR(CI_Ex, RI)
    CR_En = calculate_CR(CI_En, RI)
    CR_He = calculate_CR(CI_He, RI)

    print(weights)
    print(f'Ex: lambda_max:{lambda_max_Ex}, CI:{CI_Ex}, RI:{RI}, CR:{CR_Ex}')
    print(f'En: lambda_max:{lambda_max_En}, CI:{CI_En}, RI:{RI}, CR:{CR_En}')
    print(f'He: lambda_max:{lambda_max_He}, CI:{CI_He}, RI:{RI}, CR:{CR_He}')

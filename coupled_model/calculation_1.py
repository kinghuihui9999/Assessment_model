import numpy as np

# 定义单个云模型的特征
# C = (0.918,0.384,0.501)
A = (0.303, 0.311, 0.318)

# 二维矩阵
B = np.array([[0.037, 0.037, 0.037]])

# 更新乘法计算函数以适应矩阵
def cloud_multiplication(C1, C2):
    Ex1, En1, He1 = C1
    Ex2, En2, He2 = C2
    Ex = Ex1 * Ex2
    En = np.abs(Ex) * np.sqrt((En1 / Ex1) ** 2 + (En2 / Ex2) ** 2)
    He = np.abs(Ex) * np.sqrt((He1 / Ex1) ** 2 + (He2 / Ex2) ** 2)
    return Ex, En, He


# 扩展加法、减法和除法函数以适应矩阵
def cloud_addition(C1, C2):
    Ex1, En1, He1 = C1
    Ex2, En2, He2 = C2
    Ex = Ex1 + Ex2
    En = np.sqrt(En1 ** 2 + En2 ** 2)
    He = np.sqrt(He1 ** 2 + He2 ** 2)
    return Ex, En, He


def cloud_subtraction(C1, C2):
    Ex1, En1, He1 = C1
    Ex2, En2, He2 = C2
    Ex = Ex1 - Ex2
    En = np.sqrt(En1 ** 2 + En2 ** 2)
    He = np.sqrt(He1 ** 2 + He2 ** 2)
    return Ex, En, He


def cloud_division(C1, C2):
    Ex1, En1, He1 = C1
    Ex2, En2, He2 = C2
    Ex = Ex1 / Ex2
    En = np.abs(Ex) * np.sqrt((En1 / Ex1) ** 2 + (En2 / Ex2) ** 2)
    He = np.abs(Ex) * np.sqrt((He1 / Ex1) ** 2 + (He2 / Ex2) ** 2)
    return Ex, En, He


# 计算矩阵C2中每一行的乘法结果
def cloud_operations_matrix(C1, C2, operation):
    results_matrix = np.empty_like(C2)

    # 选择运算类型
    operations = {
        'addition': cloud_addition,
        'subtraction': cloud_subtraction,
        'multiplication': cloud_multiplication,
        'division': cloud_division
    }
    operation_func = operations[operation]

    for i, C2 in enumerate(C2):
        results_matrix[i] = operation_func(C1, C2)

    return results_matrix


# 使用加法计算矩阵C2
mutiply_results = cloud_operations_matrix(A, B, 'multiplication')
# add_results= cloud_operations_matrix(A, B, 'addition')
# matrix = np.vstack((multiplication_results_1, multiplication_results_2))
print(mutiply_results)


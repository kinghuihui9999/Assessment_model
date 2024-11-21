import numpy as np
#        水深  流速  DEM  坡度  水距  不透率
# 水深    1    2    3    3    5    4
# 流速    1/2    1    3    3    5    4
# DEM     1/3  1/3  1    2    4    3
# 坡度    1/3  1/3  1/2  1    3    2
# 水距    1/5  1/5  1/4  1/3  1    1
# 不透率  1/4  1/4  1/3  1/2  1    1


# 定义自然因子的判断矩阵
A_nature = np.array([
    [1, 2, 3, 3, 5, 4],
    [1/2, 1, 3, 3, 5, 4],
    [1/3, 1/3, 1, 2, 4, 3],
    [1/3, 1/3, 1/2, 1, 3, 2],
    [1/5, 1/5, 1/4, 1/3, 1, 1],
    [1/4, 1/4, 1/3, 1/2, 1, 1]
])


def calculate_weights_and_consistency(A):
    """
    计算给定判断矩阵A的权重和一致性检验。

    参数:
    A : numpy.ndarray
        一个判断矩阵。

    返回:
    weights : numpy.ndarray
        判断矩阵的权重向量。
    CI : float
        一致性指数。
    CR : float
        一致性比率。
    """
    # 计算特征值和特征向量
    eigenvalues, eigenvectors = np.linalg.eig(A)

    # 最大特征值
    lambda_max = max(eigenvalues.real)

    # 判断矩阵的阶数
    n = A.shape[0]

    # 计算一致性指数CI
    CI = (lambda_max - n) / (n - 1)

    # 随机一致性指数RI，这里提供了一个简单的RI表格，适用于n=1到10
    RI_list = [0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49]
    RI = RI_list[n-1] if n <= 10 else 1.49  # 对于n大于10的情况，可以适当调整

    # 计算一致性比率CR
    CR = CI / RI if RI != 0 else 0

    # 提取与最大特征值对应的特征向量
    max_eigenvalue_index = np.argmax(eigenvalues)
    eigenvector = eigenvectors[:, max_eigenvalue_index]

    # 归一化特征向量以得到权重
    weights = eigenvector / np.sum(eigenvector)
    weights_real = np.real(weights) # 确保权重是实数

    return weights_real, CI, CR

# 重新计算自然因子的权重和一致性
if __name__ == '__main__':
    weights_nature, CI_nature, CR_nature = calculate_weights_and_consistency(A_nature)
    print(weights_nature, CI_nature, CR_nature)





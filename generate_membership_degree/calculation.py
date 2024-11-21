import pandas as pd
import numpy as np
import re
from scipy.stats import norm


# 定义转换字符串表示的元组为实际元组的函数
def to_tuple(s):
    return tuple(map(float, re.findall(r"[\d\.\-]+", s)))


# 自定义矩阵乘法函数
def custom_matrix_multiplication(A, B):
    if A.shape[0] != 1 or B.shape[1] != 5 or A.shape[1] != B.shape[0]:
        raise ValueError(
            "Invalid shapes for the matrices. A must be 1xn and B must be nx5, where n is the number of columns in A.")

    C = np.zeros((1, 5))
    for col in range(5):
        sum_squares = 0
        for row in range(A.shape[1]):
            sum_squares += (A[0, row] * B[row, col]) ** 2
        C[0, col] = np.sqrt(sum_squares)

    return C


# 加载等级.xlsx文件
grades_path = '等级输出.xlsx'
grades_data = pd.read_excel(grades_path)

# 初始化Ex, En, He矩阵
rows, cols = grades_data.shape
Ex = np.zeros((rows, cols - 1))
En = np.zeros((rows, cols - 1))
He = np.zeros((rows, cols - 1))


# 填充Ex, En, He矩阵
for i in range(rows):
    for j in range(1, cols):
        val_tuple = to_tuple(grades_data.iloc[i, j])
        Ex[i, j - 1], En[i, j - 1], He[i, j - 1] = val_tuple

# 加载test.xlsx文件
test_path = 'input/50results.xlsx'
test_data = pd.read_excel(test_path)
test_data_processed = test_data.drop(columns=['FID', 'OBJECTID'])

# 定义随机样本数和固定矩阵
M = 100

fixed_matrix_Ex = np.array(
    [[0.239, 0.188, 0.111, 0.094, 0.031, 0.033, 0.035, 0.022, 0.063, 0.059, 0.097, 0.015, 0.011]])
fixed_matrix_En = np.array(
    [[0.333, 0.265, 0.157, 0.133, 0.044, 0.048, 0.051, 0.032, 0.089, 0.084, 0.139, 0.022, 0.016]])
fixed_matrix_He = np.array(
    [[0.33, 0.265, 0.157, 0.133, 0.044, 0.047, 0.052, 0.032, 0.091, 0.085, 0.141, 0.022, 0.016]])

# 计算每行数据的隶属度矩阵和最终结果矩阵
final_results = []

for index, row in test_data_processed.iterrows():
    samples = row.values
    R = np.zeros((13, 5))

    for a in range(13):
        min_value = np.min(Ex[a, :])  # Find the minimum value for each group (indicator)
        max_value = np.max(Ex[a, :])  # Find the maximum value for each group (indicator)
        if samples[a] < min_value:
            min_index = np.argmin(Ex[a, :])  # Find the index of the minimum value
            R[a, min_index] = 1  # Set the membership of the corresponding level to 1
        elif samples[a] > max_value:
            max_index = np.argmax(Ex[a, :])  # Find the index of the maximum value
            R[a, max_index] = 1
        else:
            for b in range(5):
                X = norm.rvs(loc=En[a, b], scale=He[a, b], size=M)
                Y = np.exp(-((samples[a] - Ex[a, b]) ** 2) / (2 * X ** 2))
                R[a, b] = np.mean(Y)


    # 使用自定义矩阵乘法计算
    result_Ex = np.dot(fixed_matrix_Ex, R).flatten()
    result_En = custom_matrix_multiplication(fixed_matrix_En, R).flatten()
    result_He = custom_matrix_multiplication(fixed_matrix_He, R).flatten()

    # 将三个结果整合为(**,**,**)格式的矩阵
    combined_results = np.array([(result_Ex[i], result_En[i], result_He[i]) for i in range(len(result_Ex))])
    final_results.append(combined_results)

# 准备将结果输出到Excel文件中
output_df = pd.DataFrame({
    f"Result_{i + 1}": [result for result in final_results[i]] for i in range(len(final_results))
})

# 转换DataFrame以适应(**,**,**)格式要求
for col in output_df.columns:
    output_df[col] = output_df[col].apply(lambda x: f"({x[0]:.3f}, {x[1]:.3f}, {x[2]:.3f})")

# 输出到Excel文件
output_path = 'final_results.xlsx'
output_df.T.to_excel(output_path, header=False)

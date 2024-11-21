# import pandas as pd
#
#
# # 定义用于读取和处理Excel文件的函数
# def process_excel(file_path, output_path):
#     # 读取Excel文件，不使用任何一行作为标题
#     df = pd.read_excel(file_path, header=None)
#
#     # 固定的A矩阵
#     A = [[0, 1.308, 0.13],
#          [3.09, 0.809, 0.08],
#          [5, 0.50, 0.05],
#          [6.91, 0.809, 0.08],
#          [10, 1.308, 0.13]]
#
#     # 解析字符串三元组并返回浮点数元组
#     def parse_tuple(string):
#         return tuple(map(float, string.strip("()").split(",")))
#
#     # 计算每一行的结果
#     def calculate_row(row):
#         B = [parse_tuple(row[i]) for i in range(1, 6)]  # 提取B矩阵
#         result = [0, 0, 0]
#         for i in range(len(A[0])):
#             temp_sum = 0
#             for j in range(len(A)):
#                 temp_sum += A[j][i] * B[j][i]
#             result[i] = round(temp_sum, 3)
#         return result
#
#     # 应用计算并添加结果到新列
#     df['Calculated_Result'] = df.apply(calculate_row, axis=1)
#
#     # 将处理后的DataFrame保存到新的Excel文件
#     df.to_excel(output_path, index=False, header=False)
#
#
# # 指定文件路径
# file_path = 'final_results.xlsx'
# output_path = 'processed_results.xlsx'
#
# # 调用函数处理并保存文件
# process_excel(file_path, output_path)
#
# # 返回新文件的路径，以便下载或进一步操作
# output_path

import pandas as pd

# 定义用于读取和处理Excel文件的函数
def process_excel(file_path, output_path):
    # 读取Excel文件，不使用任何一行作为标题
    df = pd.read_excel(file_path, header=None)

    # 固定的A矩阵
    A = [[0, 1.308, 0.13],
         [3.09, 0.809, 0.08],
         [5, 0.50, 0.05],
         [6.91, 0.809, 0.08],
         [10, 1.308, 0.13]]

    # 解析字符串三元组并返回浮点数元组
    def parse_tuple(string):
        return tuple(map(float, string.strip("()").split(",")))

    # 计算每一行的结果，并返回三个独立的值
    def calculate_row(row):
        B = [parse_tuple(row[i]) for i in range(1, 6)]  # 提取B矩阵
        results = []
        for i in range(3):  # 有三个结果需要计算
            temp_sum = 0
            for j in range(len(A)):
                temp_sum += A[j][i] * B[j][i]
            results.append(round(temp_sum, 3))
        return results

    # 分别为计算结果指定列名并添加到DataFrame中
    results = df.apply(calculate_row, axis=1)
    df[['Ex', 'En', 'He']] = pd.DataFrame(results.tolist(), index=df.index)

    # 将处理后的DataFrame保存到新的Excel文件
    df.to_excel(output_path, index=False, header=False)

# 指定文件路径
file_path = 'final_results.xlsx'
output_path = '与评价集相乘结果.xlsx'

# 调用函数处理并保存文件
process_excel(file_path, output_path)

# 输出语句用于演示，实际应用时可移除
print("处理完成，结果已保存至:", output_path)

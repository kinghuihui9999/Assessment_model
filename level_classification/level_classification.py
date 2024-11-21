import pandas as pd

# 假设df是你的数据表格，加载你的Excel文件到DataFrame
df = pd.read_excel('data/等级划分.xlsx')

# 定义计算Ex, En, He的函数
def calculate_cloud_model(c_min, c_max):
    Ex = round((c_min + c_max) / 2, 3)
    En = round((c_max - c_min) / 2.35, 3)
    He = round(En/3, 3)  # 由于He是常量，直接返回0.1
    return Ex, En, He

# 应用函数到每个单元格
for column in df.columns[1:]:  # 跳过第一列的指标名称
    for row in range(len(df)):
        c_min, c_max = map(float, df[column][row].split(', '))
        df.at[row, column] = calculate_cloud_model(c_min, c_max)

# 保存新的Excel文件
df.to_excel('output/等级输出.xlsx', index=False)

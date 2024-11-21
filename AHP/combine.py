import pandas as pd


# Function to parse string values in the data cells
def parse_value(value):
    if ',' in value:
        parts = value.split(',')
        numbers = [float(eval(part)) if '/' in part else float(part) for part in parts]
        return tuple(numbers)
    else:
        return (float(value),)


# Read each sheet (each expert's judgement matrix) into a dataframe
def read_sheets(file_path):
    xls = pd.ExcelFile(file_path)
    sheets = {}
    for sheet_name in xls.sheet_names:
        df = xls.parse(sheet_name)
        # Apply the parse_value function to each cell in the dataframe, skipping the first column
        for col in df.columns[1:]:
            df[col] = df[col].apply(parse_value)
        sheets[sheet_name] = df.set_index(df.columns[0])
    return sheets


# Function to calculate weighted average
def weighted_average(values, weights):
    return sum(v * w for v, w in zip(values, weights)) / sum(weights)


# Calculate the combined judgement matrix
def calculate_combined_matrix(sheets, weights):
    combined_matrix = pd.DataFrame(index=sheets[list(sheets.keys())[0]].index,
                                   columns=sheets[list(sheets.keys())[0]].columns)
    for index, row in combined_matrix.iterrows():
        for col in combined_matrix.columns:
            ex_values = [sheets[expert].at[index, col][0] for expert in sheets]
            en_values = [sheets[expert].at[index, col][1] for expert in sheets]
            he_values = [sheets[expert].at[index, col][2] for expert in sheets]

            # Calculate the weighted values for ex, en, and he
            combined_ex = weighted_average(ex_values, weights)
            combined_en = weighted_average(en_values, weights)
            combined_he = (sum(v ** 2 for v in he_values) ** 0.5)

            # Set the combined values in the combined_matrix
            combined_matrix.at[index, col] = (combined_ex, combined_en, combined_he)
    return combined_matrix


# Load the Excel file and read each sheet
file_path = '权重/level1.xlsx'  # Replace with the path to your Excel file
sheets = read_sheets(file_path)

# Define weights for the experts
weights = [1/3, 1/3, 1/3]  # Assuming equal weight for each expert

# Calculate the combined judgement matrix with the given weights
combined_matrix = calculate_combined_matrix(sheets, weights)
def format_matrix(matrix):
    formatted_matrix = matrix.copy()
    for index, row in matrix.iterrows():
        for col in matrix.columns:
            formatted_matrix.at[index, col] = '({:.3f}, {:.3f}, {:.3f})'.format(*matrix.at[index, col])
    return formatted_matrix

# Format and print the combined judgement matrix
formatted_combined_matrix = format_matrix(combined_matrix)
# 将 formatted_combined_matrix 写入 Excel 文件
formatted_combined_matrix.to_excel('output.xlsx', index=True, header=True)


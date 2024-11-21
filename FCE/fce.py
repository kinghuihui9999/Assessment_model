import pandas as pd
def sharpened_membership(x, a, b):
    if x < a:
        return 1
    elif a <= x < b:
        return (b - x) / (b - a)
    else:
        return 0

def intermediate_membership(x, a, b, c, d):
    if x < a:
        return 0
    elif a <= x < b:
        return (x - a) / (b - a)
    elif b <= x < c:
        return 1
    elif c <= x < d:
        return (d - x) / (d - c)
    else:
        return 0


def both_ends_membership(x, a, b):
    if x < a:
        return 0
    elif a <= x <= b:
        return (x - a) / (b - a)
    else:
        return 1


# Now we will apply the appropriate membership function for each indicator and level
# We will also store the calculated membership degrees in a new DataFrame

# Load the data
data = pd.read_excel('data.xlsx')

# Create a new DataFrame to hold the membership degrees
membership_degrees = pd.DataFrame()

# Loop through each row in the dataset to calculate the membership degree for each level
for index, row in data.iterrows():
    indicator_value = row['指标值']
    indicator_name = row['指标']

    # The abcdefg values need to be retrieved for each indicator
    # For "闸门", we use the provided values directly
    if indicator_name == '闸门':
        params = {'a':30, 'b': 60, 'c': 60, 'd': 70, 'e': 80, 'f': 90, 'g': 100}
    else:
        l1_lower, l1_upper = [float(x) for x in row['L1'].split(', ')]
        l5_upper = float(row['L5'].split(', ')[1])
        interval_length = l1_upper - l1_lower
        params = {
            'a': 0 + 0.5 * interval_length, #10
            'b': l1_upper , #20
            'c': l1_upper + interval_length, #30
            'd': l1_upper + 2*interval_length, #40
            'e': l1_upper + 3 * interval_length,
            'f': l1_upper + 4 * interval_length,
            'g': l5_upper
        }

    # Calculate the membership degree for each level and store in the DataFrame
    membership_degrees.loc[index, '指标'] = indicator_name
    membership_degrees.loc[index, 'L1'] = sharpened_membership(indicator_value, params['a'], params['b'])
    membership_degrees.loc[index, 'L2'] = intermediate_membership(indicator_value, params['a'], params['b'],
                                                                  params['c'], params['d'])
    membership_degrees.loc[index, 'L3'] = intermediate_membership(indicator_value, params['b'], params['c'],
                                                                  params['d'], params['e'])
    membership_degrees.loc[index, 'L4'] = intermediate_membership(indicator_value, params['c'], params['d'],
                                                                  params['e'], params['f'])
    membership_degrees.loc[index, 'L5'] = both_ends_membership(indicator_value, params['d'], params['e'])

print(membership_degrees)

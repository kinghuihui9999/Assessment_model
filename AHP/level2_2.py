import numpy as np
from level2_1 import calculate_weights_and_consistency
#        人口  建筑  消防  公安  医院  道路  管网
# 人口    1    2    1/2  1/2  1/4  3    4
# 建筑    1/2  1    1/3  1/3  1/5  2    3
# 消防    2    3    1    1    1/2  4    5
# 公安    2    3    1    1    1/2  4    5
# 医院    4    5    2    2    1    6    7
# 道路    1/3  1/2  1/4  1/4  1/6  1    2
# 管网    1/4  1/3  1/5  1/5  1/7  1/2  1

A_social = np.array([
    [1, 2, 1/2, 1/2, 1/4, 3, 4],
    [1/2, 1, 1/3, 1/3, 1/5, 2, 3],
    [2, 3, 1, 1, 1/2, 4, 5],
    [2, 3, 1, 1, 1/2, 4, 5],
    [4, 5, 2, 2, 1, 6, 7],
    [1/3, 1/2, 1/4, 1/4, 1/6, 1, 2],
    [1/4, 1/3, 1/5, 1/5, 1/7, 1/2, 1]
])


weights_social, CI_social, CR_social = calculate_weights_and_consistency(A_social)
print(weights_social, CI_social, CR_social)





A = [[0,1.308,0.13],
     [3.09,0.809,0.08],
     [5,0.50,0.05],
     [6.91,0.809,0.08],
     [10,1.308,0.13]]

B = [[0.275, 0.283, 0.281],
     [0.066, 0.080, 0.080],
     [0.060, 0.069, 0.069],
     [0.001, 0.001, 0.001],
     [0.000, 0.000, 0.000]]

result = []
for i in range(len(A[0])):
    temp_sum = 0
    for j in range(len(A)):
        temp_sum += A[j][i] * B[j][i]
    result.append(temp_sum)


print(result)
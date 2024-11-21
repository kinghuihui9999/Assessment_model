import math
A_Ex = [3.5, 5.5, 5.2, 6.5, 5.5]
B_Ex = [0.148716, 0.760104, 0.052562, 0.015908, 0.01353]
A_En = [1.5, 1.5, 1.167, 1.5, 1.5]
B_En = [0.143, 0.852, 0.397, 0.120,0.107]
A_He = [0.1, 0.1, 0.1, 0.1, 0.1]
B_He = [0.219, 0.826, 0.323, 0.098, 0.085]

# # 计算Ex
Ex = sum(a*b for a, b in zip(A_Ex, B_Ex))
En = sum(a*b for a, b in zip(A_En, B_En))
He = sum(a*b for a, b in zip(A_He, B_He))

# # 计算En
# En_squared = sum((abs(A_Ex[i] * B_Ex[i]) * math.sqrt((A_En[i]/A_Ex[i])**2 + (B_En[i]/B_Ex[i])**2))**2 for i in range(len(A_Ex)))
# En = math.sqrt(En_squared)

# # 计算He
# He_squared = sum((abs(A_Ex[i] * B_Ex[i]) * math.sqrt((A_He[i]/A_Ex[i])**2 + (B_He[i]/B_Ex[i])**2))**2 for i in range(len(A_Ex)))
# He = math.sqrt(He_squared)

print(Ex, En, He)




import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 设置中文显示和负号显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def plot_cloud_model(Ex, En, He, n, ax, label='', marker='o', color='blue'):
    # 初始化Y数组
    Y = np.zeros(n)

    # 生成初始的Enn值
    X = norm.rvs(loc=En, scale=He, size=n)

    # 按要求修改计算部分
    for k in range(n):
        E1 = X[k]
        X[k] = norm.rvs(loc=Ex, scale=np.abs(E1), size=1)  # 确保标准差为正
        Y[k] = np.exp(-((X[k] - Ex) ** 2) / (2 * (E1 ** 2)))

    # 绘制散点图，使用指定颜色
    ax.scatter(X, Y, s=10, alpha=0.5, marker=marker, label=label, color=color)

if __name__ == '__main__':
    fig, ax = plt.subplots()  # 简化画布和轴的创建

    ax.set_xlabel('期望')
    ax.set_ylabel('隶属度')

    # 为每个云图指定不同的颜色
    plot_cloud_model(0, 1.308, 0.13, 2000, ax, color='blue')  # 蓝色
    plot_cloud_model(3.09, 0.809, 0.08, 2000, ax, color='green')  # 绿色
    plot_cloud_model(5, 0.50, 0.05, 2000, ax, color='red')  # 红色
    plot_cloud_model(6.91, 0.809, 0.08, 2000, ax, color='purple')  # 紫色
    plot_cloud_model(10, 1.308, 0.13, 2000, ax, color='orange')  # 橙色

    # plot_cloud_model(8.749, 0.83, 0.082, 2000, ax, 'Grid_20775', color='red')
    # plot_cloud_model(1.732, 0.842, 0.084, 2000, ax, 'Grid_11466', color='blue')


    ax.legend(loc='best')
    plt.xlim(0, 10)
    plt.show()

import numpy as np
# 使用det函数求行列式
arr = np.array([[1, -3],[4,3]])
arr1 = np.array([[-5,-3],[-5,3]])
arr2 = np.array([[1,-5],[4,-5]])
# 求解
D = np.linalg.det(arr)
D1 = np.linalg.det(arr1)
D2 = np.linalg.det(arr2)
print("方程组1的解为：",D1/D)
print("方程组2的解为：",D2/D)

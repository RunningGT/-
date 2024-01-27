import numpy as np
from numpy import *
A = np.arange(14, 2, -1).reshape(4, 3)

# print(A)
# print(np.argmin(A))
# print(np.argmax(A))
# print(np.mean(A))
# print(np.median(A))
# print(np.diff(A))
# print(np.nonzero(A))
# print(transpose(A))
# print(sort(A))
# print(A.T)

# 创建一个多维数组
arr = np.array([[3, 1, 4],
                [1, 5, 9],
                [2, 6, 5]])

# 使用numpy.sort按总体排序
sorted_arr = np.sort(arr, axis=None)

print("按总体排序后的数组：")
print(sorted_arr)
# 创建一个多维数组
arr = np.array([[3, 1, 4],
                [1, 5, 9],
                [2, 6, 5]])

# 获取按总体排序的索引
indices = np.argsort(arr, axis=None)

# 使用索引重新排列原始数组
sorted_arr = arr.flatten()[indices].reshape(arr.shape)

print("按总体排序后的数组：")
print(sorted_arr)

import numpy as np
A = np.matrix([[2,1,-1], [0,1,2]])
B = np.matrix([[1,-1,2], [2,1,4], [-1,2,0]])
print("矩阵AB为:\n", A * B)

arr_A = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15],[16, 17, 18]]])
print(arr_A)
print(arr_A.ndim)
print(arr_A[1, 1, 1])

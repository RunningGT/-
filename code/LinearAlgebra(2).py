import numpy as np
#使用det函数求行列式
arr = np.array([[3,-1,1],[2,-4,-1],[1,2,1]])
arr1 = np. array([[26,-1,1],[9,-4,-1],[16,2,1]])
arr2 = np.array([[3,26,1],[2,9,-1],[1,16,1]])
arr3 = np.array([[3,-1,26],[2,-4,9],[1,2,16]])
#求解行列式
D = np.linalg.det(arr)
D1 = np.linalg.det(arr1)
D2 = np.linalg.det(arr2)
D3 = np.linalg.det(arr3)
print("系数行列式 D 为: ",D)
print("D1 为:",D1)
print("D2 为:",D2)
print("D3 为:",D3)
print("方程组的解x1为: ",D1/D)
print("方程组的解x2为: ",D2/D)
print("方程组的解x3为: ",D3/D)
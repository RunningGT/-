import numpy as np
from math import pi
a = np.array([[10, 20], [30, 40]])
b = np.arange(4).reshape(2,2)
c = a * b
c_dot = np.dot(a, b)
print(a, end="\n\n")
print(b, end="\n\n")
print(c,end="\n\n")
print(c_dot)
"""
d = np.array([pi / 2, pi, 3 * pi / 2])
print(np.sin(d))
print(np.cos(d))
print(np.tan(d))
print(np.arctan(d))
"""
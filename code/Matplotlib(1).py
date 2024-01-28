import matplotlib.pyplot as plt
import numpy as np
import math
x = np.linspace(3, -3, 50)
y1 = x**2
y2 = math.e**x
y3 = 1/x

plt.figure()
plt.plot(x, y3)

plt.savefig("my_plot(3).png")

plt.figure()
plt.plot(x, y1)
plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--')

plt.savefig("my_plot(4).png")
plt.show()

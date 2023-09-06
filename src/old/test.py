import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.1)

for i in range(3):
    y = np.sin(x + i)
    plt.plot(x, y, label=f"Curve {i+1}")

plt.legend()
plt.show()

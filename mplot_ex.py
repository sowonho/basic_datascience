import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1,2,2)
plt.plot(x, y)

plt.grid()

ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.subplot(1,2, 1)
plt.plot(ypoints)

plt.show()

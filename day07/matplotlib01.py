import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 4*np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin)
# plt.show()

plt.plot(x, y_cos)
plt.xlabel('degree')
plt.ylabel('sine and cosine')
plt.title('sine and cosine graph')


plt.show()

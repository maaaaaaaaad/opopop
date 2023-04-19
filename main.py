import numpy as np
import matplotlib.pyplot as plt

x_min, x_max = -np.pi, np.pi
y_min, y_max = -1.2, 1.2
x = np.arange(x_min, x_max, 0.01)
sin_data = np.sin(x)
cos_data = np.cos(x)
tan_data = np.tan(x)
fig, ax = plt.subplots()
ax.set_title('graph of trigonometric functions')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_xlim([x_min, x_max])
ax.set_ylim([y_min, y_max])
ax.plot(x, sin_data, color='red', label='sin(x)')
ax.plot(x, cos_data, color='green', label='cos(x)')
ax.plot(x, tan_data, color='blue', label='tan(x)')
ax.legend()
plt.show()

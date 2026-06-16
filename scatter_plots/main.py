import matplotlib.pyplot as plt
import numpy as np
x = np.array([6, 1, 8, 20, 13, 4, 16, 5, 11, 10])
# Square the elements of the x array
y = x ** 2
# Create a scatter plot
plt.scatter(x, y, s=70)
plt.show()
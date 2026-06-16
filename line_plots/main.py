import matplotlib.pyplot as plt
import numpy as np
x_data = np.arange(1, 11)
y_data = -x_data
# Create a line plot
plt.plot(x_data, y_data, '-o')
plt.show()
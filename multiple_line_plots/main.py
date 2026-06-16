import matplotlib.pyplot as plt
import numpy as np
data_linear = np.arange(0, 11)
data_squared = data_linear ** 2
# Create the first line plot
plt.plot(data_linear)
# Create the second line plot with markers
plt.plot(data_squared, '-o')
plt.show()
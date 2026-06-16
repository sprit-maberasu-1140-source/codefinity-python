import matplotlib.pyplot as plt
import numpy as np

data_linear = np.arange(1, 11)
data_squared = data_linear ** 2
data_exp = np.exp(data_linear)

# Create a subplot grid
fig, axs = plt.subplots(3, 1, sharex=True)

# Place the first line plot on the first row
axs[0].plot(data_linear, color='red')

# Place the second line plot on the second row
axs[1].plot(data_squared, color='blue')

# Place the third line plot on the third row
axs[2].plot(data_exp, color='orange')

plt.show()
import matplotlib.pyplot as plt
import numpy as np

data_linear = np.arange(0, 11)
data_squared = data_linear ** 2

plt.plot(data_linear, label='linear function')
plt.plot(data_squared, '-o', label='quadratic function')

# Set x-axis ticks
plt.xticks(data_linear)

# Set x-axis label
plt.xlabel('x', loc='right')

# Set y-axis label
plt.ylabel('y', loc='top', rotation=0)

plt.legend()
plt.show()
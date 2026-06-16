import matplotlib.pyplot as plt
import numpy as np

size = 1000
normal_sample_1 = np.random.normal(size=size)
normal_sample_2 = np.random.normal(size=size)

# Create two box plots for these two samples
plt.boxplot([normal_sample_1, normal_sample_2], tick_labels=['First sample', 'Second sample'])

plt.show()
import matplotlib.pyplot as plt
import numpy as np

countries = ['USA', 'China', 'Japan']

primary_sector = np.array([1.4, 4.8, 0.4])
secondary_sector = np.array([11.3, 6.2, 0.8])
tertiary_sector = np.array([14.2, 8.4, 3.2])

# Set the correct color
plt.bar(countries, primary_sector, label='primary sector', color='darkslateblue')

# Set the correct color and transparency value
plt.bar(countries, secondary_sector, bottom=primary_sector, label='secondary sector', color='steelblue', alpha=0.7)

# Set the correct color
plt.bar(countries, tertiary_sector, bottom=primary_sector + secondary_sector, label='tertiary sector', color='goldenrod')

plt.legend()
plt.show()
import matplotlib.pyplot as plt
countries = ['USA', 'Japan', 'China', 'Germany']
gdp_list = [26.9, 4.4, 19.4, 4.3]
# Create a bar chart
plt.bar(countries, gdp_list, width=[0.6, 0.45, 0.9, 0.2])
plt.show()
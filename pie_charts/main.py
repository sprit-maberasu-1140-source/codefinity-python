import matplotlib.pyplot as plt

names = ['person_1', 'person_2', 'person_3', 'person_4']
incomes = [100000, 87000, 150000, 45000]

# Create a pie chart
plt.pie(incomes, labels=names, autopct='%1.1f%%')

plt.show()
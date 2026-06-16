# Import seaborn with the sns alias
import seaborn as sns

# Import matplotlib.pyplot with the plt alias
import matplotlib.pyplot as plt

# Loading a built-in dataset of diamonds
diamonds = sns.load_dataset('diamonds')

# Create a countplot
sns.countplot(data=diamonds, y='cut')

# Display the countplot
plt.show()
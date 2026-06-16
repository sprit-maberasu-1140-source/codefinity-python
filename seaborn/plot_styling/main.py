import seaborn as sns
import matplotlib.pyplot as plt

# Set the style
sns.set_style('dark')

# Set the palette
sns.set_palette('rocket')

# Set the context
sns.set_context('talk')

# Loading a built-in dataset of the Titanic passengers
titanic_df = sns.load_dataset('titanic')

sns.countplot(data=titanic_df, x='class')
plt.show()
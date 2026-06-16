import seaborn as sns
import matplotlib.pyplot as plt

# Ignoring warnings
import warnings
warnings.filterwarnings('ignore')

# Loading the dataset with data about the penguins features
penguins_df = sns.load_dataset('penguins')

# Create a pair plot with the correct arguments
sns.pairplot(penguins_df, hue='sex', kind='reg', height=2, aspect=0.8)

plt.show()
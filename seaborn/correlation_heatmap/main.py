import seaborn as sns
import matplotlib.pyplot as plt

# Loading the dataset with data about the penguins features
penguins_df = sns.load_dataset('penguins')

# Create a correlation matrix with all numeric variables
correlation_matrix = penguins_df.corr(numeric_only=True)

# Create a heatmap based on the correlation matrix
sns.heatmap(correlation_matrix, annot=True, cmap='crest')

# Rotate the ticks by 15 degrees counterclockwise 
plt.xticks(rotation=15)
plt.yticks(rotation=15)

plt.show()
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Loading the dataset with the average yearly temperatures in Boston and Seattle
url = 'https://content-media-cdn.codefinity.com/courses/47339f29-4722-4e72-a0d4-6112c70ff738/weather_data.csv'
weather_df = pd.read_csv(url, index_col=0)

# Create a jointplot with the correct arguments
sns.jointplot(data=weather_df, x='Boston', y='Seattle', kind='reg')

plt.show()
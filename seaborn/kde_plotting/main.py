import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Loading the dataset with the countries data
url = 'https://content-media-cdn.codefinity.com/courses/47339f29-4722-4e72-a0d4-6112c70ff738/countries_data.csv'
countries_df = pd.read_csv(url, index_col=0)

# Create a KDE plot
sns.kdeplot(data=countries_df, y='GDP per capita', fill=True)

plt.show()
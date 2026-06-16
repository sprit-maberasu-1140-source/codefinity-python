import pandas as pd
import matplotlib.pyplot as plt

# Loading the dataset with the average yearly temperatures in Boston and Seattle
url = 'https://content-media-cdn.codefinity.com/courses/47339f29-4722-4e72-a0d4-6112c70ff738/weather_data.csv'
weather_df = pd.read_csv(url, index_col=0)

plt.plot(weather_df['Boston'], label='Boston')
plt.plot(weather_df['Seattle'], label='Seattle')

plt.title('Boston and Seattle average yearly temperatures')
plt.legend(loc='upper left')
plt.xticks(range(1995, 2021, 2), rotation=30)

# Customize the grid
plt.grid(True, axis='y', color='slategrey', alpha=0.5)

plt.show()
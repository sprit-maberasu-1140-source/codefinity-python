import pandas as pd
import matplotlib.pyplot as plt
url = 'https://content-media-cdn.codefinity.com/courses/47339f29-4722-4e72-a0d4-6112c70ff738/weather_data.csv'
weather_df = pd.read_csv(url, index_col=0)
plt.figure(figsize=(8, 6))
plt.plot(weather_df['Boston'])
plt.plot(weather_df['Seattle'])
# Set the title of the plot
plt.title('Boston and Seattle average yearly temperatures', fontsize=15, loc='right')
plt.show()
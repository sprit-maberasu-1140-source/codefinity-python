import geopandas as gpd
import matplotlib.pyplot as plt

# Load the world countries dataset from Natural Earth (GeoJSON format)
world_url = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_admin_0_countries.geojson"
world = gpd.read_file(world_url)

# Filter for European countries using the 'CONTINENT' column
continent = 'Europe'
europe = world[world['CONTINENT'] == continent]

# Plot all world countries in light gray
ax = world.plot(color='lightgray', edgecolor='white', figsize=(10, 6))

# Overlay European countries in a distinct color (not blue or green)
europe.plot(ax=ax, color='goldenrod', edgecolor='black', label='Europe')

# Add a title and legend
plt.title("Countries of Europe")
plt.legend()
plt.show()
import geopandas as gpd
import matplotlib.pyplot as plt


def plot_comparison_grid(gdf1, gdf2, attribute, title1, title2):
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    cmap = 'viridis'
    
    vmin = min(float(gdf1[attribute].min()), float(gdf2[attribute].min()))
    vmax = max(float(gdf1[attribute].max()), float(gdf2[attribute].max()))
    
    gdf1.plot(column=attribute, ax=axes[0], legend=True, cmap=cmap, edgecolor='black', vmin=vmin, vmax=vmax)
    axes[0].set_title(title1)
    axes[0].set_axis_off()
    
    gdf2.plot(column=attribute, ax=axes[1], legend=True, cmap=cmap, edgecolor='black', vmin=vmin, vmax=vmax)
    axes[1].set_title(title2)
    axes[1].set_axis_off()
    
    plt.tight_layout()
    plt.show()

# Example usage with built-in world data
url = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"
world = gpd.read_file(url)

# Make sure we use the uppercase CONTINENT and POP_EST matching the official dataset
africa = world[world['CONTINENT'] == 'Africa']
asia = world[world['CONTINENT'] == 'Asia']

plot_comparison_grid(africa, asia, 'POP_EST', 'Africa Population', 'Asia Population')
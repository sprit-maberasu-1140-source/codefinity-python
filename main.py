import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Point, box

# Direct URL to raw NYC Borough Boundaries GeoJSON (No special headers needed)
nyc_url = "https://raw.githubusercontent.com/datasets/geo-boundaries-nyc-boroughs/master/nyc_boroughs.geojson"

print("Loading real NYC dataset from URL...")
nyc_boroughs = gpd.read_file(nyc_url).to_crs("EPSG:2263")

# Extract Real Bounding Box parameters
minx, miny, maxx, maxy = nyc_boroughs.total_bounds

# Generate Simulated Real-World Incidents (500 points inside NYC bounds)
np.random.seed(42)
points = [
    Point(x, y)
    for x, y in zip(
        np.random.uniform(minx, maxx, 500), np.random.uniform(miny, maxy, 500)
    )
]

# Create point layer using the identical Coordinate System (CRS) as the NYC map
sample_gdf = ___

# Clip the points so they sit perfectly inside the actual landmass profiles of NYC
sample_gdf = ___


def create_grid(data, grid_size):
    l_minx, l_miny, l_maxx, l_maxy = data.total_bounds
    x_coords = np.arange(l_minx, l_maxx + grid_size, grid_size)
    y_coords = np.arange(l_miny, l_maxy + grid_size, grid_size)

    grid_cells = []
    for x in x_coords[:-1]:
        for y in y_coords[:-1]:
            ___
            
    grid = ___
    grid["grid_id"] = grid.index

    spatial_join = ___
    return grid, spatial_join


def aggregate_in_grid(spatial_join):
    aggregated = (
        ___
    )
    return aggregated


def plot_grid(grid, aggregated, baseline_map):
    # Attach data metrics back onto the spatial grid mesh
    grid_with_counts = grid.merge(aggregated, on="grid_id", how="left").fillna(
        {"count": 0}
    )

    fig, ax = plt.subplots(figsize=(10, 8))

    # Draw real background map boundaries to add situational context
    baseline_map.plot(ax=ax, color="whitesmoke", edgecolor="darkgray", alpha=0.5)

    # Plot the aggregated density block grids over it
    grid_with_counts.plot(
        column="count",
        ax=ax,
        cmap="YlGnBu",
        edgecolor="k",
        linewidth=0.3,
        legend=True,
        alpha=0.8,
    )

    plt.title("Spatial Density Distribution Over NYC Bounds (Real Data)")
    plt.xlabel("X Coordinate (State Plane Feet)")
    plt.ylabel("Y Coordinate (State Plane Feet)")
    plt.tight_layout()
    plt.show()


# Processing using the real-world dataset framework
grid_size_feet = 5000  # 5,000 feet grid blocks

grid, spatial_join = create_grid(sample_gdf, grid_size_feet)
aggregated = aggregate_in_grid(spatial_join)

# Render grid with real background map geometry
plot_grid(grid, aggregated, nyc_boroughs)
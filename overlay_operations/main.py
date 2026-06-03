import geopandas as gpd
from shapely import wkt

def perform_overlay(df1, df2, operation):
    if operation not in ["intersection", "union", "difference"]:
        raise ValueError("Invalid operation")
    return gpd.overlay(df1, df2, how=operation)

# Sample polygons for testing
poly1 = gpd.GeoDataFrame(
    {'id': [1]},
    geometry=gpd.GeoSeries.from_wkt(['POLYGON((0 0, 2 0, 2 2, 0 2, 0 0))'])
)
poly2 = gpd.GeoDataFrame(
    {'id': [2]},
    geometry=gpd.GeoSeries.from_wkt(['POLYGON((1 1, 3 1, 3 3, 1 3, 1 1))'])
)

result_intersection = perform_overlay(poly1, poly2, "intersection")
print("Intersection:\n", result_intersection)

result_union = perform_overlay(poly1, poly2, "union")
print("\nUnion:\n", result_union)

result_difference = perform_overlay(poly1, poly2, "difference")
print("\nDifference:\n", result_difference)
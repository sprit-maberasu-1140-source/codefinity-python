def scale_polygon(polygon, scale_factor):
    scaled = []
    for x, y in polygon:
        scaled.append((x * scale_factor, y * scale_factor))
    return scaled

# Sample calls
polygon1 = [(1, 2), (3, 4), (5, 6)]
scaled_polygon1 = scale_polygon(polygon1, 2)
print(scaled_polygon1)

polygon2 = [(-1, -1), (0, 0), (1, 1)]
scaled_polygon2 = scale_polygon(polygon2, 0.5)
print(scaled_polygon2)
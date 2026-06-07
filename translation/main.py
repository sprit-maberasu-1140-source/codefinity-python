def translate_polygon(polygon, vector):
    translated = []
    for x, y in polygon:
        new_point = (x + vector[0], y + vector[1])
        translated.append(new_point)
    return translated

# Sample calls
polygon1 = [(0, 0), (1, 0), (1, 1), (0, 1)]
vector1 = (2, 3)
translated_polygon1 = translate_polygon(polygon1, vector1)
print(translated_polygon1)

polygon2 = [(-1, -1), (2, -1), (2, 2), (-1, 2)]
vector2 = (0, -2)
translated_polygon2 = translate_polygon(polygon2, vector2)
print(translated_polygon2)

def are_collinear(p1, p2, p3):
    # Write your code here
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    # Calculate the area of triangle formed by the points
    area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    return area == 0

# Sample calls
result1 = are_collinear((0, 0), (1, 1), (2, 2))
print(result1)
result2 = are_collinear((0, 0), (1, 2), (2, 1))
print(result2)
result3 = are_collinear((1, 2), (2, 4), (3, 6))
print(result3)

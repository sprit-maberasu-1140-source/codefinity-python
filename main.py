import math
import matplotlib.pyplot as plt

def approximate_ellipse(a, b, num_points):
    points = []
    for i in range(num_points):
        theta = 2 * math.pi * i / num_points
        x = a * math.cos(theta)
        y = b * math.sin(theta)
        points.append((x, y))
    return points

def plot_ellipse(points):
    x_values = [pt[0] for pt in points]
    y_values = [pt[1] for pt in points]
    x_values.append(points[0][0])
    y_values.append(points[0][1])
    plt.figure(figsize=(6,6))
    plt.plot(x_values, y_values, marker='o')
    plt.title("Ellipse Approximation")
    plt.axis('equal')
    plt.show()

ellipse_points = approximate_ellipse(5, 3, 60)
plot_ellipse(ellipse_points)
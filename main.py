import numpy as np
import matplotlib.pyplot as plt

def approximate_curve_with_polygon(curve_func, interval, num_vertices):
    x_values = np.linspace(interval[0], interval[1], num_vertices)
    y_values = curve_func(x_values)
    vertices = list(zip(x_values, y_values))
    return vertices

def curve_func(x):
    return np.sin(x)

interval = (0, 2 * np.pi)
num_vertices = 8
polygon_vertices = approximate_curve_with_polygon(curve_func, interval, num_vertices)
print(polygon_vertices)

x_curve = np.linspace(interval[0], interval[1], 100)
y_curve = curve_func(x_curve)
x_poly = [v[0] for v in polygon_vertices]
y_poly = [v[1] for v in polygon_vertices]
plt.plot(x_curve, y_curve, label="Curve")
plt.plot(x_poly, y_poly, marker='o', label="Polygon Approximation")
plt.legend()
plt.show()
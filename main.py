import matplotlib.pyplot as plt

def plot_polygon(vertices):
    x_coords = [vertex[0] for vertex in vertices]
    y_coords = [vertex[1] for vertex in vertices]
    x_closed = x_coords + [x_coords[0]]
    y_closed = y_coords + [y_coords[0]]
    plt.figure()
    plt.plot(x_closed, y_closed, marker='o')
    plt.title("Polygon Plot")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.axis('equal')
    plt.show()

vertices1 = [(0, 0), (2, 0), (1, 2)]
plot_polygon(vertices1)

vertices2 = [(1, 1), (4, 1), (4, 4), (1, 4)]
plot_polygon(vertices2)

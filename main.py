import math
import matplotlib.pyplot as plt

def rotate_point(point, angle_degrees, origin=(0, 0)):
    ox, oy = origin
    px, py = point
    angle_radians = math.radians(angle_degrees)
    qx = ox + math.cos(angle_radians) * (px - ox) - math.sin(angle_radians) * (py - oy)
    qy = oy + math.sin(angle_radians) * (px - ox) + math.cos(angle_radians) * (py - oy)
    return (qx, qy)

def rotate_triangle(triangle, angle_degrees):
    rotated = []
    for point in triangle:
        rotated_point = rotate_point(point, angle_degrees)
        rotated.append(rotated_point)
    return rotated

def plot_triangles(original, rotated):
    x_orig = [p[0] for p in original] + [original[0][0]]
    y_orig = [p[1] for p in original] + [original[0][1]]
    x_rot = [p[0] for p in rotated] + [rotated[0][0]]
    y_rot = [p[1] for p in rotated] + [rotated[0][1]]

    plt.figure()
    plt.plot(x_orig, y_orig, 'bo-', label="Original Triangle")
    plt.plot(x_rot, y_rot, 'ro-', label="Rotated Triangle")
    plt.legend()
    plt.axis('equal')
    plt.title("Triangle Rotation by 90 Degrees")
    plt.show()

triangle = [(1, 1), (4, 1), (2.5, 4)]
rotated_triangle = rotate_triangle(triangle, 90)
plot_triangles(triangle, rotated_triangle)
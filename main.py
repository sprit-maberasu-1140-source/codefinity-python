import matplotlib.pyplot as plt
import numpy as np

def plot_curve_approximations():
    # Define the range for x
    x = np.linspace(0, 2 * np.pi, 1000)
    # True curves
    y_circle = np.sqrt(1 - (np.cos(x)) ** 2)
    y_ellipse = np.sqrt(1 - (0.5 * np.cos(x)) ** 2)
    # Polygonal approximations
    num_segments = 12
    theta = np.linspace(0, 2 * np.pi, num_segments + 1)
    # Circle approximation
    circle_x = np.cos(theta)
    circle_y = np.sin(theta)
    # Ellipse approximation
    ellipse_x = np.cos(theta)
    ellipse_y = 0.5 * np.sin(theta)

    plt.figure(figsize=(10, 5))
    # Plot true circle
    plt.subplot(1, 2, 1)
    plt.plot(np.cos(x), np.sin(x), label="True Circle", color="blue")
    plt.plot(circle_x, circle_y, label="Polygonal Approx.", color="orange", marker="o")
    plt.axis("equal")
    plt.title("Circle Approximations")
    plt.legend()
    # Plot true ellipse
    plt.subplot(1, 2, 2)
    plt.plot(np.cos(x), 0.5 * np.sin(x), label="True Ellipse", color="green")
    plt.plot(ellipse_x, ellipse_y, label="Polygonal Approx.", color="red", marker="o")
    plt.axis("equal")
    plt.title("Ellipse Approximations")
    plt.legend()
    plt.tight_layout()
    plt.show()

plot_curve_approximations()
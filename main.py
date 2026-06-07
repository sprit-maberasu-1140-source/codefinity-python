import numpy as np
import matplotlib.pyplot as plt

def apply_transformations_and_plot(quadrilateral, transformations):
    # Convert quadrilateral to homogeneous coordinates
    points = np.array(quadrilateral)
    ones = np.ones((points.shape[0], 1))
    points_hom = np.hstack([points, ones])
    
    # Start with identity matrix
    combined_matrix = np.eye(3)
    
    # Apply each transformation in order
    for t in transformations:
        combined_matrix = t @ combined_matrix
    
    # Apply combined transformation
    transformed_points_hom = (combined_matrix @ points_hom.T).T
    transformed_points = transformed_points_hom[:, :2]
    
    # Plot original quadrilateral
    x_orig = np.append(points[:,0], points[0,0])
    y_orig = np.append(points[:,1], points[0,1])
    plt.plot(x_orig, y_orig, 'bo-', label='Original')
    
    # Plot transformed quadrilateral
    x_trans = np.append(transformed_points[:,0], transformed_points[0,0])
    y_trans = np.append(transformed_points[:,1], transformed_points[0,1])
    plt.plot(x_trans, y_trans, 'ro-', label='Transformed')
    
    plt.legend()
    plt.axis('equal')
    plt.title('Combined Transformations on Quadrilateral')
    plt.show()

# Example usage:
quadrilateral = [(0, 0), (2, 0), (2, 1), (0, 1)]

# Define transformation matrices
# Translation by (3, 2)
T = np.array([
    [1, 0, 3],
    [0, 1, 2],
    [0, 0, 1]
])

# Rotation by 90 degrees (pi/2 radians) around origin
theta = np.pi / 2
R = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta),  np.cos(theta), 0],
    [0, 0, 1]
])

# Scaling by 0.5 in x and 2 in y
S = np.array([
    [0.5, 0, 0],
    [0, 2, 0],
    [0, 0, 1]
])

transformations = [T, R, S]
apply_transformations_and_plot(quadrilateral, transformations)
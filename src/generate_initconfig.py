import numpy as np
import sys as sys


def main():
    scale_factor = 2
    grid_size = 100
    grid = np.zeros([grid_size, grid_size, grid_size])

    knot_name = "3_1"
    knot_curve = np.load("data/" + knot_name + "/" + knot_name + ".npy")

    bounds = find_bounds(knot_curve)
    knot_curve_transformed = transformed(knot_curve, bounds, grid_size, scale_factor)

    tube_radius = 3 # In grid coordinates
    labelled_grid = label_grid(grid, knot_curve_transformed, tube_radius)

    np.savetxt("data/" + knot_name + "/initconfig.txt", labelled_grid.flatten(), fmt="%d")



def find_bounds(curve):
    curve_tp = curve.transpose()
    
    bounds = [([curve_tp[i].min(), curve_tp[i].max()]) for i in [0,1,2]]
    return bounds

def transformed(curve, bounds, grid_size, scale_factor):
    lengths = [abs(i[0] - i[1]) for i in bounds]
    lower_bounds = np.array([i[0] for i in bounds])

    curve_transposed = curve.transpose()
    curve_rescaled = np.array([(curve_transposed[i] - lower_bounds[i]) / lengths[i] for i in [0,1,2]])

    return ((curve_rescaled.transpose() + 1/2) * grid_size) / scale_factor

def label_grid(grid, curve, tube_radius):
    for p in np.ndindex(grid.shape):
        curve_distance = calculate_distance_to_curve(curve, p)
        
        if curve_distance < tube_radius:
            grid[p] = 1

    return grid

def calculate_distance_to_curve(curve, point): #curve should be a numpy array
    distances = np.linalg.norm(curve - point, axis=1)
    return distances.min()
    


if __name__ == "__main__":
    main()
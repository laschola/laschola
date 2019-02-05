import numpy as np

def retrieve_startvoxel(center_coordinate):
    center_coordinate_numpy = np.zeros((len(center_coordinate), 3))
    center_coordinate_numpy[:] = center_coordinate
    index_z = np.where((center_coordinate_numpy[:, 2] == np.min(center_coordinate_numpy[:, 2])))
    z_min = center_coordinate_numpy[index_z]
    index_y = np.where((z_min[:, 1] == np.min(z_min[:, 1])))
    y_min = z_min[index_y]
    index_x = np.where((y_min[:, 0] == np.min(y_min[:, 0])))
    start_coordinate = y_min[index_x]

    # specify index of start_coordinate
    start_coordinate = start_coordinate.flatten()  # 2d to 1d
    index_of_start_coordinate = np.where((np.all(center_coordinate_numpy == start_coordinate, axis=1)))

    return center_coordinate_numpy,start_coordinate


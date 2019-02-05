import collections
from collections import defaultdict
import numpy as np


def get_shape_tsp(center_coordinate_numpy,start_coordinate):

    """
    This function's purpose is to get shape. That is,What shape of voxel data in input file ,for example it
    has two hole, is grasped  by using this function.

    :param center_coordinate_numpy:This var has all center coordinate as numpy
    :param start_coordinate:This var has the smallest y and z coordinate
    :return:
    """
    voxel_count = []
    each_layer_voxel_coordinate = {}
    outer_coordinate = defaultdict(list)
    inner_coordinate = {}
    average_distance_voxel = []
    center_coordinate_numpy = np.round(center_coordinate_numpy, 4)
    all_y_coordinate_in_same_layer = None

    all_z_coordinate = np.sort(list(set(center_coordinate_numpy[:, 2])))
    min_y_line = np.where(center_coordinate_numpy[:, 1] == start_coordinate[1])

    def get_average_distance_voxel(all_y_coordinate_in_same_layer):
        """
        This function's purpose is to calcurate between voxel and return average_distance_voxel.
        programmer can change max(mode.values()) to improve reliability. That is , The more increasing figure,
        the more improved reliability.

        :param all_y_coordinate_in_same_layer:Input y direction or z direction coordinate
        :return:
        """
        distance_list = []
        for i in range(len(all_y_coordinate_in_same_layer) - 1):
            distance_next_to_voxel = all_y_coordinate_in_same_layer[i+1] - all_y_coordinate_in_same_layer[i]
            distance_list.append(round(distance_next_to_voxel, 2))

            if i > 9 :
                mode = collections.Counter(distance_list)
                if max(mode.values()) > 5:
                    return average_distance_voxel.append(max(mode, key=mode.get))


    for same_layer_index, z_coordinate in enumerate(all_z_coordinate):
        same_layer = np.where(z_coordinate == center_coordinate_numpy[:,2])
        each_layer_voxel_coordinate['layer{}'.format(same_layer_index + 1)] = center_coordinate_numpy[same_layer]
        all_x_coordinate_in_same_layer = np.sort(list(set(center_coordinate_numpy[same_layer[0],0])))
        all_y_coordinate_in_same_layer = np.sort(list(set(center_coordinate_numpy[same_layer[0],1])))
        if same_layer_index == 0:
            if len(all_y_coordinate_in_same_layer) > 9:#there are voxels more than 10 in y direction
                get_average_distance_voxel(all_y_coordinate_in_same_layer)
            else:#If there are NOT voxels more than 10 in y direction, use z direction
                get_average_distance_voxel(z_coordinate)
        for same_line_index, y_coordinate in enumerate(all_y_coordinate_in_same_layer):
            all_line_coordinate = np.where(center_coordinate_numpy[same_layer[0], 1] == y_coordinate)
            retrieve_coordinate = center_coordinate_numpy[same_layer[0][all_line_coordinate[0]]]
            if same_line_index == 0 or same_line_index == (len(all_y_coordinate_in_same_layer) - 1):
                for i in range(len(retrieve_coordinate)):
                    outer_coordinate['layer{}'.format(same_layer_index + 1)].append(retrieve_coordinate[i])
            else:
                outer_coordinate['layer{}'.format(same_layer_index + 1)].append(retrieve_coordinate[0])
                outer_coordinate['layer{}'.format(same_layer_index + 1)].append(retrieve_coordinate[-1])
            for x_index in range(len(retrieve_coordinate) - 1):
                if same_line_index == 0:
                    continue
                elif same_line_index == (len(all_y_coordinate_in_same_layer) - 1):
                    continue




                distance_next_to_voxel = retrieve_coordinate[x_index + 1][0] - retrieve_coordinate[x_index][0]
                if round(distance_next_to_voxel, 2) != average_distance_voxel:
                    if retrieve_coordinate[x_index] is not outer_coordinate.values():
                        outer_coordinate['layer{}'.format(same_layer_index + 1)].append(retrieve_coordinate[x_index])
                        outer_coordinate['layer{}'.format(same_layer_index + 1)].append(retrieve_coordinate[x_index+1])




        for same_row_index, x_coordinate in enumerate(all_x_coordinate_in_same_layer):
            all_row_coordinate = np.where(center_coordinate_numpy[same_layer[0], 0] == x_coordinate)
            retrieve_coordinate = center_coordinate_numpy[same_layer[0][all_row_coordinate[0]]]
            unique_count = 0
            for y_index in range(len(retrieve_coordinate) - 1):
                distance_next_to_voxel = retrieve_coordinate[y_index + 1][1] - retrieve_coordinate[y_index][1]
                if round(distance_next_to_voxel, 2) != average_distance_voxel:
                    if retrieve_coordinate[y_index] is not outer_coordinate.values():
                        unique_count += 1
                        outer_coordinate['layer{}'.format(same_layer_index + 1)].append(retrieve_coordinate[y_index])
                    if retrieve_coordinate[y_index + 1] is not outer_coordinate.values():
                        unique_count += 1
                        outer_coordinate['layer{}'.format(same_layer_index + 1)].append(retrieve_coordinate[y_index + 1])

            voxel_count.append(len(retrieve_coordinate))



    return each_layer_voxel_coordinate, outer_coordinate, average_distance_voxel





def get_shape(center_coordinate_numpy,start_coordinate):
    """
    This function's purpose is to get shape. That is,What shape of voxel data in input file ,for example it
    has two hole, is grasped  by using this function.

    :param center_coordinate_numpy:This var has all center coordinate as numpy
    :param start_coordinate:This var has the smallest y and z coordinate
    :return:
    """
    voxel_count = []
    each_layer_voxel_coordinate = {}
    outer_coordinate = defaultdict(list)
    inner_coordinate = defaultdict(list)
    average_distance_voxel = []
    center_coordinate_numpy = np.round(center_coordinate_numpy, 4)
    all_y_coordinate_in_same_layer = None


    all_z_coordinate = np.sort(list(set(center_coordinate_numpy[:, 2])))
    min_y_line = np.where(center_coordinate_numpy[:, 1] == start_coordinate[1])

    def get_average_distance_voxel(all_y_coordinate_in_same_layer):
        """
        This function's purpose is to calcurate between voxel and return average_distance_voxel.
        programmer can change max(mode.values()) to improve reliability. That is , The more increasing figure,
        the more improved reliability.

        :param all_y_coordinate_in_same_layer:Input y direction or z direction coordinate
        :return:
        """
        distance_list = []
        for i in range(len(all_y_coordinate_in_same_layer) - 1):
            distance_next_to_voxel = all_y_coordinate_in_same_layer[i+1] - all_y_coordinate_in_same_layer[i]
            distance_list.append(round(distance_next_to_voxel, 2))

            if i > 9 :
                mode = collections.Counter(distance_list)
                if max(mode.values()) > 5:
                    return average_distance_voxel.append(max(mode, key=mode.get))


    for same_layer_index, z_coordinate in enumerate(all_z_coordinate):
        same_layer = np.where(z_coordinate == center_coordinate_numpy[:,2])
        each_layer_voxel_coordinate['layer{}'.format(same_layer_index + 1)] = center_coordinate_numpy[same_layer]
        all_x_coordinate_in_same_layer = np.sort(list(set(center_coordinate_numpy[same_layer[0],0])))
        all_y_coordinate_in_same_layer = np.sort(list(set(center_coordinate_numpy[same_layer[0],1])))
        if same_layer_index == 0:
            if len(all_y_coordinate_in_same_layer) > 9:#there are voxels more than 10 in y direction
                get_average_distance_voxel(all_y_coordinate_in_same_layer)
            else:#If there are NOT voxels more than 10 in y direction, use z direction
                get_average_distance_voxel(z_coordinate)
        for same_line_index, y_coordinate in enumerate(all_y_coordinate_in_same_layer):
            all_line_coordinate = np.where(center_coordinate_numpy[same_layer[0], 1] == y_coordinate)
            retrieve_coordinate = center_coordinate_numpy[same_layer[0][all_line_coordinate[0]]]
            #if same_line_index == 0 or same_line_index == (len(all_y_coordinate_in_same_layer) - 1):
            #    for i in range(len(retrieve_coordinate)):
            #        outer_coordinate['layer{}'.format(same_layer_index + 1)].append(retrieve_coordinate[i])
            #else:
            outer_coordinate['layer{}'.format(same_layer_index + 1)].append(retrieve_coordinate[0])
            outer_coordinate['layer{}'.format(same_layer_index + 1)].append(retrieve_coordinate[-1])
            for x_index in range(len(retrieve_coordinate) - 1):
                if same_line_index == 0:
                    continue
                elif same_line_index == (len(all_y_coordinate_in_same_layer) - 1):
                    continue

                #if x_index % 3 == 0:
                 #   outer_coordinate['layer{}'.format(same_layer_index + 1)].append(retrieve_coordinate[x_index])
                #if x_index == round(len(retrieve_coordinate) * .25) :
                 #   inner_coordinate['layer{}'.format(same_layer_index + 1)].append(retrieve_coordinate[x_index])
                #elif x_index == round(len(retrieve_coordinate) * .75):
                 #   inner_coordinate['layer{}'.format(same_layer_index + 1)].append(retrieve_coordinate[x_index])
                #elif x_index == len(retrieve_coordinate)/2:
                    #outer_coordinate['layer{}'.format(same_layer_index + 1)].append(retrieve_coordinate[(len(retrieve_coordinate))/2])

                distance_next_to_voxel = retrieve_coordinate[x_index + 1][0] - retrieve_coordinate[x_index][0]
                if round(distance_next_to_voxel, 2) != average_distance_voxel:
                    if retrieve_coordinate[x_index] is not outer_coordinate.values():
                        inner_coordinate['layer{}'.format(same_layer_index + 1)].append(retrieve_coordinate[x_index])
                        inner_coordinate['layer{}'.format(same_layer_index + 1)].append(retrieve_coordinate[x_index+1])


        for same_row_index, x_coordinate in enumerate(all_x_coordinate_in_same_layer):
            all_row_coordinate = np.where(center_coordinate_numpy[same_layer[0], 0] == x_coordinate)
            retrieve_coordinate = center_coordinate_numpy[same_layer[0][all_row_coordinate[0]]]
            unique_count = 0
            for y_index in range(len(retrieve_coordinate) - 1):
                distance_next_to_voxel = retrieve_coordinate[y_index + 1][1] - retrieve_coordinate[y_index][1]
                if round(distance_next_to_voxel, 2) != average_distance_voxel:
                    if retrieve_coordinate[y_index] is not outer_coordinate.values():
                        unique_count += 1
                        inner_coordinate['layer{}'.format(same_layer_index + 1)].append(retrieve_coordinate[y_index])
                    if retrieve_coordinate[y_index + 1] is not outer_coordinate.values():
                        unique_count += 1
                        inner_coordinate['layer{}'.format(same_layer_index + 1)].append(retrieve_coordinate[y_index + 1])

                    voxel_count.append(len(retrieve_coordinate))



        """

        def determination_inside_and_outside(searching_outer_voxel):
            start_voxel = searching_outer_voxel[:][0]
            print(searching_outer_voxel)
            print(start_voxel[0] + average_distance_voxel)
            for i,v in enumerate(searching_outer_voxel):
                print(searching_outer_voxel)
                print(start_voxel[0] + average_distance_voxel)

        determination_inside_and_outside(outer_coordinate['layer{}'.format(same_layer_index + 1)])
         """


    return  each_layer_voxel_coordinate, outer_coordinate, inner_coordinate,all_y_coordinate_in_same_layer,average_distance_voxel

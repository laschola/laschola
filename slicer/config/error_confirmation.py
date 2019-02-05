from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

from slicer.models import get_shape
from slicer.models import InputFile
from slicer.models import retrieve_startvoxel



def main():
    """
    This function is main. This program is done following sequence
    1.load obj file
    2.Retrieve start position
    3.Getting a shape
    4.Cosen path by User in cmd
    5.Calcuration printpath and gcode


    This version can load only obj file.

    :return:
    """

    from tsp.greedy import greedy
    from tsp.twoopt import TSP2opt
    from tsp.twoopt.TSP2opt import Node

    def visualization(outer_coordinate,inner_coordinate,visited_node):
        data_x = []
        data_y = []
        x = []
        y = []

        outer_coordinate = list(outer_coordinate.values())
        inner_coordinate = list(inner_coordinate.values())

        for i in range(len(outer_coordinate[0])):
            data_x.append(outer_coordinate[0][i][0])
            data_y.append(outer_coordinate[0][i][1])
        for i in range(len(inner_coordinate[0])):
            data_x.append(inner_coordinate[0][i][0])
            data_y.append(inner_coordinate[0][i][1])

        for i, v in enumerate(visited_node):
            x.append(v[0])
            y.append(v[1])

        # Figure内にAxesを追加()
        fig = plt.figure(figsize=(12, 8))  # ...1

        # Figure内にAxesを追加()
        ax = fig.add_subplot(111)  # ...2
        ax.plot(data_x, data_y, '.', label="test")  # ...3
        ax.plot(x, y, color='red', linestyle='solid')
        plt.show()


    def toturple(coordinate):
        data = []
        for i in range(len(coordinate['layer1'])):
            data.append((coordinate['layer1'][i][0],coordinate['layer1'][i][1],coordinate['layer1'][i][2]))
        return data

    def get_y_of_inner_coordinate(inner_coordinate):
        y_of_inner_coords = []
        for i, v in enumerate(inner_coordinate['layer1']):
            y_of_inner_coords.append(v[1])
        y_of_inner_coords = list(set(y_of_inner_coords))
        return y_of_inner_coords




    def tsp(current_node,y_of_inner_coords,remaining_outer_nodes,remaining_inner_nodes):
        def preparation_for_tsp(next_y_index,current_y_index):
            if (next_y_index - current_y_index)%2 == 0:
                goal_node = [node for node in remaining_outer_nodes if
                     (node[0] == current_node[0]) and (node[1] == y_of_inner_coords[next_y_index] + average_distance_voxel)]
            else:
                goal_node = [node for node in remaining_outer_nodes if
                             (node[0] != current_node[0]) and (node[1] == y_of_inner_coords[next_y_index]+average_distance_voxel)]


            count = 0
            data = []
            data.append((count, current_node[0], current_node[1]))
            count += 1
            for node in remaining_outer_nodes:
                if current_node[1] <= node[1] <= y_of_inner_coords[next_y_index]:
                    data.append((count, node[0], node[1]))
                    count += 1
            for node in remaining_inner_nodes:
                if current_node[1] <= node[1] <= y_of_inner_coords[next_y_index]:
                    data.append((count, node[0], node[1]))
                    count += 1


            data.append((count, goal_node[0][0],goal_node[0][1]))
            start_node = []
            start_node.append(data[-1])
            start_node.append(data[0])

            return data,start_node


        current_y_index = y_of_inner_coords.index(current_node[1])
        next_y_index = None
        for i,v in enumerate(y_of_inner_coords[current_y_index:]):
            if v == y_of_inner_coords[-1]:
                next_y_index = i + current_y_index
                break
            elif round((y_of_inner_coords[i+1+current_y_index] - v),4) != average_distance_voxel[0]:
                next_y_index = i + current_y_index
                break

        data,start_node = preparation_for_tsp(next_y_index,current_y_index)

        #TSP,greedy 2-opt
        nodes, distance = greedy.solveGreedyTSP(data, start_node)
        route = []
        for k in range(len(nodes)):
            route.append(Node(nodes[k]))
        route = TSP2opt.run_2opt(route)


        return route,start_node,next_y_index


    def whether_available_for_x(current_node,remaining_outer_nodes,remaining_inner_nodes,y_of_inner_coords):
        if current_node[1] in y_of_inner_coords:
            route,start_node,next_y_index = tsp(current_node,y_of_inner_coords,remaining_outer_nodes,remaining_inner_nodes)

            return route,start_node,next_y_index

        else:
            y_same_outer_node = [node for node in remaining_outer_nodes if node[1] == current_node[1]]
            if len(y_same_outer_node) == 1:
                return y_same_outer_node[0]
            elif len(y_same_outer_node) == 0:
                x_same_outer_node = [node for node in remaining_outer_nodes
                                     if (node[0] == current_node[0]) and (current_node[1] - 0.8<= node[1] <= current_node[1] + 0.8)]
                if len(x_same_outer_node) == 1:
                    return x_same_outer_node[0]
                elif len(x_same_outer_node) == 0:
                    return current_node
            else:
                raise ValueError





    input_file = InputFile()
    all_coordinate,start_position = retrieve_startvoxel(input_file.load_obj())
    each_layer_voxel_coordinate, outer_coordinate, inner_coordinate, all_y_coordinate_in_same_layer,average_distance_voxel \
        = get_shape(all_coordinate, start_position)


    remaining_outer_nodes = toturple(outer_coordinate)
    remaining_inner_nodes = toturple(inner_coordinate)
    start_position = tuple(np.round(start_position,4))
    y_of_inner_coords = sorted(get_y_of_inner_coordinate(inner_coordinate))



    dicision = True
    visited_node = []
    visited_node.append(start_position)
    remaining_outer_nodes.remove(visited_node[-1])
    while dicision:
        dicision = False
        next_node = whether_available_for_x(visited_node[-1],remaining_outer_nodes,remaining_inner_nodes,y_of_inner_coords)
        if next_node == visited_node[-1]:
            break
        else:
            visited_node.append(next_node)
            remaining_outer_nodes.remove(visited_node[-1])
            dicision = True

    visualization(outer_coordinate,inner_coordinate,visited_node)


def test_tsp():
    """
    This function is main. This program is done following sequence
    1.load obj file
    2.Retrieve start position
    3.Getting a shape
    4.Cosen path by User in cmd
    5.Calcuration printpath and gcode


    This version can load only obj file.

    :return:
    """
    input_file = InputFile()
    start_position = retrieve_startvoxel(input_file.load_obj())
    each_layer_voxel_coordinate, outer_coordinate, inner_coordinate, all_y_coordinate_in_same_layer,average_distance_voxel = get_shape(start_position[0],start_position[1])

    regional_division = defaultdict(list)


    #for i, v in enumerate(each_layer_voxel_coordinate['layer1'][:]):
     #   if (-14.15 <= v[1] <= 14.55) and (v[0] == 32.25 or v[0] == -31.45) :
      #      regional_division['division_test'].append(v)



    for i, v in enumerate(outer_coordinate['layer1'][:]):
        if   v[1] == all_y_coordinate_in_same_layer[0]  and (v[0] == 49.75 or v[0] == -49.65) :
            regional_division['division_test'].append(v)
        elif v[1] in all_y_coordinate_in_same_layer[1:10]:
            regional_division['division_test'].append(v)
        elif v[1] == all_y_coordinate_in_same_layer[11] and v[0] == 49.75:
            regional_division['division_test'].append(v)

    for i, v in enumerate(inner_coordinate['layer1'][:]):
        if   v[1] <= -15  :
            regional_division['division_test'].append(v)

    print(regional_division['division_test'])

    data = []

    """


    for i in range(len(outer_coordinate['layer1'])):
        data.append((i,outer_coordinate['layer1'][i][0],outer_coordinate['layer1'][i][1]))

    for i in range(len(inner_coordinate['layer1'])):
        data.append((i, inner_coordinate['layer1'][i][0], inner_coordinate['layer1'][i][1]))
    """

    for i in range(len(regional_division['division_test'])):
        data.append((i,regional_division['division_test'][i][0],regional_division['division_test'][i][1]))



    from tsp.greedy import greedy
    from tsp.twoopt import TSP2opt
    from tsp.twoopt.TSP2opt import Node

    from timeit import default_timer


    def column(matrix, i):
        return [row[i] for row in matrix]

    data_x = column(data, 1)
    data_y = column(data, 2)

    print('スタート')
    start = default_timer()
    start_node = []
    start_node.append(data[-1])
    start_node.append(data[0])

    nodes, distance = greedy.solveGreedyTSP(data,start_node)

    route = []
    for k in range(len(nodes)):
        route.append(Node(nodes[k]))

    # start time of running 2opt
    route = TSP2opt.run_2opt(route)

    end = default_timer() # end time of running 2opt


    time = round((end - start), 2)
    print(time)
    print('終了')

    x = []
    y = []


    """
    for i , v in enumerate(get_shape(start_position[0],start_position[1])[1].values()):


        if i == 0:
            for count in range(len(v[:, 0])):
                x.append(v[count, 0])
                y.append(v[count, 1])

        elif  i == (len(get_shape(start_position[0],start_position[1])[1].values()) -1):
            for count in range(len(v[:, 0])):
                x.append(v[count, 0])
                y.append(v[count, 1])

        else:
            x.append(v[:][0])
            y.append(v[:][1])
    """

    """

        for i, v in enumerate(nodes):
            x.append(v[1])
            y.append(v[2])
    """



    for i in range(len(route)):
        x.append(route[i].x)
        y.append(route[i].y)



    # Figure内にAxesを追加()

    fig = plt.figure(figsize=(12, 8))  # ...1

    # Figure内にAxesを追加()
    ax = fig.add_subplot(111)  # ...2
    ax.plot(data_x, data_y, '.', label="test")  # ...3
    ax.plot(x,y,color='red',  linestyle='solid')
    plt.show()

def plot_getting_voxel():
    input_file = InputFile()
    start_position = retrieve_startvoxel(input_file.load_obj())
    each_layer_voxel_coordinate, outer_coordinate, inner_coordinate, all_y_coordinate_in_same_layer,abc = get_shape(
        start_position[0], start_position[1])


    data_x = []
    data_y = []
    outer_coordinate = list(outer_coordinate.values())
    inner_coordinate = list(inner_coordinate.values())



    for i in range(len(outer_coordinate[0])):
        data_x.append(outer_coordinate[0][i][0])
        data_y.append(outer_coordinate[0][i][1])

    x = []
    y = []

    for i in range(len(inner_coordinate[0])):
        x.append(inner_coordinate[0][i][0])
        y.append(inner_coordinate[0][i][1])





    fig = plt.figure(figsize=(12, 8))  # ...1

    # Figure内にAxesを追加()
    ax = fig.add_subplot(111)  # ...2
    ax.plot(data_x, data_y, '.', color='blue', label="test")  # ...3
    ax.plot(x, y,'.', color='red' )
    plt.show()

def reserch_time_and_coordinate():

    import openpyxl as px

    from tsp.greedy import greedy
    from tsp.twoopt import TSP2opt
    from tsp.twoopt.TSP2opt import Node

    from timeit import default_timer


    book = px.load_workbook('C:/Users/admin/Desktop/TSP.xlsx')
    sheet = book.active

    for i in range(2):
        print(i)
        print('スタート')
        name = "B" + str(i + 15)
        file = sheet[name].value
        data = greedy.parseFile(file)

        def column(matrix, i):
            return [row[i] for row in matrix]

        data_x = column(data, 1)
        data_y = column(data, 2)

        start = default_timer()
        nodes, distance = greedy.solveGreedyTSP(data)

        route = []
        for k in range(len(nodes)):
            route.append(Node(nodes[k]))

        # start time of running 2opt
        route = TSP2opt.run_2opt(route)
        end = default_timer() # end time of running 2opt


        time_cell = "D" + str(i + 15)
        time = round((end - start),2)
        dimention_cell = "C" + str(i + 15)
        dimention = str(len(route))
        sheet[dimention_cell] = dimention
        sheet[time_cell] = time
        print(time)
        print('終了')


        '''

        database = []
        for node in route:
            database.append(vars(node))

        print(-1)

        print("Dimension : " + str(len(route)))

        print("Total Distance : " + str(TSP2opt.route_distance(route)))
        print("Time to run 2opt : %.2f seconds" % (end - start))
        '''


    book.save('C:/Users/admin/Desktop/TSP.xlsx')

    '''


    x = []
    y = []

    """
    for i , v in enumerate(get_shape(start_position[0],start_position[1])[1].values()):


        if i == 0:
            for count in range(len(v[:, 0])):
                x.append(v[count, 0])
                y.append(v[count, 1])

        elif  i == (len(get_shape(start_position[0],start_position[1])[1].values()) -1):
            for count in range(len(v[:, 0])):
                x.append(v[count, 0])
                y.append(v[count, 1])

        else:
            x.append(v[:][0])
            y.append(v[:][1])
        """




    for i in range(len(route)):
        x.append(route[i].x)
        y.append(route[i].y)



    # Figure内にAxesを追加()

    fig = plt.figure(figsize=(12, 8))  # ...1

    # Figure内にAxesを追加()
    ax = fig.add_subplot(111)  # ...2
    ax.plot(data_x, data_y, 'o', label="test")  # ...3
    ax.plot(x, y, color='red', linestyle='solid')
    plt.show()




    x = []
    y = []
    for i in database:
        x.append(i['x'])
        y.append(i['y'])




    #x = column(nodes,1)
    #y = column(nodes,2)




    # Figure内にAxesを追加()

    fig = plt.figure(figsize=(12, 8))  # ...1

    # Figure内にAxesを追加()
    ax = fig.add_subplot(111)  # ...2
    ax.plot(data_x, data_y, 'o', label="test")  # ...3
    ax.plot(x,y,color='red',  linestyle='solid')
    plt.show()
    '''

if __name__ == '__main__':
    test_tsp()
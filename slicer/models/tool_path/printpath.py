import matplotlib.pyplot as plt



class PrintPath(object):

    def __init__(self,outer_coordinate,inner_coordinate,start_position,average_distance_voxel):
        self.visited_node = []
        self.remaining_outer_nodes = self.toturple(outer_coordinate)
        self.remaining_inner_nodes = self.toturple(inner_coordinate)
        self.start_position = start_position
        self.y_of_inner_coords = sorted(self.get_y_of_inner_coordinate(inner_coordinate))
        self.average_distance_voxel = average_distance_voxel
        self.current_node = None


    def toturple(self,coordinate):
        data = []
        for i in range(len(coordinate['layer1'])):
            data.append((coordinate['layer1'][i][0],coordinate['layer1'][i][1],coordinate['layer1'][i][2]))
        return data

    def get_y_of_inner_coordinate(self,inner_coordinate):
        y_of_inner_coords = []
        for i, v in enumerate(inner_coordinate['layer1']):
            y_of_inner_coords.append(v[1])
        y_of_inner_coords = list(set(y_of_inner_coords))
        return y_of_inner_coords





    def whether_available_for_x(self):
        if self.current_node[1] in self.y_of_inner_coords:
            start_node = self.tsp()
            return start_node

        else:
            y_same_outer_node = [node for node in self.remaining_outer_nodes if node[1] == self.current_node[1]]
            if len(y_same_outer_node) == 1:
                return y_same_outer_node[0]
            elif len(y_same_outer_node) == 0:
                #0.01 cope with Rounding error
                x_same_outer_node = [node for node in self.remaining_outer_nodes
                                     if (node[0] == self.current_node[0]) and
                                     (self.current_node[1] - self.average_distance_voxel-0.01 <= node[1] <= self.current_node[1] + self.average_distance_voxel+0.01)]
                if len(x_same_outer_node) == 1:
                    return x_same_outer_node[0]
                elif len(x_same_outer_node) == 0:
                    return self.current_node
                else:
                    raise ValueError
            else:
                raise ValueError

    def searching_for_printpath(self):
        dicision = True
        self.visited_node.append(self.start_position)
        self.remaining_outer_nodes.remove(self.visited_node[-1])
        while dicision:
            dicision = False
            self.current_node = self.visited_node[-1]
            next_node = self.whether_available_for_x()
            if next_node == self.visited_node[-1]:
                if len(self.remaining_outer_nodes) == 0 and len(self.remaining_inner_nodes) == 0:
                    break
                else:
                    self.visited_node.append(self.remaining_outer_nodes[0])
                    self.remaining_outer_nodes.remove(self.visited_node[-1])
                    dicision = True
            else:
                self.visited_node.append(next_node)
                self.remaining_outer_nodes.remove(self.visited_node[-1])
                dicision = True

        return self.visited_node

def visualization(outer_coordinate, inner_coordinate, visited_node):
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
    ax.plot(x, y, color='black', linestyle='solid')
    plt.axes().set_aspect('equal', 'datalim')
    plt.show()
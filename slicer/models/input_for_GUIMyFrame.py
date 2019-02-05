import os

import numpy as np



class InputFile(object):
    def __init__(self):
        self.data_list = []


#deleted duplicate coordinate
    def deleted_duplication(self,seq):
        seen = []
        [x for x in seq if x not in seen and not seen.append(x)]
        self.data_list = seen

#import obj file
    def load_obj(self,name):
        with open (os.path.join(name),"r", encoding='utf-8') as obj_file:
            for line in obj_file:
                vals = line.split()
                if len(vals) == 0:
                    continue
                if vals[0] == "v":
                    v = list(map(float, vals[1:4]))
                    self.data_list.append(v)

        if self.data_list[0:3].count(self.data_list[0]) == 3:
            self.deleted_duplication(self.data_list)


        #Receive data and slicing each 8 element and making list
        each_coordinate = [self.data_list[i : i + 8] for i in range(0, len(self.data_list), 8)]
        data_arr = np.zeros((len(self.data_list)//8,8,3))
        data_arr[:] = each_coordinate

        #Get each center coordinate of voxel and do a two-dimensional array
        center_coordinate = []
        for i in range(0,len(data_arr[:,0,0])):
            for j in range(0, 3):
                calculation = (np.max(data_arr[i,:,j]) + np.min(data_arr[i,:,j]))/2
                center_coordinate.append(calculation)
        center_coordinate = [center_coordinate[i : i + 3] for i in range(0, len(center_coordinate), 3)]

        return center_coordinate


if __name__ == "__main__":
    pass


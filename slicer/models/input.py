import os

import numpy as np

from slicer.views.GUI2 import FindFile


input_gui = FindFile()


class InputFile(object):
    def __init__(self):
        self.data_list = []

    def modification_of_obj_file_in_console(self):
        """
        This function is to choose yes or no that user inputed obj file has whether duplicated coordinate.
        but It isn't used this program after 2018/11/12.

        :return:
        """
        while True:
            print('Are there duplicated coordinate in obj file?[y/n]')
            whether_there_are_duplicated_coordinate = input('Input y or n:')
            if whether_there_are_duplicated_coordinate == 'y':
                return self.deleted_duplication(self.data_list)
            elif whether_there_are_duplicated_coordinate == 'n':
                return self.data_list
            else:
                print('Answer y or n．Choose again!．')


#deleted duplicate coordinate
    def deleted_duplication(self,seq):
        seen = []
        [x for x in seq if x not in seen and not seen.append(x)]
        self.data_list = seen

#import obj file
    def load_obj(self):
        with open (os.path.join(input_gui.getfilename()),"r", encoding='utf-8') as obj_file:
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

    input_file = InputFile()
    print(input_file.load_obj())
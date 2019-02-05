import numpy as np
from slicer.models.getshape import get_shape
from slicer.models.input import InputFile
from slicer.models.serchforstartvoxel import retrieve_startvoxel
from slicer.models.tool_path.printpath import PrintPath
from slicer import models as pp

"""
#GUI
def main():
    app = wx.App(False)
    frame = GUIMyFrame1(None)
    frame.Show(True)
    app.MainLoop()

"""



def main():
    input_file = InputFile()
    all_coordinate, start_position = retrieve_startvoxel(input_file.load_obj())
    each_layer_voxel_coordinate, outer_coordinate, inner_coordinate, all_y_coordinate_in_same_layer, average_distance_voxel \
        = get_shape(all_coordinate, start_position)

    printpath = PrintPath(outer_coordinate, inner_coordinate,tuple(np.round(start_position, 4)),average_distance_voxel)
    visited_node = printpath.searching_for_printpath()

    pp.visualization(outer_coordinate,inner_coordinate,visited_node)


def main_GUIframe():
    import wx
    from slicer.views.GUIMyFrame1 import GUIMyFrame1

    app = wx.App(False)
    frame = GUIMyFrame1(None)
    frame.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    main_GUIframe()
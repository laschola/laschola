from mecode import G
from slicer.models.tool_path.Gcode import gcode



def generate_gcode(file,
                   node,
                   filament_diameter,
                   nozzle_diameter,
                   nozzle_temperature,
                   bet_temperature,
                   print_spped,
                   surround_outer_frame,
                   surround_inner_frame):
    """
     This function's purpose is to generate gcode.

    :param gui:Recive path in GUI
    :return:
    """


    g = gcode(outfile=file)

    g.bet_temperature(bet_temperature)
    g.nozzle_temperature(nozzle_temperature)
    g.set_temperature(nozzle_temperature)
    g.millimeters()
    g.home()
    g.base_print_speed(print_spped)
    g.absolute()

    for i in node:
        g.abs_move(x=i[0],y=i[1],z=i[2])


if __name__ == "__main__":

    g = G()
    g.home()
    g.move(10,10,10)
    g.move(10, 20, 10)
    g.move(0, 20, 10)
    g.move(00, 10, 10)
    g.view()


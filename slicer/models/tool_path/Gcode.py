from mecode import G

class gcode(G):


    def filament_diameter(self,text):
        pass


    def nozzle_diameter(self):
        pass

    def nozzle_temperature(self,text):
        command = "M104 S{} ; set temperature".format(text)
        super().write(command)

    def bet_temperature(self,text):
        command = "M190 S{} ; set bed temperature and wait for it to be reached".format(text)
        super().write(command)

    def set_temperature(self,text):
        command = "M109 S{} ;set temperature and wait for it to be reached" .format(text)
        super().write(command)

    def base_print_speed(self,text):
        command = "F{} ; set base print speed".format(text)
        super().write(command)

    def fan_on(self):
        command = "M106 ;Fan On"
        super().write(command)

    def millimeters(self):
        command = "G21 ;set units to millimeters"
        super().write(command)




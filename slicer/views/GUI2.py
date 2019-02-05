import wx

class FindFile(object):
    def getfilename(self):
        app = wx.App()
        dialog = wx.FileDialog(None, u'ファイルを選択してください',wildcard="obj file(*.obj) | *.obj" )
        dialog.ShowModal()
        self.name = dialog.GetPath()
        return self.name

    def savefile(self):
        app = wx.App()
        dialog = wx.FileDialog(None, u'名前を付けて保存',wildcard="gcode file(*.gcode) | *.gocde" ,style=wx.FD_SAVE)
        dialog.ShowModal()
        self.name = dialog.GetPath()
        return self.name

def printpath_setting():
    """
    User can choose to make a printpath

    :return:
    """
    while True:
        print('You can choose whether to surround outer or not')
        print('Surround:y')
        print('Not surround:n')
        whether_surround_outer = input('Input y or n:')
        if whether_surround_outer == 'y':
            while True:
                print('How many times does it surround?')
                repeat_number = int(input('How many times? But you have to choose no less than 3 :'))
                if repeat_number > 3:
                    print('Choose again!')
                else:
                    break
            break
        elif whether_surround_outer == 'n':
            break
        else:
            print('Choose again!')



if __name__ == "__main__":

    f = FindFile()
    f_ = f.savefile()

    print(f_ )

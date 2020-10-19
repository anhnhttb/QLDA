from tkinter_source_file import *
######
class Window(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master = master

# this is needed to make the 'window' to operate
#####


######
window_root = Tk()
application = Window(window_root)
window_root.mainloop()
# This is needed to start the process to see the 'window'
######
from tkinter_source_file import *

class Window(Frame):

    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    # init_window creation
    def init_window(self):
        # Title Customiz for the master widget
        self.master.title('GUI Tutorial')
        # Widget will take the full space avial of the root's window
        self.pack(fill=BOTH, expand=1)

        # This will create a button instance for the user to see/interact
        quitButton = Button(self,text='Quit')

        # the button location -> in relative to the max size of the window
        quitButton.place(x=450,y=370)


root = Tk()

# the max size of the window
root.geometry('500x400')
application = Window(root)
root.mainloop()

from tkinter_source_file import *


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title('Gui Menu')
        self.pack(fill=BOTH, expand=1)

        def client_exit(self):
            exit()
        # Now creating a menu
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file menu
        file = Menu(menu)
        # create example menu
        examp = Menu(menu)

        # This will show what subjects will be on the 'File' Category once
        # a user has clicked 'File' they will see the exit button

        file.add_command(label='Exit', command=self.client_exit)

        # Once a user has clicked 'Examp' they will see the open button, for now it will just close the
        # program
        examp.add_command(label='Open', command=self.client_open)

        # creates the instance of 'File' which will hold the exit information
        menu.add_cascade(label='File', menu=file)

        # creates the instance of 'examp' which will close the program for the time being
        menu.add_cascade(label='Examp', menu=examp)

        # creating the file obj
        edit = Menu(menu)
        # Add Categories in which will be shown for options, such as File, Edit, etc
        # on top of the window
        edit.add_command(label='Undo')
        menu.add_cascade(label='Edit', menu=edit)
        menu.add_cascade(label='Now', menu=examp)


#### Disabled  4 The Time Being ####
#    def client_exit(self):
#        exit()
#### Disabled 4 The Time Being ####

root = Tk()
root.geometry('500x400')

application = Window(root)

root.mainloop()

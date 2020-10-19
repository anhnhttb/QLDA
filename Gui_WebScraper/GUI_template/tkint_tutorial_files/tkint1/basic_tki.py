from tkinter_source_file import *


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title('Gui Job Program')
        self.pack(fill=BOTH, expand=1)


        # Menu Data
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file menu
        file = Menu(menu)
        # create export function menu
        export_info = Menu(menu)

        # Menu for top of GUI Screen
        edit = Menu(menu)
        # Categories for the menu screen
        menu.add_cascade(label='File', menu=file)
        menu.add_cascade(label='Edit', menu=edit)
        menu.add_cascade(label='Export', menu=export_info)

        # Commands for the menu screen
        # Undo Last Action
        edit.add_command(label='Undo')
        # Exit Program
        file.add_command(label='Exit', command=self.client_exit)
        # Export Info
        export_info.add_command(label='Export', command=self.client_open)



    # Functions relating to Menu operations
    def client_exit(self):
        exit()

    def client_open(self):
        exit()


#### Disabled  4 The Time Being ####
#    def client_exit(self):
#        exit()
#### Disabled 4 The Time Being ####

window = Tk()
window.geometry('500x400')
application = Window(window)
window.mainloop()

from tkinter_source_file import *

class Window(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        # gets a refrence 2 the master widget aka tk window
        self.master = master
        #######
        self.init_window()

    def init_window(self):

        self.master.title('Gui Quit Functionality')
        self.pack(fill=BOTH, expand=1)

        # making the button instance
        quitButton = Button(self,text='Quit',command=self.client_exit)
        quitButton.place(x=450,y=370)

    def client_exit(self):
        exit()

root=Tk()
root.geometry('500x400')

# instance creation
application = Window(root)

root.mainloop()

from tkinter_source_file import *
from pillow_lib_tk import *


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        # ref to the master widget aka tk window
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title('GUI Img/Txt')
        self.pack(fill=BOTH, expand=1)

        # creation of a menu
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # file obj creation
        file = Menu(menu)

        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        # edit obj creation
        edit = Menu(menu)

        edit.add_command(label='Show Image', command=self.showImage)
        edit.add_command(label='Show Text', command=self.showText)
    #    edit.add_command(label='Delete Text', command=self.delText())

        menu.add_cascade(label='Edit', menu=edit)

    def showImage(self):
        load_image = Image.open('image/wallhaven-eyp3ro.png')
        load_image_size = load_image.resize((470,380), Image.ANTIALIAS)
        load_image_render = ImageTk.PhotoImage(load_image_size)

        # labels 4 either txt or image
        image = Label(self, image=load_image_render)
        image.image = load_image_render
        image.place(x=0, y=0)

    def showText(self):
        text = Label(self, text='Hello User')
        text.pack()

 #    Will check more info in regarding the text widget http://effbot.org/tkinterbook/text.htm#patterns
    #   def delText(self):
    #       text = Label(self, text='Delete' , command=lambda: text.delete(1.0,END))
    #      text.pack()


    def client_exit(self):
        exit()


# window creaton for user to see the program tabs/info

window_root = Tk()
window_root.geometry('500x400')

application = Window(window_root)

# main loop
window_root.mainloop()

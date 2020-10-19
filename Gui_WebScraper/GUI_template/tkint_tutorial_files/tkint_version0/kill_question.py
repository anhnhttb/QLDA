from tkinter_source_file import *
# Acquired from https://www.daniweb.com/programming/software-development/threads/66698/exit-a-tkinter-gui-program
# Other options if a user would like to shut down the program.
# Will look further into this to make the program more interactive and to help aid in A.i development as well
# Could be good to give an A.i for the program some personality/piszas
# Also heres the stack overflow in regarding to using this for .Py 3
# https://stackoverflow.com/questions/38181710/tkmessagebox-no-module/38181986


def ask_quit():
    if tkinter.messagebox.askokcancel("Quit", "You want to quit now? *sniff*"):
        root.destroy()
root = Tk()
root.protocol("WM_DELETE_WINDOW", ask_quit)
root.mainloop()
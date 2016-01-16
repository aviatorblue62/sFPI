from Tkinter import *
import sys, os
from Application import GUI

# The backbone Application Class

def main():
    app = GUI(master=root)
    mods = app.master

    # Modify GUI features
    mods.title("GUI - Scanning Fabry-Perot Interferometer")
    app.mainloop()
    # send to GUI Application and display accordingly

if __name__ == "__main__":
    root = Tk()
    main()
    sys.exit()
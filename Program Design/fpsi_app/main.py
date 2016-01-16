#from ImageProcessing import WriteToImage as WTI
import sys,os,re
from time import strftime as date, sleep
from subprocess import call, Popen
from PIL import Image as IM, ImageTk as ITK
from Tkinter import *
from USBinterface import SERIALPORT as SP
#from DataAnalysis import Compute as op
#from GUIErrors import *
import argparse,sys,os,re

# The backbone Application Class
class Application(Frame):
    def __init__(self,master=None,port=None,data=None,go=None):
        Frame.__init__(self,master,bd=1)
        # Initialize Class Variables and Functions
        self.master = master

        # Set the geometry of the main windowing
        self.setGeometry()

        # Set Image variables
        self.image = "Graph_Update.gif"

        # Set error routine
        #self.error = Error(master=root)

        # Set Port variable
        self.port = port

        # Execute Initialization Functions for Operation
        self.pack()
        self.create_menu_bar()
        self.Preferences()
        if self.preferences_test_var is not True:
            self.updateImage()
            self.display_port()
        else:
            self.data_testing()


###################################################################################################################
# Function: create_menu_bar
#
# Inputs:   self.master
#
# Outputs:  Generates menu bar with the following menus:
#               1. File
#                   a. New Project..
#                   b. Save Project
#                   c. Exit
#               2. Edit
#                   a. Copy Image
#               3. Tools
#                   a. Change Serial Port
#                   b. Preferences
#                   c. Pause
#                   d. Start
###################################################################################################################


    def create_menu_bar(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # File Menu
        fileMenu = Menu(menu)
        menu.add_cascade(label="File",menu=fileMenu)
        fileMenu.add_command(label="New Project...", command=self.updateImage)
        fileMenu.add_command(label="Save Project", command=self.saveProject)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=root.destroy)

        # Edit Menu
        editMenu = Menu(menu)
        menu.add_cascade(label="Edit",menu=editMenu)
        editMenu.add_command(label="Copy Image", command=self.saveProject)

        # Tools Menu
        toolsMenu = Menu(menu)
        menu.add_cascade(label="Tools",menu=toolsMenu)
        toolsMenu.add_command(label="Change Serial Port", command=self.Serial_Window)
        toolsMenu.add_command(label="Preferences", command=self.Preferences)
        toolsMenu.add_separator()
        toolsMenu.add_command(label="Pause", command=self.PauseImage)
        toolsMenu.add_command(label="Start", command=self.CurrentImage)

###################################################################################################################
# Function: updateImage
#
# Inputs:   None
#
# Outputs:  Creates a frame. Sets the standard image height to the screenheight - 150 px and the screen width to
#           screenwidth. It sets the image in a canvas using the previously defined height and width.
###################################################################################################################

    def updateImage(self):
        iframe2 = Frame(self,bd=2)

        self.width = self.master.winfo_screenwidth()
        self.height = self.master.winfo_screenheight()-150

        self.canvas = Canvas(iframe2, width=self.width, height=self.height, bg="white")
        self.filename = PhotoImage(file=self.image)
        image = self.canvas.create_image(0, 0, anchor=NW, image=self.filename)
        self.canvas.pack(side="top")

        iframe2.pack(expand=1, fill=X, pady=20, padx=100)

###################################################################################################################
# Function: saveProject
#
# Inputs:   None
#
# Outputs:  Creates time stamped image name and saves it to a path using a bash command.
#
# Notes: *** This will need to change in order to promote cross platform usage. ***
###################################################################################################################

    def saveProject(self):
        save_image = './images/' + date('%Y-%m-%d_%H%M%S') + '.gif'
        call(['cp','Graph_Update.gif',save_image])

    def PauseImage(self):
        self.pause_image = './images/pause/' + date('%Y-%m-%d_%H%M%S') + '.gif'
        call(['cp','Graph_Update.gif',self.pause_image])
        self.image = self.pause_image

    def CurrentImage(self):
        self.image = "Graph_Update.gif"

    def setGeometry(self):
        self.master.geometry('{}x{}'.format(self.master.winfo_screenwidth(), self.master.winfo_screenheight()))

###################################################################################################################
# Function: Preferences
#
# Inputs:   None
#
# Outputs:  Sets specific variables for use in operation.
###################################################################################################################

    def Preferences(self):
        self.preferences = Toplevel(self.master)
        iframe = Frame(self.preferences,bd=3)

        self.preferences_test_var = IntVar()
        self.Testing = Checkbutton(iframe, text="Testing", variable=self.preferences_test_var, onvalue=True, offvalue=False)
        self.Testing.pack()

        self.Submit = self.GET = Button(iframe, text="Submit",fg="black",
                                                command=self.close_window)
        self.Submit.pack(side=RIGHT,padx=5)

        iframe.pack(expand=1, fill=X, pady=10, padx=5)
        self.preferences.attributes("-topmost", True)
        self.preferences.title("Preferences")
        self.preferences.geometry('{}x{}'.format(1000, 300))

        self.preferences.update_idletasks()
        w = self.preferences.winfo_screenwidth()
        h = self.preferences.winfo_screenheight()
        size = tuple(int(_) for _ in self.preferences.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        self.preferences.geometry("%dx%d+%d+%d" % (size + (x, y)))

###################################################################################################################
# Function: Serial_Window
#
# Inputs:   None
#
# Outputs:  Generates button "GET" and text entry "e".
#           When button "GET" is pressed, execution is passed to function GetPort
###################################################################################################################

    def Serial_Window(self):
        self.serial_window = Toplevel(self.master)
        iframe1 = Frame(self.serial_window,bd=2)

        # Get Port Button
        self.GET = Button(iframe1, text="Store Port",fg="black",
                                                command=self.GetPort)
        self.GET.pack(side=RIGHT, padx=5)

        self.e = Entry(iframe1)
        self.e.pack(side=RIGHT, padx=0)

        self.e.delete(0, END)
        self.e.insert(0, "Enter Port Location")

        iframe1.pack(expand=1, fill=X, pady=10, padx=5)

    def GetPort(self):
        self.port = self.e.get()
        info = open("./docs/info.bin",'w')
        string = self.port
        info.write(string)
        info.close()
        self.port_name = string
        self.serial_window.destroy()
        self.update_port()

    def display_port(self):
        try:
            info = open("./docs/info.bin",'r')
            self.port_name = info.read()
            self.name_label = Label(root, text=self.port_name, bd=1, relief=SUNKEN, anchor=SE)
            self.name_label.pack(fill=X)
        except IndexError as ie:
            port = "No Port Selected"
            self.name_label = Label(root, text=port, bd=1, relief=SUNKEN, anchor=SE)
            self.name_label.pack(fill=X)
        except IOError as INOUT:
            port = "No Port Selected"
            self.name_label = Label(root, text=port, bd=1, relief=SUNKEN, anchor=SE)
            self.name_label.pack(fill=X)

    def update_port(self):
        self.name_label.configure(text=self.port_name)

    def close_window(self):
        self.preferences.destroy()


class Error(Frame):
    def __init__(self,master=None,variable=None):
        Frame.__init__(self,master)
        self.variable = variable
        self.pack()
        self.canvas = Canvas(root, width=500, height=100, bg="white")
        self.canvas.pack(side="top")
        self.createWidgets()

    def createWidgets(self):

        text = self.variable
        err = "ERROR: " + text
        # Quit Button
        self.QUIT = Button(self, text=err, fg="red",
                                            command=root.destroy)
        self.QUIT.pack(side="right")

def main():
    try:
        app = Application(master=root)
        mods = app.master

        # Modify GUI features
        mods.title("GUI - Scanning Fabry-Perot Interferometer")
        app.mainloop()
        # send to GUI Application and display accordingly

    except IOError as io:
        print "No Bueno, Me Amigo"

if __name__ == "__main__":
    root = Tk()
    main()
    sys.exit()

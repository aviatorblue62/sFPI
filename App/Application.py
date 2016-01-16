import csv, os
import numpy as np
import datetime
import FileDialog
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg \
    import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from USBInterface import SerialPort as SP
from Tkinter import *
# from GUIErrors import *

class GUI(Frame):
    def __init__(self,directory="/Applications/sFPI-GUI",
                 master=None,port=None,data=None,go=None):
        Frame.__init__(self,master,bd=1)
        # Initialize Class Variables and Functions
        self.cwd = directory
        self.master = master
        self.calibrated = False
        self.max_screenwidth = 1200
        self.max_screenheight = 690
        self.start_time = None

        # Set the geometry of the main windowing
        self.set_geometry()

        # Data Variables
        self.driver = [1]
        self.pdiode = [1]
        self.preferences_pause = False
        filename = self.cwd + "/docs/info.bin"
        if not os.path.exists(os.path.dirname(filename)):
            self.port_name = "New Port Address"
        else:
            self.port_name = open(filename,'r').read()
        # Set Port variable
        self.port = port
        # Execute Initialization Functions for Operation
        self.pack()
        self.clock()
        self.tell_time()
        self.create_menu_bar()
        self.preferences()
        self.display_port()
        self.update()

    def create_menu_bar(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # File Menu
        fileMenu = Menu(menu)
        menu.add_cascade(label="File",menu=fileMenu)
        fileMenu.add_command(label="New Project...",
                             command=self.save_project())
        fileMenu.add_command(label="Save Project",
                             command=self.save_project)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit",
                             command=self.master.destroy)

        # Edit Menu
        editMenu = Menu(menu)
        menu.add_cascade(label="Edit",menu=editMenu)
        editMenu.add_command(label="Copy Image",
                             command=self.save_project)

        # Tools Menu
        toolsMenu = Menu(menu)
        menu.add_cascade(label="Tools",menu=toolsMenu)
        toolsMenu.add_command(label="Change Serial Port",
                              command=self.serial_window)
        toolsMenu.add_command(label="Calibrate",
                              command=self.fsr_calibration)
        toolsMenu.add_command(label="Preferences",
                              command=self.preferences)
        toolsMenu.add_separator()
        toolsMenu.add_command(label="Pause", command=self.pause)
        toolsMenu.add_command(label="Start", command=self.resume)
        toolsMenu.add_command(label="Get Ramp",
                              command=self.get_ramp)

    def graph_data(self):
        if bool(self.preferences_twoplot_var.get()) is False:
            f = Figure(figsize=(15,6), dpi=100,)
            self.graph = f.add_subplot(111)
            self.plot_data, = self.graph.plot(0,0)

            self.graph_canvas = FigureCanvasTkAgg(f, self)
            self.graph_canvas.show()
            self.graph_canvas.get_tk_widget().pack(side=BOTTOM,
                                                   fill=BOTH, expand=True)

            toolbar = NavigationToolbar2TkAgg(self.graph_canvas, self)
            toolbar.update()
            self.graph_canvas._tkcanvas.pack(side=TOP,
                                             fill=BOTH, expand=True)
        else:
            f = Figure(figsize=(15,6), dpi=100,)
            self.graph1 = f.add_subplot(211)
            self.graph2 = f.add_subplot(212)
            self.plot_data_1, = self.graph1.plot(0,0)
            self.plot_data_2, = self.graph2.plot(0,0)

            self.graph_canvas = FigureCanvasTkAgg(f, self)
            self.graph_canvas.show()
            self.graph_canvas.get_tk_widget().pack(side=BOTTOM,
                                                   fill=BOTH, expand=True)

            toolbar = NavigationToolbar2TkAgg(self.graph_canvas, self)
            toolbar.update()
            self.graph_canvas._tkcanvas.pack(side=TOP,
                                             fill=BOTH, expand=True)
        self.update_graph()

    def update_graph(self):
        if bool(self.preferences_twoplot_var.get()) is False:
            self.graph.clear()
            self.graph.plot(np.array(self.driver),
                            np.array(self.pdiode),"r")
            self.graph.set_title('Spectral Plot of Cavity')
            self.graph.set_xlabel('Frequency (GHz)')
            self.graph.set_ylabel('Normalized Intensity')
            self.graph_canvas.draw()

        else:
            self.graph1.clear()
            self.graph1.plot(np.array(self.driver),"r")
            self.graph1.set_title('Ramp Function')

            self.graph2.clear()
            self.graph2.plot(np.array(self.pdiode),"r")
            self.graph2.set_title('Photodiode Output')
            self.graph_canvas.draw()

        if self.preferences_pause is False:
            self.after(500,self.update_graph)

    def save_project(self):
        filename = self.cwd + '/Logs/' + \
                   datetime.datetime.now().strftime("%m-%d-%Y-%H_%M_%S") \
                   + '.csv'
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
        with open(filename, 'wb') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|',
                                    quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(self.driver)
            spamwriter.writerow(self.pdiode)
        csvfile.close()

    def pause(self):
        self.preferences_pause = True

    def resume(self):
        self.preferences_pause = False
        self.update_graph()
        self.serial = SP(port=self.port_name)
        self.serial_read()

    def get_ramp(self):
        self.serial = SP(port=self.port_name,get_ramp=True)
        self.serial_read(run_once=True)

    def set_geometry(self):
        if self.master.winfo_screenwidth() > self.max_screenwidth:
            self.screen_width = self.max_screenwidth
        else:
            self.screen_width = self.master.winfo_screenwidth()

        if self.master.winfo_screenheight() > self.max_screenheight:
            self.screen_height = self.max_screenheight
        else:
            self.screen_height = self.master.winfo_screenwidth()

        self.master.geometry('{}x{}'.format(self.screen_width,
                                            self.screen_height))
        self.master.minsize(self.screen_width,self.screen_height)
        self.master.maxsize(self.screen_width,self.screen_height)

    def fsr_calibration(self):
        self.cal_window = Toplevel(self.master)
        self.cal_window.title("FSR (GHz)")
        iframe1 = Frame(self.cal_window,bd=2)

        # Get Port Button
        self.butt = Button(iframe1, text="Calibrate",fg="black",
                           command=self.begin_calibration)
        self.butt.pack(side=RIGHT, padx=5)

        self.fsr = Entry(iframe1)
        self.fsr.pack(side=RIGHT, padx=0)

        self.fsr.delete(0, END)
        self.fsr.insert(0, "FSR (GHz)")

        iframe1.pack(expand=1, fill=X, pady=10, padx=5)

    def begin_calibration(self):
        self.calibrated = True
        self.cal_window.destroy()

    def set_calibration(self):
        fsr = self.fsr.get()
        fsr_range = float(fsr)
        data_range = max(self.driver)-min(self.driver)
        scale = float(fsr_range/data_range)
        offset = self.driver[0]
        normalize = max(self.pdiode)
        for k in range(len(self.driver)):
            self.driver[k] = self.driver[k] - offset
            self.driver[k] = scale*self.driver[k]
            self.pdiode[k] = self.pdiode[k]/normalize
        self.graph.set_ylim((0,1),auto=False)
        self.graph.set_ymargin(0)

    def preferences(self):
        self.preferences = Toplevel(self.master)
        iframe = Frame(self.preferences,bd=3)

        self.preferences_test_var = IntVar()
        self.Testing = Checkbutton(iframe, text="Testing",
                                   variable=self.preferences_test_var,
                                   onvalue=True, offvalue=False)
        self.Testing.pack()

        self.preferences_twoplot_var = IntVar()
        self.Plot2 = Checkbutton(iframe, text="Plot Seperate Graphs",
                                 variable=self.preferences_twoplot_var,
                                 onvalue=True, offvalue=False)
        self.Plot2.pack()

        self.Submit = self.GET = Button(iframe, text="Submit",fg="black",
                                        command=self.close_window,
                                        relief=SUNKEN)
        self.Submit.pack(fill=X)

        iframe.pack(expand=1, fill=X, pady=10, padx=5)
        self.preferences.attributes("-topmost", True)
        self.preferences.title("Preferences")
        self.preferences.geometry('{}x{}'.format(170, 90))
        self.preferences.minsize(170,90)

        self.preferences.update_idletasks()
        w = self.preferences.winfo_screenwidth()
        h = self.preferences.winfo_screenheight()
        size = tuple(int(_) for _ in
                     self.preferences.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        self.preferences.geometry("%dx%d+%d+%d" % (size + (x, y)))

    def serial_window(self):
        self.serial_window = Toplevel(self.master)
        iframe1 = Frame(self.serial_window,bd=2)
        self.serial_window.title("Enter Serial Port")

        # Get Port Button
        self.GET = Button(iframe1, text="Store Port",fg="black",
                                                command=self.get_port)
        self.GET.pack(side=RIGHT, padx=5)

        self.e = Entry(iframe1)
        self.e.pack(side=RIGHT, padx=0)

        self.e.delete(0, END)
        self.e.insert(0, self.port_name)

        iframe1.pack(expand=1, fill=X, pady=10, padx=5)

    def get_port(self):
        self.port = self.e.get()
        filename = self.cwd + "/docs/info.bin"
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
        info = open(filename,'w')
        string = self.port
        info.write(string)
        info.close()
        self.port_name = string
        self.serial_window.destroy()
        self.update_port()

    def display_port(self):
        try:
            filename = self.cwd + "/docs/info.bin"
            if not os.path.exists(os.path.dirname(filename)):
                os.makedirs(os.path.dirname(filename))
            info = open(filename,'w')
            self.port_name = info.read()
            self.name_label = Label(self.master, text=self.port_name,
                                    bd=1, relief=SUNKEN, anchor=SE)
            self.name_label.pack(fill=X)

        except IndexError as ie:
            port = "No Port Selected"
            self.name_label = Label(self.master, text=port,
                                    bd=1, relief=SUNKEN, anchor=SE)
            self.name_label.pack(fill=X)

        except IOError as INOUT:
            port = "No Port Selected"
            self.name_label = Label(self.master, text=port,
                                    bd=1, relief=SUNKEN, anchor=SE)
            self.name_label.pack(fill=X)

    def update_port(self):
        self.name_label.configure(text=self.port_name)
        self.serial = SP(port=self.port_name)

    def close_window(self):
        self.preferences.destroy()
        if bool(self.preferences_test_var.get()) is True:
            data = {}
            filename = self.cwd + "/test/photodiode_output.csv"
            if not os.path.exists(os.path.dirname(filename)):
                os.makedirs(os.path.dirname(filename))
            with open(filename,'r') as csvdata:
                data_reader = csv.reader(csvdata)
                i = 0
                for row in data_reader:
                    if i == 0:
                        data['driver'] = row
                        i = i + 1
                    else:
                        data['pdiode'] = row
                for num in range(len(data['driver'])):
                    data['driver'][num] = float(data['driver'][num])
                    data['pdiode'][num] = float(data['pdiode'][num])
                self.driver = data['driver']
                self.pdiode = data['pdiode']
        self.graph_data()

    def clock(self):
        self.time = Label(self.master, bd=1, relief=SUNKEN, anchor=SE)
        self.time.pack(fill=X)

    def tell_time(self):
        time = datetime.datetime.now().strftime("Time: %H:%M:%S")
        self.time.config(text=time)
        #lab['text'] = time
        self.after(1000, self.tell_time) # run itself again after 1000 ms

    def serial_read(self,run_once=False):
        data = self.serial.Get_Data()
        if data is not False:
            if data['get_ramp'] is False:
                self.pdiode = data['values']
            else:
                self.driver = data['values']

            if self.calibrated == True:
                self.set_calibration()

            if run_once is False:
                self.after(1000,self.serial_read)
        else:
            self.name_label.configure(text="Communication Failed")
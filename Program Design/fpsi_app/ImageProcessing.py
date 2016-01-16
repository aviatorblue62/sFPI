import sys,os,re
from GUIErrors import *
#from PIL import Image as IM

class WriteToImage():
    def __init__(self,data,image):
        self.image = image
        DI = DetermineImage(image=self.image)
        self.zero = DI.zero
        self.scale = DI.scale

    def pixle_coordinates(self):

class DetermineImage():
    def __init__(self,image):
        self.loc = None
        self.width = None
        self.height = None
        self.zero = []
        self.photo=image
        self.im = IM.open(self.photo)
        self.pix = self.im.load()

    def find_edge(self):
        dim = self.im.size
        self.height = dim[0]
        self.width = dim[1]
        # Find vertical edge
        self.cycle_y()
        # Find horizontal edge
        self.cycle_x()

    def confirm(self,axis):
        if axis == 'y':
            for z in range(self.loc[0],self.loc[0]+100):
                color = self.pix[z,x]
                if color == 0:
                    isaxis = False
                    break
            isaxis = True
        else:
            for z in range(self.loc[1],self.loc[1]+100):
                color = self.pix[y,z]
                if color == 0:
                    isaxis = False
                    break
            isaxis = True
        return isaxis

    def cycle_y(self):
        try:
            for x in range(0,self.width):
                for y in range(0,self.height):
                    color = self.pix[y,x]
                    self.loc = (y,x)
                    if color is not 0:
                        check = self.confirm(axis='y')
                        if check:
                            self.zero[0] = [y,x]
            raise ImageError('No Axis Found')
        finally:
            print "Try another image please :)"

    def cycle_x(self):
        try:
            for y in range(0,self.width):
                for x in range(0,self.height):
                    color = self.pix[y,x]
                    self.loc = (y,x)
                    if color is not 0:
                        check = self.confirm(axis='y')
                        if check:
                            self.zero[0] = [y,x]
            raise ImageError('No Axis Found')
        finally:
            print "Try another image please :)"

    def find_scale(self):

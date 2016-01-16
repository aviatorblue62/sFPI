from subprocess import *
import sys,os,re

class Dimensions():
    def __init__(self,width=None,height=None):
        self.width = width
        self.height = height
        self.get_hw()
        
    def get_hw(self):
        # This is where it gets the height and width
        self.width = 1200
        self.height = 968
        self.imageh = 676
        self.imagew = 1067

    def get_dim(self):
        dim = {}
        dim["width"] = self.width
        dim["height"] = self.height
        dim["imageh"] = self.imageh
        dim["imagew"] = self.imagew

        return dim

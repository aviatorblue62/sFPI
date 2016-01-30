#! /usr/bin/python

import sys, os, re
from subprocess import call
import csv
import math


def generate(self,amplitude=None,duration=None,freq=None,length=None,cond=1,data=None):
    global filename
    filename = str(raw_input('Path to written File and Filename: '))
    dp = []
    string = None
    if freq is not None:
        freq = float(freq)
    filename = filename + '.txt'
    if cond == 1:
        f = open(filename, 'w')
        x = 1
        time = (0.0+x-1)/freq
        volts = 0
        string = str(time) + ' ' + str(volts) + ' '
        f.write(string)
        while x <= length:
            time = [(1.0+x-1)/freq,(1.001+x-1)/freq,(2+x-1)/freq]
            volts = [5,0,2.5]
            string = str(time[0]) + ' ' + str(volts[0]) + ' ' + str(time[1]) + ' ' + str(volts[1]) +\
                     ' ' + str(time[2]) + ' ' + str(volts[2]) + ' '
            print (string)
            f.write(string)
            x = x + 2
        f.close()

    elif cond == 4:
        horizontal = {}
        vertical = {}
        horizontal['name'] = None
        horizontal['data'] = []
        horizontal['units'] = None
        vertical['name'] = None
        vertical['data'] = []
        vertical['units'] = None
        with open(data,'rb') as csvfile:
            data_file = csv.reader(csvfile,delimiter = ";",quotechar='|')
            titles = data_file[0][0].split(',')
            for i in range(len(titles)):
                print "Item %d: %s" % (i+1, titles[i])
            horz = input('Horizontal Axis Column (Ex. 1): ')
            vert = input('Vertical Axis Column (Ex. 2): ')
            units_row = 'N' # Default Value
            while True:
                try:
                    units_row = raw_input("Is there a units row?(y/N):  ")
                    break
                except NameError as NE:
                    print ("Cannot determine answer please re-enter")
            if units_row is 'y' or 'Y':
                units_row = True
                u = 1
            else:
                units_row = False
                u = 0
            skipping = input('Number of rows to skip: ')
            scale = input('Scaling Factor: ')
            inc = 1
            for rows in data_file:
                rows = rows[0].split(',')
                if inc == 1:
                    horizontal['name'] = rows[horz-1]
                    vertical['name'] = rows[vert-1]
                elif units_row is True and inc is not 1 and inc < 3:
                    horizontal['units'] = rows[horz-1]
                    vertical['units'] = rows[vert-1]
                elif skipping >= (inc-1+u):
                    # Do Nothing
                    nothing = None
                else:
                    horizontal['data'].append(rows[horz-1])
                    vertical['data'].append(rows[vert-1])
                inc = inc + 1
        csvfile.close()
        output_file = open(filename, 'a')
        for pts in range(len(horizontal['data'])):
            input_string = (str(horizontal['data'][pts]) + ' ' + str(vertical['data'][pts]) + ' ')
            output_file.write(input_string)
        output_file.close()
        print ("Length of each vector was " + str(len(horizontal['data'])) + " data points")

    elif cond == 5:
        noise = []
        time = []
        duration = float(duration)
        length = float(length)
        scale = float(duration/length)
        for pts in range(length):
            noise.append(random.uniform(0,amplitude))
            time.append(pts*scale)
        with open(filename, 'w') as noise_file:
            for values in range(length(noise)):
                string = str(time[values]) + " " + str(noise[values]) + " "
                noise_file.write(string)
            noise_file.close()


def main():
    print ("--- Waveforms ---\n1. Sawtooth\n2. Triangle\n3. Sine/Cosine\n4. Convert CSV Data to PWL\n5. Generate Noise Signal")
    cond = input('>> ')
    if cond == 1:
        length = raw_input('Number of Data Points: ')
        frequency = input('Frequency of the Waveform: ')
        generate(None,None,frequency,length,cond,None)
        print ("Written to " + filename)
    elif cond == 5:
        length = raw_input('Number of Data Points: ')
        amp = raw_input('Amplitude of the Noise Signal(units): ')
        duration = raw_input('Duration of the Noise Signal(sec): ')
        generate(amp,duration,None,length,cond,None)
        print ("Noise file generated to " + filename)
    elif cond == 4:
        data_file = str(raw_input('Path to data file and filename: '))
        generate(None,None,None,None,cond,data_file)
        print ("Data from " + str(data_file) + " was written to " + str(filename))
    else:
        print "Current programs are still in beta testing sorry :("
if __name__ == "__main__":
    main()
    sys.exit()


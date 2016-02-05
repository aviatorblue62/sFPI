#! /usr/bin/python

import sys, os, re
from subprocess import call
import csv
import math
import random

def generate(amplitude,duration,freq,length,cond):
    dp = []
    string = None
    if freq is not None:
        freq = float(freq)
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
        global data
        data = str(raw_input('Path to data file and filename: '))
        try:
            with open(data,'rb') as csvfile:
                data_file = csv.reader(csvfile)
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
        except IOError as no_file:
            print data + " does not exsist, please enter another filename"
            return False
        # Deterime if time is in the correct range
        if horizontal['data'][0] < 0:
            less_than_zero = True
        else:
            less_than_zero = False

        # Comparision for time orentation
        possible_names = ["^[Tt]ime$","^[Ss]econd$","^[Mm]inute$"]
        registered_names = [horizontal['name'],horizontal['units']]
        which_name = 0
        found_name = False
        for j in range(len(registered_names)):
            if found_name == True:
                break
            else:
                while which_name <= :
                    try:
                        name_match = re.match(possible_names[which_name], registered_names[j]).group(0)
                        if name_match is not None:
                            # Function that checks the orentiation of the time access.
                            taxis_is_correct = time_axis(horizontal['data'])
                            found_name = True
                            break
                    except AttributeError as no_match:
                        which_name += 1
                    finally:
                        print ("Apperently there is no time axis... Axis: " + registered_names[j])
                        if j == 1:
                            taxis_is_correct = True
                        break
        # Reverses both data lists if t-axis is incorrectly orientated 
        if taxis_is_correct != True:
            horizontal['data'].reverse()
            vertical['data'].reverse()

        if horizontal['data'][0] < 0:
            for val in range(len(horizontal['data'])):
                horizontal['data'][val] += abs(horizontal['data'][0])
                
        # Write data to file
        output_file = open(filename, 'a')
        for pts in range(len(horizontal['data'])):
            input_string = (str(horizontal['data'][pts]) + ' ' + str(vertical['data'][pts]) + ' ')
            output_file.write(input_string)
        output_file.close()
        print ("Length of each vector was " + str(len(horizontal['data'])) + " data points")
        return True
   # elif cond == 5:
       # scale = float(duration)/float(length)
       # gen = Process(target=random_numbers(scale))
       # watch = Process(target=wait())
       # # if 
       # noise = rand['noise']
       # time = rand['time']
       # with open(filename, 'w') as noise_file:
       #     for values in range(length(noise)):
       #         string = str(time[values]) + " " + str(noise[values]) + " "
       #         noise_file.write(string)
       #     noise_file.close()

def time_axis(t_data):
    compare = []
    standard = []
    for i in range(len(t_data)-1):
        if (t_data[i] < t_data[i+1]):
            compare.append(True)
        else:
            compare.append(False)
        standard.append(True)        
    result = list(set(standard) ^ set(compare))
    if len(result) > 0:
        return False
    else:
        return True

# def random_numbers():
#     noise = []
#     time = []
#     global dict rand
#     for pts in range(int(length)):
#         noise.append(random.uniform(0,float(amplitude)))
#         time.append(pts*scale)
#     rand['noise'] = noise
#     rand['time'] = time
# 
#     return rand

def main():
    print ("--- Waveforms ---\n1. Sawtooth\n2. Triangle\n3. Sine/Cosine\n4. Convert CSV Data to PWL\n5. Generate Noise Signal")
    global filename
    cond = input('>> ')
    filename = str(raw_input('Path to write File and Filename: '))
    filename += ".txt"
    if cond == 1:
        length = raw_input('Number of Data Points: ')
        frequency = input('Frequency of the Waveform: ')
        generate(None,None,frequency,length,cond)
        print ("Written to " + filename)
    elif cond == 5:
        length = raw_input('Number of Data Points: ')
        amp = raw_input('Amplitude of the Noise Signal(units): ')
        duration = raw_input('Duration of the Noise Signal(sec): ')
        generate(amp,duration,None,length,cond)
        print ("Noise file generated to " + filename)
    elif cond == 4:
        while True:
            success = generate(None,None,None,None,cond)
            if success is True:
                break
            else:
                pass
        print ("Data from " + str(data) + " was written to " + str(filename))
    else:
        print "Current programs are still in beta testing sorry :("
if __name__ == "__main__":
    main()
    sys.exit()


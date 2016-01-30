#! /usr/bin/python

import sys, os, re
from subprocess import call
import csv

def generate(freq,length,cond,filename,data):
	dp = []
	string = None
        if freq is not None:
            freq = float(freq)
	filename = filename + '.txt'
	if cond == 1:
		f = open(filename, 'w')
		x = 1;
		time = (0.0+x-1)/freq
		volts = 0
		string = str(time) + ' ' + str(volts) + ' '
		f.write(string)
		while x <= length:
			time = [(1.0+x-1)/freq,(1.001+x-1)/freq,(2+x-1)/freq]
			volts = [5,0,2.5]
			string = str(time[0]) + ' ' + str(volts[0]) + ' ' + str(time[1]) + ' ' + str(volts[1]) +\
					 ' ' + str(time[2]) + ' ' + str(volts[2]) + ' '
			print string
			f.write(string)
			x = x + 2
		f.close()
		
	if cond == 4:
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
			horz = input('Horizontal Axis Column (Ex. 1): ')
			vert = input('Vertical Axis Column (Ex. 2): ')
                        while True:
                            try:
                                units_row = input("Is there a units row?(y/N)  ")
                                break
                            except NameError as NE:
                                print "Cannot determine answer please re-enter"
			if units_row is not "y" or "Y":
				units_row = False
				u = 0
			else:
				units_row = True
				u = 1
			skipping = input('Number of rows to skip: ')
			inc = 1
			for rows in data_file:
				rows = rows[0].split(',')
				if inc == 1:
					horizontal['name'] = rows[horz]
					vertical['name'] = rows[vert]
				elif units_row is True and inc is not 1:
					horizonal['units'] = rows[horz]
					vertical['units'] = rows[vert]
				elif skipping >= (inc-1+u):
					# Do Nothing
                                        nothing = None
				else:
                                        print rows
                                        horizontal['data'].append(rows[horz-1])
                                        vertical['data'].append(rows[vert-1])
				inc = inc + 1
                        csvfile.close()
                output_file = open(filename, 'a')
                for pts in range(len(horizontal['data'])):
                        input_string = (str(horizontal['data'][pts]) + ' ' + str(vertical['data'][pts]) + ' ')
                        output_file.write(input_string)
                output_file.close()
		print str(data) + " has been written to " + filename + " with horizontal axis " + horizontal['name'] +\
				" and vertical axis " + vertical['name']
	
def main():
	print "--- Waveforms ---\n1. Sawtooth\n2. Triangle\n3. Sine/Cosine\n4. Convert CSV Data to PWL"
	cond = input('>> ')
	filename = str(input('Path to written File and Filename: '))
	if cond != 4:
		length = input('Number of Data Points: ')
		frequency = input('Frequency of the Waveform: ')
		generate(frequency,length,cond,filename,None)
		print ("Written to " + filename + '.txt')
	else:
		data_file = str(input('Path to data file and filename: '))
		generate(None,None,cond,filename,data_file)
		print ("Data from " + str(data_file) + " was written to " + str(filename))

if __name__ == "__main__":
	main()
	sys.exit()
	

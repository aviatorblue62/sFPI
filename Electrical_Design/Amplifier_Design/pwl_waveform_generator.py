#! /usr/bin/python


import sys, os, re
from subprocess import call

def generate(freq,length,cond,filename):
	dp = []
	string = None
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
	
def main():
	print "--- Waveforms ---\n1. Sawtooth\n2. Triangle\n3. Sine/Cosine\n4. Convert MATLAB Data to PWL"
	cond = input('>>')
	filename = input('Path to File and Filename: ')
	if cond != 4:
		length = input('Number of Data Points: ')
		frequency = input('Frequency of the Waveform: ')
		generate(frequency,length,cond,filename)
		print ("Written to " + filename + '.txt')

if __name__ == "__main__":
	main()
	sys.exit()
	

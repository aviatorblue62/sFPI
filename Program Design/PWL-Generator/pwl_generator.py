import sys, os, re
from subprocess import call

def generate(freq,length,type,filename):
	dp = []
	string = None
	freq = float(freq)
	filename = filename + '.txt'
	if type == "sawtooth":
		file = open(filename, 'a')
		while x is not length:
			time = [(0.0+x)/freq,(1.0+x)/freq,(1.001+x)/freq]
			volts = [0,5,0]
			string = str(time[0]) + ' ' + str(volts[0]) + str(time[1]) + ' ' + str(volts[1]) +\
					 str(time[2]) + ' ' + str(volts[2]) + ' '
			file.write(string)
			x = x + 2			
	file.close()
	
def main():
	pring """\
			--- Waveforms ---
			1. Sawtooth
			2. Triangle
			3. Sine/Cosine
			4. Convert MATLAB Data to PWL"""
	type = input('>>')
	filename = input('Path to File and Filename: ')
	if type != 4:
		length = input('Number of Data Points: ')
		frequency = input('Frequency of the Waveform: ')
		generate(frequency,length,type)
		print ("Written to " + filename + '.txt')
	else:
	

if __name__ == "__main__":
	main()
	sys.exit()
	

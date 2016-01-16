#! /usr/bin/python

import sys, re, os

def pwl_file(filename,num_var,length_var):
	offset = 0
	variables = []
	lt_table = open(filename, 'r')
	output = lt_table.read()
	list = output.split('   ')
	for i in range(num_var):
		for j in range(length_var[i]):
			variables.append(list[j+offset])
		variables.append('ixx')
		offset = j		

	output = ' '.join(variables).split('ixx')
	output[0] = output[0].split(' ')
	output[1] = output[1].split(' ')	
	new_file_name = filename.split('.')[0] + '_new'  
	new_file = open(new_file_name, 'a')

	for k in range(length_var[0]):
		print k
		out1 = str(output[0][k]) + ' ' + str(output[1][k]) + ' '	
		new_file.write(out1)

	new_file.close()


def main():
	length_var = []
	possible_progs = ['ltspice','matlab','arduino'];
	filename = raw_input('Enter Path to File: ')
	program = raw_input('Which Program are you writing this file to? ')
	if program.lower() == possible_progs[0]:
		num_var = int(raw_input('Enter Number of Variablesi: '))
		for var in range(0,num_var):
			length_var.append(int(input('Enter in length of Variable ' + str(var+1) + ':')))

		pwl_file(filename,num_var,length_var)

if __name__ == "__main__":
	main()
	sys.exit()

	
			

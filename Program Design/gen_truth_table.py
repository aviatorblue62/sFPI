#! /usr/bin/python

import subprocess, re, os, sys

def binary_to_truth(num):
	list = ['LOW','LOW','LOW','LOW','LOW','LOW','LOW','LOW']
	count = 0
	while num != 0:
		count = count + 1
		bit = num % 2
		if bit == 0:
			list[-count]='LOW'
		elif bit == 1:
			list[-count]='HIGH'
		num = num / 2
	list = list[::-1]
	list = ','.join(list)
	list = '{' + list + '},'
	print list
	return list

def main():
	LIST = []
	indiv = []
	tabledoc = open('truth_table.txt','a')
	tabledoc.write('{')
	for DB in range(0,255):
		indiv.append(binary_to_truth(DB))
		list_line = '\n'.join(indiv)
		list_out = list_line
		tabledoc.write(list_out)
	tabledoc.write('}')
	tabledoc.close()

if __name__ == "__main__":
	main()
	sys.exit()

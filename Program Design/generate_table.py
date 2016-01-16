#! /usr/bin/python

import sys, os, re, itertools


def standard():
	tabledoc = open('rampfunc.txt','a')
	n = 4096
	table = list(itertools.product(['LOW', 'HIGH'], repeat=n))
	string = str(table)
	tabledoc.write(string)
	tabledoc.close()

def main():
	standard()

if __name__ == "__main__":
	main()
	sys.exit()

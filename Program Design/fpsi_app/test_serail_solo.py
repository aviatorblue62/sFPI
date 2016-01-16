import sys,os,re
import serial

def test():
	ser = serial.Serial("/dev/tty.usbmodemfd121", 9600)
	ser.write("1")
	return ser.readlines()




def main():


if __name__ == "__main__":
	main()
	sys.exit()
import serial

def SERIALPORT():
	ser = serial.Serial("/dev/tty.usbmodemfd121", 9600)
	ser.write("1")
	return ser.readlines()






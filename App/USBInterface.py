import serial, time, itertools
from GUIErrors import *

class SerialPort():
    def __init__(self,port=None,get_ramp=False):
        try:
            self.get_ramp = get_ramp
            self.error = False
            self.ser = serial.Serial(port, 57600,timeout=1)
        except OSError as Bad_Port:
            self.error = True

    def Get_Data(self):
        try:
            arduino_data = []
            data = []
            if self.error is not True:
                # VERY IMPORTANT!!!
                time.sleep(1/1000)
                self.ser.setDTR(level=0)
                time.sleep(1/1000)
                if self.get_ramp == True:
                    self.ser.write("0")
                else:
                    self.ser.write("1")
                self.bits = 256
                for i in range(0,(self.bits*2)):
                    arduino_data.append(self.ser.read())
                if arduino_data[0] == '':
                            raise DataError(arduino_data[0])
                arduino_data = self.deArduinoify(arduino_data)
                self.ser.flush()
                for i in range(0,self.bits-1):
                    data.append(self.add_hex(arduino_data[2*i],
                                             arduino_data[2*i+1]))
            else:
                data = []
                raise DataError('No Data')

            output = {'values':data,'get_ramp':self.get_ramp}
            return output
        except DataError as Bad_comm:
            return False

    def deArduinoify(self,data):
        values = []
        for k in range(len(data)):
            d = data[k].encode('hex')
            dnew = int(d,16)
            values.append(dnew)
        return values

    def add_hex(self,A,B):
        conv = B*256 + A
        return conv
import serial
import time


#Set settings - interactivity with aquaresp

#Load settings

#Open Device

#Test COMPORTS
# ser.write("#IDNR\r".encode())
# ser.write("#BAUD\r".encode())
# ser.write("#BAUD\r".encode())
# ser.write("#LOGO\r".encode())

#LOG DATA
channelsactive = 2


#open serial port
while 1:
    with serial.Serial('COM3', 115200, timeout=5) as ser:
        #loop active channels
        for c in range(1,channelsactive+1):
            mystamp = float(time.time())
            mycmd = "MEA "+str(c)+" 1\r"
            ser.write(mycmd.encode())
            response =  ser.readline()
            # time.sleep(.5)
            sr = [i for i in response.decode().split(' ')]
            status, dphi, umolar, mbar, airSat, tempSample, tempCase, signalIntensity, ambientLight, pressure, humidity,resistorTemp, percentO2, tempOptical, pH, ldev = sr[:16]
            oxsat = float(airSat)
            print("Channel: ", c,oxsat/1000.0,mystamp)

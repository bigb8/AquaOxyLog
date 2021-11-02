import serial
import time
import os


#Own libs
import assist


#Load settings

saveloc_data, saveloc_latest, deviceport, channelsactive = assist.getsettings2()

#LOG DATA

delta_timeout = float("%.2f" % (1/float(channelsactive)))

t0 = float(time.time())
with open(str(int(t0))+".txt",'w') as flog:
    flog.write("%s;%s;%s;%s;\n" % ("CHANNEL", "OXYGEN AIR SAT", "TIME ABS","TIME REL"))

#open serial port
while 1:
    with serial.Serial(deviceport, 115200, timeout=delta_timeout) as ser:
        #loop active channels
        for c in range(1,channelsactive+1):
            #Get time stamp
            mystamp = float(time.time())

            #Create serial command for reading oxygen at channel
            mycmd = "MEA "+str(c)+" 1\r"

            #Send command
            ser.write(mycmd.encode())

            #Wait for line response
            response =  ser.readline()

            #decode command
            sr = [i for i in response.decode().split(' ')]
            status, dphi, umolar, mbar, airSat, tempSample, tempCase, signalIntensity, ambientLight, pressure, humidity,resistorTemp, percentO2, tempOptical, pH, ldev = sr[:16]

            # convert to number
            oxsat = float(airSat)/1000.0
            print("Channel: ", c,oxsat,mystamp)

            #Save to log file
            with open(str(int(t0))+".txt",'a') as flog:
                flog.write("%s;%s;%s;%s;\n" % (c, oxsat, mystamp,mystamp-t0))

            #Save to active datafile
            with open(saveloc_latest + str(c) +".aqua",'w') as flatest:
                flatest.write("%s;%s;" % (mystamp,oxsat))

            #Save to active datafile for plotting
            with open("liveplot"+os.sep+ str(c) +".aqua",'w') as flatest:
                flatest.write("%s;%s;" % (mystamp,oxsat))

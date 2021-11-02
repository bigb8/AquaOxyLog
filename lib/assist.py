
import os
import json
import getpass


def savesettings(settings):
    #Write json settings file.  ALREADY DEPRECATED - CONSIDER DELETION
    with open("settings.aquaset", "w") as outfile:
        json.dump(settings, outfile)



def getsettings():
    #Read JSON settingsfile. ALREADY DEPRECATED - CONSIDER DELETION
    with open("settings.aquaset","r") as json_file:
        data = json.load(json_file)

    saveloc_data = data["saveloc_data"]
    saveloc_latest = data["saveloc_latest"]
    deviceport = data["deviceport"]
    channelsactive = data["channelsactive"]

    return saveloc_data, saveloc_latest, deviceport, int(channelsactive)


def getsettings2():
    #Get system username
    un = getpass.getuser()

    #Parsing of settings text file. ACTIVE
    with open("settings.txt",'r') as fread:
        lines = fread.readlines()

    for l in lines:
        data = l.split(";")

        if data[0] == "channels":
            channelsactive = data[1].split("\n")[0].replace(" ","")

        if data[0] == "loc1":
            saveloc_data = data[1].split("\n")[0]
            saveloc_data = saveloc_data.replace("[USERNAME]",un)

        if data[0] == "loc2":
            saveloc_latest = data[1].split("\n")[0]
            saveloc_latest = saveloc_latest.replace("[USERNAME]",un)
            print(saveloc_latest)
        if data[0] == "comport":
            deviceport = data[1].split("\n")[0].replace(" ","")

    return saveloc_data, saveloc_latest, deviceport, int(channelsactive)

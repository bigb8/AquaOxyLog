
import os
import json



def savesettings(settings):
    with open("settings.aquaset", "w") as outfile:
        json.dump(settings, outfile)



def getsettings():
    with open("settings.aquaset","r") as json_file:
        data = json.load(json_file)

    saveloc_data = data["saveloc_data"]
    saveloc_latest = data["saveloc_latest"]
    deviceport = data["deviceport"]
    channelsactive = data["channelsactive"]

    return saveloc_data, saveloc_latest, deviceport, channelsactive

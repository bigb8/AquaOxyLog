import assist as ass

#Setsettings
# settings = {
#     "saveloc_data": "",
#     "saveloc_latest": "",
#     "deviceport": "COM3",
#     "channelsactive": 2
# }
#

# ass.savesettings(settings)


saveloc_data, saveloc_latest, deviceport, channelsactive = ass.getsettings2()

print(saveloc_data, saveloc_latest, deviceport, channelsactive)

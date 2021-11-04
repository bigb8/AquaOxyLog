# AquaOxyLog
 Simple logger software for Pyroscience Firesting

For use with AquaResp.


## Features

Retrieves and saves OXYGEN (as % AIR SAT) data from Pyroscience Firesting fiber optic sensors.

Creates one (1) data file per session. Logs sensors, up to 4, at approximately 1 sample per second.

Updates a file with the latest measurement (For external access, e.g. Aquaresp or similar)

You can request features if you think that something would be nice to have.

## Getting started

## Prerequisites
1. Python installed
2. **pyserial** installed. > Open CMD (Windows button, then type "cmd") > write "py -m pip install pyserial", press ENTER

### Preparation of the oxygen sensor

**The logger requires that the oxygen meter is set up and calibrated before use.**

 1. Calibrate and setup the oxygen logger via the PyroWorkbench provided by the manufacturer.
 See [PyroScience](https://www.pyroscience.com/en/downloads/laboratory-devices)

 2. Close PyroScience Software. This is necessary as only 1 software connection to the hardware is possible.

### Start Aqua OxyLog

 3.  Create a settings file: Find the index.html file in /settinggui file out and press download. Place the "downloaded" file in the /lib folder, replace the existing one.

 4. Run Logger.bat

 5. Check file at Location Datafile. See live data using the data.html in /lib/liveplot/

 6. End logging by closing the CMD window.


 A more elaborate quick guide is available here as PDF
 [PDF GUIDE](https://github.com/bigb8/AquaOxyLog/raw/main/Aqua%20OxyLog%2020211102.pdf)

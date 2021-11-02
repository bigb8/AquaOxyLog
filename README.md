# AquaOxyLog
 Simple logger software for Pyroscience Firesting

For use with AquaResp.


## Features

Retrieves and saves OXYGEN (as % AIR SAT) data from Pyroscience Firesting fiber optic sensors.

Creates one (1) data file per session. Logs sensors, up to 4, at approximately 1 sample per second.

Updates a file with the latest measurement (For external access, e.g. Aquaresp or similar)

You can request features if you think that something would be nice to have.

## Getting started

### Preparation of the oxygen sensor

 1. Calibrate and setup the oxygen logger via the PyroWorkbench provided by the manufacturer.
 See (LINKLINK)[TOHERE]

 2. Close PyroScience Software. This is necessary as only 1 software connection to the hardware is possible.

### Start AquaOxyLog

 3.  Create a settings file: Find the index.html file in /settinggui file out and press download. Place the "downloaded" file in the /lib folder, replace the existing one.

 4. Run Logger.bat

 5. Check file at LOC and see graphs at LOC2

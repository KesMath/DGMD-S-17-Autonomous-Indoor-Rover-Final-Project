# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
#
# SPDX-License-Identifier: MIT

from math import floor
from adafruit_rplidar import RPLidar

# Setup the RPLidar
PORT_NAME = "/dev/ttyUSB0"
lidar = RPLidar(None, PORT_NAME, timeout=3)

lidar.connect()

try:
    for scan in lidar.iter_scans():        
        for (_, angle, distance) in scan:
            #scan_data[min([359, floor(angle)])] = distance
            print(angle, distance)
        #process_data(scan_data)
        
except KeyboardInterrupt:
    #print("Stopping.")
    lidar.stop()
    lidar.stop_motor()
    
#lidar.disconnect()


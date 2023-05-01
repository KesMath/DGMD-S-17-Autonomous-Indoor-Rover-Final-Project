import time
import numpy as np
from adafruit_rplidar import RPLidar


def scan_enclosure() -> np.ndarray:
    """
    takes a 25 sec sampling of NxN sq ft enclosure
    and persist angle and distance data as a numpy array 
    """
    # setup connection to device
    SAMPLING_TIME = 25
    PORT_NAME = "/dev/ttyUSB0"
    lidar = RPLidar(None, PORT_NAME)
    lidar.connect()

    sensor_data = np.empty()

    # iterating for 20 sec and persisting lidar reading to 2D array
    t_end = time.time() + SAMPLING_TIME
    while time.time() < t_end:
        for scan in lidar.iter_scans():       
            for (_, angle, distance) in scan:
                sensor_data.append([angle, distance])

    # disconnecting resources
    lidar.stop()
    lidar.stop_motor()
    return sensor_data

if __name__ == '__main__':
    print(scan_enclosure())
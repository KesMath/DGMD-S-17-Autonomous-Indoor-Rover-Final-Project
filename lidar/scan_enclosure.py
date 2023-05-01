import time
import pandas as pd
from adafruit_rplidar import RPLidar


def scan_enclosure() -> pd.DataFrame:
    """
    takes a 25 sec sampling of NxN sq ft enclosure
    and persist angle and distance data as a pandas dataframe 
    """
    # setup connection to device
    SAMPLING_TIME = 25
    PORT_NAME = "/dev/ttyUSB0"
    lidar = RPLidar(None, PORT_NAME, timeout=3)
    lidar.connect()

    sensor_data = list()
    # iterating for 20 sec and persisting lidar reading to 2D array
    t_end = time.time() + SAMPLING_TIME

    try:
        while time.time() < t_end:
            print("saving lidar data to dataframe...")
            for scan in lidar.iter_scans():      
                for (_, angle, distance) in scan:
                    sensor_data.append([angle, distance])

    except KeyboardInterrupt:
        print("Stopping lidar...")

    # disconnecting resource
    finally:
        print("disconnecting lidar...")
        lidar.stop()
        lidar.stop_motor()
    return pd.DataFrame(sensor_data)

if __name__ == '__main__':
    scan_enclosure()
import time
import pandas as pd
from adafruit_rplidar import RPLidar

class LidarDriver:

    def __init__(self, port_name: str):
        # setup connection to device
        self.lidar = RPLidar(None, port_name, timeout=3)
        self.lidar.connect()

    def scan_enclosure(self) -> pd.DataFrame:
        """
        persists angle and distance data as a pandas dataframe 
        """
        sensor_data = list()

        try:
            for scan in self.lidar.iter_scans():      
                for (_, angle, distance) in scan:
                    sensor_data.append([angle, distance])

        except KeyboardInterrupt:
            print("Stopping lidar...")

        # disconnecting resource
        finally:
            print("disconnecting lidar...")
            self.lidar.stop()
            self.lidar.stop_motor()
        return pd.DataFrame(sensor_data)

    def shutdown(self) -> None:
        if self.lidar.motor_running:
            print("shutting down lidar...")
            self.lidar.stop()
            self.lidar.stop_motor()

if __name__ == '__main__':
    driver = LidarDriver(port_name= "/dev/ttyUSB0")
    driver.scan_enclosure()
    driver.shutdown()
import time
import pandas as pd
from adafruit_rplidar import RPLidar

class LidarDriver:
    def __init__(self, port_name: str):
        # setup connection to device
        self.lidar = RPLidar(None, port_name, timeout=3)
        self.lidar.connect()
        self.sample_df = pd.DataFrame(columns = ['Angle', 'Distance'])

    def scan_enclosure(self):
        """
        persists angle and distance data as a pandas dataframe 
        """

        try:
            for scan in self.lidar.iter_scans():
                print("sampling enclosure...")      
                for (_, angle, distance) in scan:
                    self.sample_df.loc[len(self.sample_df)] = [angle, distance]

        except KeyboardInterrupt:
            print("Stopping lidar...")

        # disconnecting resource
        finally:
            print("disconnecting lidar...")
            self.lidar.stop()
            self.lidar.stop_motor()

    def shutdown(self) -> None:
        if self.lidar.motor_running:
            print("shutting down lidar...")
            self.lidar.stop()
            self.lidar.stop_motor()
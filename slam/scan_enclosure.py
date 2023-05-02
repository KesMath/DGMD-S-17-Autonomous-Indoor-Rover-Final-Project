import time
import pandas as pd
from adafruit_rplidar import RPLidar

class LidarDriver:
    def __init__(self, port_name: str):
        # setup connection to device
        self.lidar = RPLidar(None, port_name, timeout=3)
        self.lidar.connect()

    def scan_enclosure(self, result: dict) -> pd.DataFrame:
        """
        persists angle and distance data as a pandas dataframe 
        """
        sensor_data = list()

        try:
            for scan in self.lidar.iter_scans():
                print("sampling enclosure...")      
                for (_, angle, distance) in scan:
                    sensor_data.append([angle, distance])

        except KeyboardInterrupt:
            print("Stopping lidar...")

        # disconnecting resource
        finally:
            print("disconnecting lidar...")
            self.lidar.stop()
            self.lidar.stop_motor()

        df = pd.DataFrame(sensor_data)    
        return result['Dataframe'] = df

    def shutdown(self) -> None:
        if self.lidar.motor_running:
            print("shutting down lidar...")
            self.lidar.stop()
            self.lidar.stop_motor()
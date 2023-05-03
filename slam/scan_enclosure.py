import datetime
import pandas as pd
from adafruit_rplidar import RPLidar, RPLidarException

class LidarDriver:
    def __init__(self, port_name: str):
        # setup connection to device
        self.lidar = RPLidar(None, port_name, timeout=3)
        self.lidar.connect()
        self.sampling_df = pd.DataFrame(columns = ['Angle', 'Distance'])

    def scan_enclosure(self):
        """
        persists angle and distance data as a pandas dataframe 
        """
        delta = datetime.timedelta(seconds=30)
        stop = datetime.datetime.now() + delta
        while datetime.datetime.now() < stop:
            try:
                for scan in self.lidar.iter_scans():
                    print("sampling enclosure...")      
                    for (_, angle, distance) in scan:
                        self.sampling_df.loc[len(self.sampling_df)] = [angle, distance]

            except KeyboardInterrupt:
                print("Stopping lidar due to keyboard interrupt...")
                break

            except RPLidarException as e:
                print("Stopping lidar due to exception raised: " + str(e))
                # comment out break statement if you want to supress exceptions and continue scanning.
                # Warning!!! - may produce undesireable effects
                break
        
        # disconnecting resource
        self.shutdown()

    def shutdown(self) -> None:
        if self.lidar.motor_running:
            print("shutting down lidar...")
            self.lidar.stop()
            self.lidar.stop_motor()


if __name__ == '__main__':
    driver = LidarDriver(port_name= "/dev/ttyUSB0")
    driver.scan_enclosure()
    print(driver.sampling_df)
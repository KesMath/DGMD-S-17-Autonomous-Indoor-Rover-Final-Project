import board
import busio
import adafruit_adxl34x

### REFERENCES ###
#https://pimylifeup.com/raspberry-pi-accelerometer-adxl345/
#https://www.youtube.com/watch?v=QH1umP-duik

#set i2c
i2c = busio.I2C(board.SCL, board.SDA)

#create accelerometer object
accelerometer = adafruit_adxl34x.ADXL345(i2c)

#print out data from accelerometer
while True:
    print("%f %f %f"%accelerometer.acceleration)
    time.sleep(1)

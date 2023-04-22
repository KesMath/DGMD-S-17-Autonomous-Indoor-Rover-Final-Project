import time
import RPi.GPIO as GPIO

# Refer to L298 Motor Driver Documentation: https://www.electroduino.com/introduction-to-l298n-motor-driver-how-its-work/

# Pins for Direction Control
# Refer to https://docs.viam.com/try-viam/rover-resources/rover-tutorial/ to determine Raspberry Pi Pin Mapping! 
INPUT_PIN_1_MOTOR_A = 11
INPUT_PIN_2_MOTOR_A = 13

INPUT_PIN_3_MOTOR_B = 16
INPUT_PIN_4_MOTOR_B = 18

# Pins for Speed Control
MOTOR_A_SPEED_ENABLE = 15
MOTOR_B_SPEED_ENABLE = 22

FREQUENCY = 100 # is the number of times per second that a pulse is generated.
DUTY_CYLCE = 50 # is the percentage of time between pulses that the signal is “high” or “On”.

class MotorDriver:
    def __init__(self):

        # Uses pin numbers not GPIO numbers. Refer to Wiring diagram https://docs.viam.com/try-viam/rover-resources/rover-tutorial/ which illustrates pin numbering being used
        GPIO.setmode(GPIO.BOARD)
        # setup all pins as output
        GPIO.setup(INPUT_PIN_1_MOTOR_A, GPIO.OUT)
        GPIO.setup(INPUT_PIN_2_MOTOR_A, GPIO.OUT)

        GPIO.setup(INPUT_PIN_3_MOTOR_B, GPIO.OUT)
        GPIO.setup(INPUT_PIN_4_MOTOR_B, GPIO.OUT)
        GPIO.setup(MOTOR_A_SPEED_ENABLE, GPIO.OUT)
        GPIO.setup(MOTOR_B_SPEED_ENABLE, GPIO.OUT)

        # Reference on Pulse Width Modulation (PWM): https://raspi.tv/2013/rpi-gpio-0-5-2a-now-has-software-pwm-how-to-use-it
        self.p1 = GPIO.PWM(MOTOR_A_SPEED_ENABLE, FREQUENCY)
        self.p2 = GPIO.PWM(MOTOR_B_SPEED_ENABLE, FREQUENCY)

        self.p1.start(DUTY_CYLCE) # 50% power for motor 1
        self.p2.start(DUTY_CYLCE) # 50% power for motor 2

        def get_motor1():
            return self.p1

        def get_motor2():
            return self.p2
        
        # Refer to table here for HIGH/LOW combinations <-> movement: https://lastminuteengineers.com/l298n-dc-stepper-driver-arduino-tutorial/
        def move_rover_forward(self) -> None:
            GPIO.output(INPUT_PIN_1_MOTOR_A, GPIO.HIGH)
            GPIO.output(INPUT_PIN_2_MOTOR_A, GPIO.LOW)

            GPIO.output(INPUT_PIN_3_MOTOR_B, GPIO.HIGH)
            GPIO.output(INPUT_PIN_4_MOTOR_B, GPIO.LOW)

        def move_rover_backward(self) -> None:
            GPIO.output(INPUT_PIN_1_MOTOR_A, GPIO.LOW)
            GPIO.output(INPUT_PIN_2_MOTOR_A, GPIO.HIGH)

            GPIO.output(INPUT_PIN_3_MOTOR_B, GPIO.LOW)
            GPIO.output(INPUT_PIN_4_MOTOR_B, GPIO.HIGH)



def main():
    m = MotorDriver()
    try:
        while True:
            m.move_rover_forward()
            time.sleep(10)
            m.move_rover_backward()
            time.sleep(10)
            
    except KeyboardInterrupt:
        print("keyboard interupt detected...")
        pass
    finally:
        print("stopping pwm on both motors...")
        m.get_motor1().stop()
        m.get_motor2().stop()
        print("gpio cleanup...")
        GPIO.cleanup()
    
if __name__ == '__main__':
    main()
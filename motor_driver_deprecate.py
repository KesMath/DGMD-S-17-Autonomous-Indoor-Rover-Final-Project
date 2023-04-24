import time
import RPi.GPIO as GPIO
from typing import Final

# Refer to L298 Motor Driver Documentation: https://www.electroduino.com/introduction-to-l298n-motor-driver-how-its-work/

# Pins for Direction Control
# Refer to https://docs.viam.com/try-viam/rover-resources/rover-tutorial/ to determine Raspberry Pi Pin Mapping! 
INPUT_PIN_1_MOTOR_A: Final[int] = 11
INPUT_PIN_2_MOTOR_A: Final[int] = 13

INPUT_PIN_3_MOTOR_B: Final[int] = 16
INPUT_PIN_4_MOTOR_B: Final[int] = 18

# Pins for Speed Control
MOTOR_A_SPEED_ENABLE: Final[int] = 15
MOTOR_B_SPEED_ENABLE: Final[int] = 22

# Pins for Encoder Reading
MOTOR_ENCODER_LEFT: Final[int] = 35
MOTOR_ENCODER_RIGHT: Final[int] = 37


FREQUENCY: Final[int] = 100 # is the number of times per second that a pulse is generated.
DUTY_CYLCE: Final[int] = 50 # is the percentage of time between pulses that the signal is “high” or “On”.

####### WARNING!! - VALUE HERE IS DEPENDENT ON FREQ=100/DUTY_CYCLE=50 #######
MILLESECOND_DELAY_FOR_1_FOOT_TRAVEL: Final[float] = 0.00200 # experimentally timed milleseconds needed for rover to travel 1 foot

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

        GPIO.setup(MOTOR_ENCODER_LEFT, GPIO.IN)
        GPIO.setup(MOTOR_ENCODER_RIGHT, GPIO.IN)        

        # Reference on Pulse Width Modulation (PWM): https://raspi.tv/2013/rpi-gpio-0-5-2a-now-has-software-pwm-how-to-use-it
        self.p1 = GPIO.PWM(MOTOR_A_SPEED_ENABLE, FREQUENCY)
        self.p2 = GPIO.PWM(MOTOR_B_SPEED_ENABLE, FREQUENCY)

        self.p1.start(DUTY_CYLCE) # 50% power for motor 1
        self.p2.start(DUTY_CYLCE) # 50% power for motor 2

    def get_motor1(self):
        return self.p1

    def get_motor2(self):
        return self.p2

    def stop_pwm_on_both_motors(self):
        self.p1.stop() # stop PWM output
        self.p2.stop() # stop PWM output
        
    # Refer to table here for HIGH/LOW combinations <-> movement: https://lastminuteengineers.com/l298n-dc-stepper-driver-arduino-tutorial/
    def __move_rover_forward(self) -> None:
        GPIO.output(INPUT_PIN_1_MOTOR_A, GPIO.HIGH)
        GPIO.output(INPUT_PIN_2_MOTOR_A, GPIO.LOW)

        GPIO.output(INPUT_PIN_3_MOTOR_B, GPIO.HIGH)
        GPIO.output(INPUT_PIN_4_MOTOR_B, GPIO.LOW)

    def __move_rover_backward(self) -> None:
        GPIO.output(INPUT_PIN_1_MOTOR_A, GPIO.LOW)
        GPIO.output(INPUT_PIN_2_MOTOR_A, GPIO.HIGH)

        GPIO.output(INPUT_PIN_3_MOTOR_B, GPIO.LOW)
        GPIO.output(INPUT_PIN_4_MOTOR_B, GPIO.HIGH)

    def rotate_left(self) -> None:
        GPIO.output(INPUT_PIN_1_MOTOR_A, GPIO.HIGH)
        GPIO.output(INPUT_PIN_2_MOTOR_A, GPIO.LOW)

        GPIO.output(INPUT_PIN_3_MOTOR_B, GPIO.LOW)
        GPIO.output(INPUT_PIN_4_MOTOR_B, GPIO.HIGH)
    
    def pivot_left_90_deg(self) -> None:
        # turn left until number of ticks reached
        while True:
            self.rotate_left()
            break
        self.stop_pwm_on_both_motors()

    def pivot_right_90_deg(self) -> None:
        pass


    def move_forward_1_foot(self) -> None:
        # move fwd until number of ticks reached
        while True:
            self.__move_rover_forward()
            break
        self.stop_pwm_on_both_motors()


    def move_right_1_foot(self) -> None:
        self.pivot_right_90_deg()
        self.move_forward_1_foot()
    
    def move_left_1_foot(self) -> None:
        self.pivot_left_90_deg()
        self.move_forward_1_foot()


def main():
#######################
# ENCODER
    GPIO.setup(MOTOR_ENCODER_LEFT, GPIO.IN)
    GPIO.setup(MOTOR_ENCODER_RIGHT, GPIO.IN)

    # reads initial state of encoder pin   
    init = GPIO.input(MOTOR_ENCODER_LEFT)
    cout = 0
    try:
        while True:
            # a pulse change has occurred if value discrepancy occurred
            if GPIO.input(MOTOR_ENCODER_LEFT) != init:
                cout +=1
                print("position : " + cout)

    except KeyboardInterrupt:
        print("keyboard interupt detected...")
        pass
    finally:
        print("gpio cleanup...")
        GPIO.cleanup()

###################################
# ROTATION
    #motor = MotorDriver()
    #motor.rotate_left()
    #GPIO.cleanup()

###################################
# GENERAL DRIVE TEST
    # try:
    #     while True:
    #         m.move_rover_forward()
    #         time.sleep(10)
    #         m.move_rover_backward()
    #         time.sleep(10)
            
    # except KeyboardInterrupt:
    #     print("keyboard interupt detected...")
    #     pass
    # finally:
    #     print("stopping pwm on both motors...")
    #     m.get_motor1().stop()
    #     m.get_motor2().stop()
    #     print("gpio cleanup...")
    #     GPIO.cleanup()
    
if __name__ == '__main__':
    main()
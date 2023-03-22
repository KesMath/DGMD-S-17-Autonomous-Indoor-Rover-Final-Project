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

# Uses pin numbers not GPIO numbers. Refer to Wiring diagram in above url which illustrates pin numbering being used
def setup() -> None:
    GPIO.setmode(GPIO.BOARD)
    # setup all pins as output
    GPIO.setup(INPUT_PIN_1_MOTOR_A, GPIO.OUT)
    GPIO.setup(INPUT_PIN_2_MOTOR_A, GPIO.OUT)

    GPIO.setup(INPUT_PIN_3_MOTOR_B, GPIO.OUT)
    GPIO.setup(INPUT_PIN_4_MOTOR_B, GPIO.OUT)
    GPIO.setup(MOTOR_A_SPEED_ENABLE, GPIO.OUT)
    GPIO.setup(MOTOR_B_SPEED_ENABLE, GPIO.OUT)
    p = GPIO.PWM(MOTOR_A_SPEED_ENABLE, 100)
    p.start(50)

# Refer to table here for HIGH/LOW combinations <-> movement: https://lastminuteengineers.com/l298n-dc-stepper-driver-arduino-tutorial/
def motor_off() -> None:
    GPIO.output(INPUT_PIN_1_MOTOR_A, GPIO.LOW)
    GPIO.output(INPUT_PIN_2_MOTOR_A, GPIO.LOW)
    GPIO.output(INPUT_PIN_3_MOTOR_B, GPIO.LOW)
    GPIO.output(INPUT_PIN_4_MOTOR_B, GPIO.LOW)

def move_rover_forward() -> None:
    GPIO.output(INPUT_PIN_1_MOTOR_A, GPIO.HIGH)
    GPIO.output(INPUT_PIN_2_MOTOR_A, GPIO.LOW)

    GPIO.output(INPUT_PIN_3_MOTOR_B, GPIO.HIGH)
    GPIO.output(INPUT_PIN_4_MOTOR_B, GPIO.LOW)


def main():
    print("setting up board...")
    while True:
        move_rover_forward()
        time.sleep(10)

    p.ChangeDutyCycle(0)
    print("turning off motors ...")
    motor_off()
    print("gpio cleanup...")
    GPIO.cleanup()
    
if __name__ == '__main__':
    main()
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
print("setting up board...")
GPIO.setmode(GPIO.BOARD)
# setup all pins as output
GPIO.setup(INPUT_PIN_1_MOTOR_A, GPIO.OUT)
GPIO.setup(INPUT_PIN_2_MOTOR_A, GPIO.OUT)

GPIO.setup(INPUT_PIN_3_MOTOR_B, GPIO.OUT)
GPIO.setup(INPUT_PIN_4_MOTOR_B, GPIO.OUT)
GPIO.setup(MOTOR_A_SPEED_ENABLE, GPIO.OUT)
GPIO.setup(MOTOR_B_SPEED_ENABLE, GPIO.OUT)

# Reference on Pulse Width Modulation (PWM): https://raspi.tv/2013/rpi-gpio-0-5-2a-now-has-software-pwm-how-to-use-it
p1 = GPIO.PWM(MOTOR_A_SPEED_ENABLE, 100)
p2 = GPIO.PWM(MOTOR_B_SPEED_ENABLE, 100)
p1.start(50) # 50% duty cycle or 50% power for motor 1
p2.start(50) # 50% duty cycle or 50% power for motor 2

# Refer to table here for HIGH/LOW combinations <-> movement: https://lastminuteengineers.com/l298n-dc-stepper-driver-arduino-tutorial/
def move_rover_forward() -> None:
    GPIO.output(INPUT_PIN_1_MOTOR_A, GPIO.HIGH)
    GPIO.output(INPUT_PIN_2_MOTOR_A, GPIO.LOW)

    GPIO.output(INPUT_PIN_3_MOTOR_B, GPIO.HIGH)
    GPIO.output(INPUT_PIN_4_MOTOR_B, GPIO.LOW)

def move_rover_backward() -> None:
    GPIO.output(INPUT_PIN_1_MOTOR_A, GPIO.LOW)
    GPIO.output(INPUT_PIN_2_MOTOR_A, GPIO.HIGH)

    GPIO.output(INPUT_PIN_3_MOTOR_B, GPIO.LOW)
    GPIO.output(INPUT_PIN_4_MOTOR_B, GPIO.HIGH)

# Good video tutorial: https://www.youtube.com/watch?v=Qp4wNdyC2Z0
# Rover goes forward for 10 sec then drives back for 10 sec
def main():
    try:
        while True:
            move_rover_forward()
            time.sleep(10)
            move_rover_backward()
            time.sleep(10)
            
    except KeyboardInterrupt:
        print("keyboard interupt detected...")
        pass
    finally:
        print("stopping pwm on both motors...")
        p1.stop()
        p2.stop()
        print("gpio cleanup...")
        GPIO.cleanup()
    
if __name__ == '__main__':
    main()
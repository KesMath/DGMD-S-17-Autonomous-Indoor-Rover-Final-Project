import time
from gpiozero import Motor

# Refer to L298 Motor Driver Documentation: https://www.electroduino.com/introduction-to-l298n-motor-driver-how-its-work/

# Pins for Rotating Direction
# Refer to https://docs.viam.com/try-viam/rover-resources/rover-tutorial/ to determine Raspberry Pi Pin Mapping! 
INPUT_PIN_1_MOTOR_A = 11
INPUT_PIN_2_MOTOR_A = 13

INPUT_PIN_3_MOTOR_B = 16
INPUT_PIN_4_MOTOR_B = 18

# Pins for Speed Control
MOTOR_A_SPEED = 15
MOTOR_B_SPEED = 22

MOTOR1_PINS = (INPUT_PIN_1_MOTOR_A, INPUT_PIN_2_MOTOR_A)
MOTOR2_PINS = (INPUT_PIN_3_MOTOR_B, INPUT_PIN_4_MOTOR_B)

# Refer to this document https://gpiozero.readthedocs.io/en/stable/api_output.html?gpiozero.Motor
motor1 = Motor(forward=MOTOR1_PINS[0], backward=MOTOR1_PINS[1])
motor2 = Motor(forward=MOTOR2_PINS[0], backward=MOTOR2_PINS[1])


def speed_check(speed) -> bool:
    return speed >= 0 and speed <= 1

def move_rover_forward(speed) -> None:
    if speed_check:
        print("motor1 moving fwd...")
        motor1.forward(speed)
        print("motor2 moving fwd...")
        motor2.forward(speed)

def move_rover_backward(speed) -> None:
    if speed_check:
        print("motor1 moving backward...")
        motor1.backward(speed)
        print("motor2 moving backward...")
        motor2.backward(speed)

# For testing purposes only! 
# At production level, we can leverage "from gpiozero import Robot" to control 2 motors simultaneously!!
def main():
    # half speed forward, pause, then half speed backwards
    print("moving fwd...")
    move_rover_forward(0.5)
    print("sleeping for 5 secs ...")
    time.sleep(5)
    print("moving backwards...")
    move_rover_backward(0.5)
    print("stopping motors...")
    motor1.stop()
    motor2.stop()

    # full speed forward, pause, then full speed backwards
    #move_rover_forward(1)
    #time.sleep(5)
    #move_rover_backward(1)

if __name__ == '__main__':
    main()
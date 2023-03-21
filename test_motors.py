import time
from gpiozero import Motor

# Refer to https://docs.viam.com/try-viam/rover-resources/rover-tutorial/ for pin layout
MOTOR1_PINS = (, )
MOTOR2_PINS = (, )

# Refer to this document https://gpiozero.readthedocs.io/en/stable/api_output.html?gpiozero.Motor
motor1 = Motor(forward=MOTOR1_PINS[0], backward=MOTOR1_PINS[1])
motor2 = Motor(forward=MOTOR2_PINS[0], backward=MOTOR2_PINS[1])


def speed_check(speed) -> bool:
    return speed >= 0 and speed <= 1

def move_rover_forward(speed) -> None:
    if speed_check:
        motor1.forward(speed)
        motor2.forward(speed)

def move_rover_backward(speed) -> None:
    if speed_check:
        motor1.forward(speed)
        motor2.forward(speed)


# For testing purposes only! 
# At production level, we can leverage "from gpiozero import Robot" to control 2 motors simultaneously!!
def main():
    # half speed forward, pause, then half speed backwards
    move_rover_forward(0.5)
    time.sleep(5)
    move_rover_backward(0.5)

    # full speed forward, pause, then full speed backwards
    move_rover_forward(1)
    time.sleep(5)
    move_rover_backward(1)

if __name__ == '__main__':
    main()
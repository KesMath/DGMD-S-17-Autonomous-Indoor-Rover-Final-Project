import asyncio

from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions
from viam.components.base import Base


async def connect():
    creds = Credentials(
        type='robot-location-secret',
        payload='xhp2wcnjiej2m5kstyh2kmvrkx4q5yan60cncyamc61uvsed')
    opts = RobotClient.Options(
        refresh_interval=0,
        dial_options=DialOptions(credentials=creds)
    )
    return await RobotClient.at_address('kes-rover-main.0ltqp6fjer.viam.cloud', opts)

async def move_forward_1_foot(base):
    # Moves the Viam Rover forward 625mm at 625mm/s
    await base.move_straight(velocity=625, distance=625)
    print("move straight")


async def spin_left_90_degrees(base):
    # Spins the Viam Rover 90 degrees at 100 degrees per second
    # Experimentally, I had to reduce by 10 degrees since 90 deg was overshot
    await base.spin(velocity=100, angle=80)
    print("spin left 90 degrees")

async def spin_right_90_degrees(base):
    # Spins the Viam Rover 90 degrees at 100 degrees per second
    # Experimentally, I had to reduce by 10 degrees since 90 deg was overshot
    await base.spin(velocity=100, angle=-80)
    print("spin right 90 degrees")

async def main():
    robot = await connect()

    #print('Resources:')
    #print(robot.resource_names)
    
    # Get the base component from the Viam Rover
    roverBase = Base.from_robot(robot, 'viam_base')

    await move_forward_1_foot(roverBase)

    # Don't forget to close the robot when you're done!
    await robot.close()

if __name__ == '__main__':
    asyncio.run(main())

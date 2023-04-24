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

async def moveInSquare(base):
    for _ in range(4):
        # moves the Viam Rover forward 500mm at 500mm/s
        await base.move_straight(velocity=500, distance=500)
        print("move straight")
        # spins the Viam Rover 90 degrees at 100 degrees per second
        await base.spin(velocity=100, angle=90)
        print("spin 90 degrees")

async def main():
    robot = await connect()

    print('Resources:')
    print(robot.resource_names)
    
    # Get the base component from the Viam Rover
    roverBase = Base.from_robot(robot, 'viam_base')

    # Move the Viam Rover in a square
    await moveInSquare(roverBase)

    # Don't forget to close the robot when you're done!
    await robot.close()

if __name__ == '__main__':
    asyncio.run(main())

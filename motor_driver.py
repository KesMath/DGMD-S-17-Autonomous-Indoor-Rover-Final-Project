import time
import asyncio

from viam.components.base import Base
from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions

#from path_planning import *

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
    print("moving straight")
    await base.move_straight(velocity=625, distance=625)

async def move_backward_1_foot(base):
    # Moves the Viam Rover backward 625mm at 625mm/s
    print("moving backward")
    await base.move_straight(velocity=-625, distance=515)

async def spin_left_90_degrees(base):
    # Spins the Viam Rover 90 degrees at 100 degrees per second
    # Experimentally, I had to reduce by 10 degrees since 90 deg was overshot
    print("spinning left 90 degrees")
    await base.spin(velocity=100, angle=80)

async def spin_right_90_degrees(base):
    # Spins the Viam Rover 90 degrees at 100 degrees per second
    # Experimentally, I had to reduce by 10 degrees since 90 deg was overshot
    print("spinning right 90 degrees")
    await base.spin(velocity=100, angle=-80)

async def drive_right_1_foot(base):
    await spin_right_90_degrees(base)
    time.sleep(1)
    await move_forward_1_foot(base)
    time.sleep(1)
    # re-centers rover forward
    await spin_left_90_degrees(base)

async def drive_left_1_foot(base):
    await spin_left_90_degrees(base)
    time.sleep(1)
    await move_forward_1_foot(base)
    time.sleep(1)
    # re-centers rover forward
    await spin_right_90_degrees(base)

async def drive_to_next_tile(base, current_point: tuple, new_coordinate_pt: tuple):
    # drive forward
    if new_coordinate_pt[0] == current_point[0] - 1  and new_coordinate_pt[1] == current_point[1]:
        await move_forward_1_foot(base)

    # drive to left tile
    elif new_coordinate_pt[0] == current_point[0] - 1:
        await drive_left_1_foot(base)

    # drive to right tile
    elif new_coordinate_pt[1] == current_point[1] + 1:
        await drive_right_1_foot(base)
   
    # drive backward
    elif new_coordinate_pt[0] == current_point[0] + 1  and new_coordinate_pt[1] == current_point[1]:
        await move_backward_1_foot(base)

async def main():
    print("connecting to robot...")
    robot = await connect()
    start_point = (4,0)
    # Get the base component from the Viam Rover
    roverBase = Base.from_robot(robot, 'viam_base')

    await move_backward_1_foot(roverBase)

    ############# TODO: fix import issue ######################
    # shortest_path = return_shortest_path(start_point = start_point, goal_point = (0,4), width = GRID_WIDTH, height = GRID_HEIGHT, gridmap= EMPTY_GRID, resolution = STEP_COST)
    # del shortest_path[0] # remove current point

    # if shortest_path is not None:
    #     for node in shortest_path:
    #         next_point = node.get_coordinate_pt()
    #         print("driving to :" + next_point)
    #         await drive_to_next_tile(base = robot, current_point = start_point, new_coordinate_pt = next_point)
    #         time.sleep(2)
    #         # need to update starting point since robot moved to a new position
    #         start_point = next_point
    # else:
    #     print("Rover unable to find shortest path... ")
    ##########################################################


    ############# NOTE: due to import issue above and time constraints, need to mock shortest path for DEMO purposes ######################
    # shortest_path = [(4,0), (4,1), (4,2), (4,3), (4,4), (3,4), (2,4), (1,4), (0,4)]
    # del shortest_path[0] # remove current point

    # if shortest_path is not None:
    #     for point in shortest_path:
    #         next_point = point
    #         print("driving to :" + str(next_point))
    #         await drive_to_next_tile(base = roverBase, current_point = start_point, new_coordinate_pt = next_point)
    #         time.sleep(5)
    #         # need to update starting point since robot moved to a new position
    #         start_point = next_point
    
    # else:
    #     print("Rover unable to find shortest path... ")

    # close server connection
    print("closing connection to robot...")
    await robot.close()

if __name__ == '__main__':
    asyncio.run(main())

## :robot:Developing an Autonomous Reconnaissance Robot Used to Navigate Indoor Spaces Using LiDAR based SLAM and Subsequently Stream and Persist Live Video Stream To the Cloud:robot:

## Group Members
Kesler Mathieu, Hung Tran, Ameera Zamani Iftekhar, Maggie Lau

## Type of Project
Engineering - Graduate Level


## Summary
The goal at hand is to create a rover that can be deployed in an unknown indoor environment, autonomously navigate while capturing video feed, and subsequently return to its starting position. The central technique known as SLAM will allow the rover to concurrently map and locate itself in a newfound floorspace. This will subsequently be paired with path planning algorithms so the vehicle can efficiently navigate such space while reducing collisions, henceforth achieving a level of autonomy sufficient enough for indoor exploration. 

## Introduction
In certain hostile environments, first responders have to navigate through unknown zones that can lead to their demise if the area isn’t canvassed beforehand. To provide some context, first responders scenarios can range from police officers trying to deescalate hostage situations to firefighters performing disaster relief efforts after the onset of a hurricane and even military personnel commandeering battlefield strongholds from enemy possession. According to the National Institute of Science and Technology, over 83,000 firefighter related injuries (which totaled to $11.8B in 2005) are due to the lack of real-time analytics that can give first responders critical insight into a building’s deteriorating infrastructure. A viable solution is for first responders to deploy a lightweight, rugged chassis rover that has a relatively small form factor and is certainly cost effective, from a sensor standpoint, to perform reconnaissance and return back to its starting point for retrieval/collection. Autonomous navigation will be subsequently paired with live streaming video to a remote server so that operators can analyze and give further command to ground-level constituents.
Autonomous navigation is not a trivial feat given that a machine must skillfully make its way around an environment that it has no prior context to. Given this fact, we will be leveraging as many off-the-shelf libraries/components to expedite the development of our use case. The challenge here lies with harnessing datasets from our amalgamation of sensors (LiDAR, 3-axis accelerometer, wheel encoder)  to fit our business case. We define the measure of success by showcasing the rover is able to navigate within a confined space containing fixed obstacles that it circumvents and return back to the starting point. We'll run a series of trials with randomized obstacles and starting points to measure the effectiveness of our implementation.


## Background
Simultaneous Localization and Mapping or SLAM is concerned with the objective of creating a map of an unknown environment while the rover must simultaneously ascertain its location in that space. In order for SLAM to work, it requires as input a set of distance points from the rover to a nearby object. There are a number of physical sensors that can accomplish this task but one common approach is to leverage a LiDAR sensor. A LiDAR sensor essentially works by shooting a beam of light from an internal emitter to an outbound target. The light beam returns to the LiDAR assembly, specifically the receiver, and its elapsed time is measured. Using the distance formula, we can intuitively calculate the distance from the assembly to an outbound target. LiDAR is an excellent choice for SLAM algorithms to generate a high fidelity map as certain models can sample the environment as much as 8,000 times per second!
From a mapping perspective, using LiDAR to establish a point cloud of all neighboring objects at a fixed distance sounds intuitive enough but that alone doesn’t touch on the topic of localization. Fortunately, LiDAR-Based SLAM can be interfaced with wheel odometry, which measures distance traveled at the wheel, along with accelerometers & gyroscope sensors to mathematically model its location based on initial starting conditions. With its environment mapped out, the final step to reach a level of autonomy has to deal with path planning. There are a number of path planning algorithms (e.g. Dijkstra, A* Search, & Rapidly Exploring Random Tree) that essentially try to solve the same task: to find the shortest path in the form of a continuous sequence of non-blocking points that leads to its goal destination while avoiding points along that path that are deemed or marked as obstacles. Taken in conjunction, we get an overview of how autonomous navigation can generally be achieved - perception through SLAM coupled with classical shortest path algorithms.

## GitHub Directory Description
```lidar/scan1.py```: script to run a LiDAR scan  
```lidar/start1.py```: script to connect to LiDAR   
```lidar/stop1.py```: script to stop LiDAR  
```path_planning/dijkstra_path_planner.py```: implementation of dijkstra's algorithm for shortest path creation  
```path_planning/grid_maps.py```: file with grid maps to be loaded into path planner  
```path_planning/test_dijkstra_path_planner.py```: unit test suite to test dijkstra's algorithm implementation upon different occupancy grid scenarios  
```slam/lidar_data_01.csv:``` file of data from LiDAR scan  
```slam/map.py```: script to create point cloud map  
```slam/OccupancyMap-2.ipynb```: notebook to create occupany grid  
```slam/sampling_10.csv```: data to create occupancy grid  
```motor_driver.py```: entry point file - contains business logic that ties path planner to discrete rover movements (i.e. left, right, forward, backward) using VIAM SDK   


## Demo
<a><img src="media/Sample_Drive_For_Video_Deliverable.gif" width="400" height="300"></a>

## Run Command to Drive Rover: `python motor_driver.py`
```
pi@headlesspi:~/DGMD-S-17-Autonomous-Indoor-Rover-Final-Project $ python motor_driver.py
Enter the goal point as x y: 0 4
connecting rover to Viam server...
2023-04-27 22:31:55,166		INFO	viam.rpc.dial (dial.py:209)	Connecting to socket: /tmp/proxy-64D4HUGj.sock
calculating shortest path...
driving to :(4, 1)
spinning right 90 degrees
moving straight
spinning left 90 degrees
driving to :(4, 2)
spinning right 90 degrees
moving straight
spinning left 90 degrees
driving to :(4, 3)
spinning right 90 degrees
moving straight
spinning left 90 degrees
driving to :(4, 4)
spinning right 90 degrees
moving straight
spinning left 90 degrees
driving to :(3, 4)
moving straight
driving to :(2, 4)
moving straight
driving to :(1, 4)
moving straight
driving to :(0, 4)
moving straight
closing client connection to Viam server...
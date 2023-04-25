## :robot:Developing an Autonomous Reconnaissance Robot Used to Navigate Indoor Spaces Using LiDAR based SLAM and Subsequently Stream and Persist Live Video Stream To the Cloud:robot:

## Group Members
Kesler Mathieu, Hung Tran, Ameera Zamani Iftekhar, Maggie Lau

## Type of Project
Engineering - Graduate Level

## Detailed Reference
[Proposal Doc](https://docs.google.com/document/d/1DPl8a1aFSLdDcSO5HPQ68z0GHqil6a57udiRcfCY16c/edit)

## Summary
The goal at hand is to create a rover that can be deployed in an unknown indoor environment, autonomously navigate while capturing video feed, and subsequently return to its starting position. The central technique known as SLAM will allow the rover to concurrently map and locate itself in a newfound floorspace. This will subsequently be paired with path planning algorithms so the vehicle can efficiently navigate such space while reducing collisions, henceforth achieving a level of autonomy sufficient enough for indoor exploration. 

## Introduction
In certain hostile environments, first responders have to navigate through unknown zones that can lead to their demise if the area isn’t canvassed beforehand. To provide some context, first responders scenarios can range from police officers trying to deescalate hostage situations to firefighters performing disaster relief efforts after the onset of a hurricane and even military personnel commandeering battlefield strongholds from enemy possession. According to the National Institute of Science and Technology, over 83,000 firefighter related injuries (which totaled to $11.8B in 2005) are due to the lack of real-time analytics that can give first responders critical insight into a building’s deteriorating infrastructure. A viable solution is for first responders to deploy a lightweight, rugged chassis rover that has a relatively small form factor and is certainly cost effective, from a sensor standpoint, to perform reconnaissance and return back to its starting point for retrieval/collection. Autonomous navigation will be subsequently paired with live streaming video to a remote server so that operators can analyze and give further command to ground-level constituents.
Autonomous navigation is not a trivial feat given that a machine must skillfully make its way around an environment that it has no prior context to. Given this fact, we will be leveraging as many off-the-shelf libraries/components to expedite the development of our use case. The challenge here lies with harnessing datasets from our amalgamation of sensors (LiDAR, 3-axis accelerometer, wheel encoder)  to fit our business case. We define the measure of success by showcasing the rover is able to navigate within a confined space containing fixed obstacles that it circumvents and return back to the starting point. We'll run a series of trials with randomized obstacles and starting points to measure the effectiveness of our implementation.


## Background
Simultaneous Localization and Mapping or SLAM is concerned with the objective of creating a map of an unknown environment while the rover must simultaneously ascertain its location in that space. In order for SLAM to work, it requires as input a set of distance points from the rover to a nearby object. There are a number of physical sensors that can accomplish this task but one common approach is to leverage a LiDAR sensor. A LiDAR sensor essentially works by shooting a beam of light from an internal emitter to an outbound target. The light beam returns to the LiDAR assembly, specifically the receiver, and its elapsed time is measured. Using the distance formula, we can intuitively calculate the distance from the assembly to an outbound target. LiDAR is an excellent choice for SLAM algorithms to generate a high fidelity map as certain models can sample the environment as much as 8,000 times per second!
From a mapping perspective, using LiDAR to establish a point cloud of all neighboring objects at a fixed distance sounds intuitive enough but that alone doesn’t touch on the topic of localization. Fortunately, LiDAR-Based SLAM can be interfaced with wheel odometry, which measures distance traveled at the wheel, along with accelerometers & gyroscope sensors to mathematically model its location based on initial starting conditions. With its environment mapped out, the final step to reach a level of autonomy has to deal with path planning. There are a number of path planning algorithms (e.g. Dijkstra, A* Search, & Rapidly Exploring Random Tree) that essentially try to solve the same task: to find the shortest path in the form of a continuous sequence of non-blocking points that leads to its goal destination while avoiding points along that path that are deemed or marked as obstacles. Taken in conjunction, we get an overview of how autonomous navigation can generally be achieved - perception through SLAM coupled with classical shortest path algorithms.

## Minimum Viable Product
Run Command to Drive Rover
```
pi@headlesspi:~/DGMD-E-17-Autonomous-Indoor-Rover-Final-Project $ python motor_driver.py
2023-04-24 21:56:25,416		INFO	viam.rpc.dial (dial.py:209)	Connecting to socket: /tmp/proxy-KqmhUfy3.sock
driving to :(4, 1)
spin right 90 degrees
move straight
spin left 90 degrees
driving to :(4, 2)
spin right 90 degrees
move straight
spin left 90 degrees
driving to :(4, 3)
spin right 90 degrees
move straight
spin left 90 degrees
driving to :(4, 4)
spin right 90 degrees
move straight
spin left 90 degrees
driving to :(3, 4)
move straight
driving to :(2, 4)
move straight
driving to :(1, 4)
move straight
driving to :(0, 4)
move straight
```

## had some issues with importing path planner but running unit tests indeed proves it's working



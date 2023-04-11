from typing import List, Optional

class Node:
    def __init__(self, coordinate_pt: tuple, parent) -> None:
        self.parent = parent
        self.coordinate_pt = coordinate_pt

    def get_parent(self):
        return self.parent
    
    def get_coordinate_pt(self) -> tuple:
        return self.coordinate_pt

    def __str__(self):
        return "Node with grid_cost = " + str(self.grid_cost) + " at starting pt: " + str(self.coordinate_pt)




def return_shortest_path(start_point, goal_point, width, height, gridmap, resolution) -> Optional[List[Node]]:
    ''' 
    Constructs shortest path based on Rapidly-Exploring Random Tree (RRT) algorithm search on a costmap with a given start and goal node
    Parameters:
        start_point     (tuple):      starting point on the occupancy grid.
        goal_point      (tuple):      destination point on the occupancy grid.
        width           (int):        grid width (or number of columns), specified as a positive scalar in meters.
        height          (int):        grid height (or number of rows), specified as a positive scalar in meters.
        gridmap         (np.ndarray): 2D array corresponding where [row][col] indices represent a grid square being freed (i.e. binary value = 0) or occupied (i.e. binary value = 1). Value of -1 implies an unscanned areas
        resolution      (float):      side of each grid map square in feet

    Returns:
        shortest_path (List[Nodes]): if destination can be found, else returns None

    Dijkstra's Algorithm can be implemented in 2 phases:
    Phase 1: From a starting point, we incrementally explore other neighboring nodes until the goal_node can be found 
    Phase 2: When goal_node is found, we recursively backtrack to the starting_node, given that each child node's parent attribute is a recursive structure
    '''
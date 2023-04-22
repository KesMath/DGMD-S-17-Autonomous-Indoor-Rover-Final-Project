from node import Node
from typing import List, Optional
from sortedcontainers import SortedKeyList

STEP_COST = 1 # cost incurred when moving to a adjacent cell. We assume each grid cell has a side length of 1
FREE_SPACE = 0
OBSTACLES = 1

def is_within_grid_bounds(n: int, boundary: int) -> bool:
    return n >= 0 and n < boundary  

# Grid Map Reference: https://automaticaddison.com/what-is-an-occupancy-grid-map/
# TODO: CODE CLEANUP: can remove width and height params as this is implicity declared within gridmap dimensions!
def find_neighbours(node: Node, width: int, height: int, gridmap, resolution) -> Optional[List[Node]]:
    ''' 
    Identifies von Neumann neighborhood (i.e. up, down, left, right).
    When motors/MotorController() can perform diagonal turns, neighboring nodes can be at most 8.
    Parameters:
        node:          (Node):       neighboring nodes will be derived from this current node 
        width          (int):        grid width (or number of columns), specified as a positive scalar in meters. A node's X-coordinate value cannot exceed this value!
        height         (int):        grid height (or number of rows), specified as a positive scalar in meters. A node's Y-coordinate value cannot exceed this value!
        gridmap        (np.ndarray): NxN 2D array corresponding where [row][col] indices represent a grid square being freed (i.e. binary value = 0) or occupied (i.e. binary value = 1). Value of -1 implies an unscanned areas
        resolution     (float):      side of each grid map square in feet .. we assume it's equal to STEP_COST for this scenario

    Returns:
        neighbors (List[Nodes]): if neighbors can be found, else returns None
    '''
    assert width == len(gridmap[0])
    assert height == len(gridmap)
    assert width == height

    neighbors = list()
    coordinates = node.get_coordinate_pt()
    LEFT = coordinates[1] - 1
    RIGHT = coordinates[1] + 1
    UP = coordinates[0] - 1
    DOWN = coordinates[0] + 1
    
    # avoid obstacles
    if gridmap[coordinates[0]][coordinates[1]] != OBSTACLES:
        # check left within grid bounds
        if is_within_grid_bounds(LEFT, width):
            if gridmap[coordinates[0]][LEFT] == FREE_SPACE:
                neighbors.append(Node(grid_cost = resolution + node.get_grid_cost(), coordinate_pt = (coordinates[0], LEFT), parent = node))

        # check right within grid bounds
        if is_within_grid_bounds(RIGHT, width):
            if gridmap[coordinates[0]][RIGHT] == FREE_SPACE:
                neighbors.append(Node(grid_cost = resolution + node.get_grid_cost(), coordinate_pt = (coordinates[0], RIGHT), parent = node))

        # check up within grid bounds
        if is_within_grid_bounds(UP, height):
            if gridmap[UP][coordinates[1]] == FREE_SPACE:
                neighbors.append(Node(grid_cost = resolution + node.get_grid_cost(), coordinate_pt = (UP, coordinates[1]), parent = node))

        # check down within grid bounds
        if is_within_grid_bounds(DOWN, height):
            if gridmap[DOWN][coordinates[1]] == FREE_SPACE:
                neighbors.append(Node(grid_cost = resolution + node.get_grid_cost(), coordinate_pt = (DOWN, coordinates[1]), parent = node))

    return neighbors


def return_shortest_path(start_point, goal_point, width, height, gridmap, resolution) -> Optional[List[Node]]:
    ''' 
    Performs Dijkstra's shortest path algorithm search on a costmap with a given start and goal node
    Parameters:
        start_point     (tuple):      starting point on the occupancy grid.
        goal_point      (tuple):      destination point on the occupancy grid.
        width           (int):        grid width (or number of columns), specified as a positive scalar in meters.
        height          (int):        grid height (or number of rows), specified as a positive scalar in meters.
        gridmap         (np.ndarray): 2D array corresponding where [height][width] indices represent a grid square being freed (i.e. binary value = 0) or occupied (i.e. binary value = 1). Value of -1 implies an unscanned areas
        resolution      (float):      side of each grid map square in feet

    Returns:
        shortest_path (List[Nodes]): if destination can be found, else returns None

    Dijkstra's Algorithm can be implemented in 2 phases:
    Phase 1: From a starting point, we incrementally explore other neighboring nodes until the goal_node can be found 
    Phase 2: When goal_node is found, we recursively backtrack to the starting_node, given that each child node's parent attribute is a recursive structure
    '''

    shortest_path = list()
    current_node = None
    path_exists = False
    sort_func = lambda a: a.get_grid_cost()
    unvisited_queue = SortedKeyList(key = sort_func) # means of book-keeping to store list of unvisited nodes. Idealistically we want this to be a SortedSet so our selection favors nodes with minimum grid costs.
    visited_queue = list() # means of book-keeping to store list of visited nodes
    
    # intializing parent node and adding that to the beginning of frontier
    starting_node = Node(grid_cost=0, coordinate_pt=start_point, parent=None)
    unvisited_queue.add(starting_node)

    while(len(unvisited_queue) != 0):
        # remove current node from frontier and declare it as target node to explore
        current_node = unvisited_queue.pop(0)

        # check if current node is goal point
        if current_node.get_coordinate_pt() == goal_point:
            path_exists = True
            break

        # find the neighbors of the current node and add to frontier iff it's a new member to the set ... if it exists within set, re-evaluate smaller g_cost if necessary
        neighbors = find_neighbours(node=current_node, width=width, height=height, gridmap=gridmap, resolution=STEP_COST)
        for neighbor in neighbors:
            if neighbor not in visited_queue:

                # In this case, we've essentially found a shorter route to an unexplored node 
                if neighbor in unvisited_queue:
                    n_index = unvisited_queue.index(neighbor)
                    neighbor_node = unvisited_queue.pop(n_index)
                    

                    if current_node.grid_cost + STEP_COST < neighbor_node.grid_cost:
                        neighbor_node.update_grid_cost(current_node.grid_cost + STEP_COST)
                        neighbor_node.parent = current_node

                    unvisited_queue.add(neighbor_node)

                # add neighbor node to open list since it's first occurrence
                else:
                    unvisited_queue.add(neighbor)

        # add target node to visited
        visited_queue.append(current_node)

    if path_exists:
        # building path by recursive backtracking
        while(current_node != None):
            shortest_path.append(current_node)
            current_node = current_node.parent
        shortest_path.reverse()
        return shortest_path
    return None
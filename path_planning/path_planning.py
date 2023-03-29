from typing import List, Optional
from sortedcontainers import SortedKeyList

class Node:
    def __init__(self, grid_cost: int, parent) -> None:
        self.grid_cost = grid_cost # shortest distance from parent node 
        self.parent = parent
    
    def update_grid_cost(self, val: int) -> None:
        if val >= 0:
            self.grid_cost = val
    
    def get_grid_cost(self) -> int:
        return self.grid_cost

    def get_parent(self):
        return self.parent

    def __str__(self):
        return "Node with grid_cost = " + str(self.grid_cost)
    

# TODO: define explicit types for params below
def return_shortest_path(start_index, goal_index, width, height, costmap, resolution, origin) -> Optional[List[Node]]:
    ''' 
    Performs Dijkstra's shortest path algorithm search on a costmap with a given start and goal node
    Returns: shortest path as List[Nodes] if destination can be found, else returns None 
    '''
    '''
    Dijkstra's Algorithm can be implemented in 2 phases:
    Phase 1: From a starting point, we incrementally explore other neighboring nodes until the goal_node can be found 
    Phase 2: When goal_node is found, we recursively backtrack to the starting_node, given that each child node's parent attribute is a recursive structure
    '''

    shortest_path = list()
    sort_func = lambda a: a.get_grid_cost()
    unvisited_queue = SortedKeyList(key = sort_func) # means of book-keeping to store list of unvisited nodes. Idealistically we want this to be a SortedSet so our selection favors nodes with minimum grid costs.
    visited_queue = list() # means of book-keeping to store list of visited nodes

    
    return shortest_path


def main():
    # TESTING SORTEDLIST with custom KEY!
    node1 = Node(1, None)
    node2 = Node(2, None)
    node3 = Node(3, None)
    l = list()
    l.append(node2)
    l.append(node1)
    l.append(node3)
    ######################
    sort_list = SortedKeyList(key=lambda a: a.get_grid_cost())
    sort_list.add(node2)
    sort_list.add(node1)
    sort_list.add(node3)
    #######################
    for ele in sort_list:
        print(ele)
    for e in l:
        print(e.get_grid_cost())
if __name__ == '__main__':
    main()
class Node:
    def __init__(self, grid_cost: int, parent) -> None:
        self.grid_cost = grid_cost
        self.parent = parent
    
    def update_grid_cost(self, val: int) -> None:
        self.grid_cost = val
    
    def get_grid_cost(self) -> int:
        return self.grid_cost

    def get_parent(self):
        return self.parent
    


def dijkstra(start_index, goal_index, width, height, costmap, resolution, origin):
  ''' 
  Performs Dijkstra's shortest path algorithm search on a costmap with a given start and goal node
  '''

    
  pass



def main():
    pass
if __name__ == '__main__':
    main()
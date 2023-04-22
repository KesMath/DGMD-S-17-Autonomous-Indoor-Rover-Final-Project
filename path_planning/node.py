class Node:
    def __init__(self, grid_cost: int, coordinate_pt: tuple, parent) -> None:
        self.grid_cost = grid_cost # shortest distance from parent node 
        self.parent = parent
        self.coordinate_pt = coordinate_pt
    
    def update_grid_cost(self, val: int) -> None:
        if val >= 0:
            self.grid_cost = val
    
    def get_grid_cost(self) -> int:
        return self.grid_cost

    def get_parent(self):
        return self.parent
    
    def get_coordinate_pt(self) -> tuple:
        return self.coordinate_pt

    def __str__(self):
        return "Node with grid_cost = " + str(self.grid_cost) + " at starting pt: " + str(self.coordinate_pt)
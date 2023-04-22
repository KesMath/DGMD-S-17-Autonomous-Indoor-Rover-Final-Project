import unittest
from grid_maps import *
from copy import deepcopy
from dijkstra_path_planner import *

'''
python3 path_planning/test_dijkstra_path_planner.py
'''

class TestPathPlanner(unittest.TestCase):

    def test_center_cell_returns_four_neighbors(self):
        expected = list()
        parent_node = Node(grid_cost = 0, coordinate_pt = (2,2), parent = None)

        expected.append(Node(grid_cost = 1, coordinate_pt = (2,1), parent = parent_node)) # LEFT
        expected.append(Node(grid_cost = 1, coordinate_pt = (2,3), parent = parent_node)) # RIGHT
        expected.append(Node(grid_cost = 1, coordinate_pt = (1,2), parent = parent_node)) # UP
        expected.append(Node(grid_cost = 1, coordinate_pt = (3,2), parent = parent_node)) # DOWN

        actual = find_neighbours(node=parent_node, width=5, height=5, gridmap=EMPTY_GRID, resolution=STEP_COST)
        
        assert(len(actual) == len(expected))

        # assert coordinates are as expected
        self.assertEqual(expected[0].get_coordinate_pt(), actual[0].get_coordinate_pt())
        self.assertEqual(expected[1].get_coordinate_pt(), actual[1].get_coordinate_pt())
        self.assertEqual(expected[2].get_coordinate_pt(), actual[2].get_coordinate_pt())
        self.assertEqual(expected[3].get_coordinate_pt(), actual[3].get_coordinate_pt())
        
        # assert grid cost is as expected
        self.assertEqual(expected[0].grid_cost, actual[0].grid_cost)
        self.assertEqual(expected[1].grid_cost, actual[1].grid_cost)
        self.assertEqual(expected[2].grid_cost, actual[2].grid_cost)
        self.assertEqual(expected[3].grid_cost, actual[3].grid_cost)

        # assert parent node is as expected
        for node in actual:
            self.assertEqual(node.parent, parent_node)
        

    def test_bottom_left_cell_returns_two_neighbors(self):
        expected = list()
        parent_node = Node(grid_cost = 0, coordinate_pt = (4,0), parent = None)

        expected.append(Node(grid_cost = 1, coordinate_pt = (4,1), parent = parent_node)) # RIGHT
        expected.append(Node(grid_cost = 1, coordinate_pt = (3,0), parent = parent_node)) # UP

        actual = find_neighbours(node=parent_node, width=5, height=5, gridmap=EMPTY_GRID, resolution=STEP_COST)

        assert(len(actual) == len(expected))

        # assert coordinates are as expected
        self.assertEqual(expected[0].get_coordinate_pt(), actual[0].get_coordinate_pt())
        self.assertEqual(expected[1].get_coordinate_pt(), actual[1].get_coordinate_pt())
        
        # assert grid cost is as expected
        self.assertEqual(expected[0].grid_cost, actual[0].grid_cost)
        self.assertEqual(expected[1].grid_cost, actual[1].grid_cost)

        # assert parent node is as expected
        for node in actual:
            self.assertEqual(node.parent, parent_node)


    def test_bottom_right_cell_returns_two_neighbors(self):
        expected = list()
        parent_node = Node(grid_cost = 0, coordinate_pt = (4,4), parent = None)

        expected.append(Node(grid_cost = 1, coordinate_pt = (4,3), parent = parent_node)) # LEFT
        expected.append(Node(grid_cost = 1, coordinate_pt = (3,4), parent = parent_node)) # UP

        actual = find_neighbours(node=parent_node, width=5, height=5, gridmap=EMPTY_GRID, resolution=STEP_COST)

        assert(len(actual) == len(expected))

        # assert coordinates are as expected
        self.assertEqual(expected[0].get_coordinate_pt(), actual[0].get_coordinate_pt())
        self.assertEqual(expected[1].get_coordinate_pt(), actual[1].get_coordinate_pt())
        
        # assert grid cost is as expected
        self.assertEqual(expected[0].grid_cost, actual[0].grid_cost)
        self.assertEqual(expected[1].grid_cost, actual[1].grid_cost)

        # assert parent node is as expected
        for node in actual:
            self.assertEqual(node.parent, parent_node)

    def test_upper_left_cell_returns_two_neighbors(self):
        expected = list()
        parent_node = Node(grid_cost = 0, coordinate_pt = (0,0), parent = None)

        expected.append(Node(grid_cost = 1, coordinate_pt = (0,1), parent = parent_node)) # RIGHT
        expected.append(Node(grid_cost = 1, coordinate_pt = (1,0), parent = parent_node)) # DOWN

        actual = find_neighbours(node=parent_node, width=5, height=5, gridmap=EMPTY_GRID, resolution=STEP_COST)

        assert(len(actual) == len(expected))

        # assert coordinates are as expected
        self.assertEqual(expected[0].get_coordinate_pt(), actual[0].get_coordinate_pt())
        self.assertEqual(expected[1].get_coordinate_pt(), actual[1].get_coordinate_pt())
        
        # assert grid cost is as expected
        self.assertEqual(expected[0].grid_cost, actual[0].grid_cost)
        self.assertEqual(expected[1].grid_cost, actual[1].grid_cost)

        # assert parent node is as expected
        for node in actual:
            self.assertEqual(node.parent, parent_node)
    
    def test_upper_right_cell_returns_two_neighbors(self):
        expected = list()
        parent_node = Node(grid_cost = 0, coordinate_pt = (0,4), parent = None)

        expected.append(Node(grid_cost = 1, coordinate_pt = (0,3), parent = parent_node)) # LEFT
        expected.append(Node(grid_cost = 1, coordinate_pt = (1,4), parent = parent_node)) # DOWN

        actual = find_neighbours(node=parent_node, width=5, height=5, gridmap=EMPTY_GRID, resolution=STEP_COST)

        assert(len(actual) == len(expected))

        # assert coordinates are as expected
        self.assertEqual(expected[0].get_coordinate_pt(), actual[0].get_coordinate_pt())
        self.assertEqual(expected[1].get_coordinate_pt(), actual[1].get_coordinate_pt())
        
        # assert grid cost is as expected
        self.assertEqual(expected[0].grid_cost, actual[0].grid_cost)
        self.assertEqual(expected[1].grid_cost, actual[1].grid_cost)

        # assert parent node is as expected
        for node in actual:
            self.assertEqual(node.parent, parent_node)


    def test_cell_ignores_one_occupied_neighbor(self):
        expected = list()
        parent_node = Node(grid_cost = 0, coordinate_pt = (2,2), parent = None)
        temp_grid = deepcopy(EMPTY_GRID)

        # occupying left adjacent neighbor
        temp_grid[2][1] = 1  # LEFT

        actual = find_neighbours(node=parent_node, width=5, height=5, gridmap=temp_grid, resolution=STEP_COST)

        expected.append(Node(grid_cost = 1, coordinate_pt = (2,3), parent = parent_node)) # RIGHT
        expected.append(Node(grid_cost = 1, coordinate_pt = (1,2), parent = parent_node)) # UP
        expected.append(Node(grid_cost = 1, coordinate_pt = (3,2), parent = parent_node)) # DOWN

        assert(len(actual) == len(expected))

        # assert coordinates are as expected
        self.assertEqual(expected[0].get_coordinate_pt(), actual[0].get_coordinate_pt())
        self.assertEqual(expected[1].get_coordinate_pt(), actual[1].get_coordinate_pt())
        self.assertEqual(expected[2].get_coordinate_pt(), actual[2].get_coordinate_pt())
        
        # assert grid cost is as expected
        self.assertEqual(expected[0].grid_cost, actual[0].grid_cost)
        self.assertEqual(expected[1].grid_cost, actual[1].grid_cost)
        self.assertEqual(expected[2].grid_cost, actual[2].grid_cost)

        # assert parent node is as expected
        for node in actual:
            self.assertEqual(node.parent, parent_node)


    def test_cell_ignores_two_occupied_neighbors(self):
        expected = list()
        parent_node = Node(grid_cost = 0, coordinate_pt = (2,2), parent = None)
        temp_grid = deepcopy(EMPTY_GRID)

        # occupying left and righht adjacent neighbors
        temp_grid[2][1] = 1  # LEFT
        temp_grid[2][3] = 1  # RIGHT

        actual = find_neighbours(node=parent_node, width=5, height=5, gridmap=temp_grid, resolution=STEP_COST)

        expected.append(Node(grid_cost = 1, coordinate_pt = (1,2), parent = parent_node)) # UP
        expected.append(Node(grid_cost = 1, coordinate_pt = (3,2), parent = parent_node)) # DOWN

        assert(len(actual) == len(expected))

        # assert coordinates are as expected
        self.assertEqual(expected[0].get_coordinate_pt(), actual[0].get_coordinate_pt())
        self.assertEqual(expected[1].get_coordinate_pt(), actual[1].get_coordinate_pt())
        
        # assert grid cost is as expected
        self.assertEqual(expected[0].grid_cost, actual[0].grid_cost)
        self.assertEqual(expected[1].grid_cost, actual[1].grid_cost)

        # assert parent node is as expected
        for node in actual:
            self.assertEqual(node.parent, parent_node)
   
    def test_cell_ignores_three_occupied_neighbors(self):
        expected = list()
        parent_node = Node(grid_cost = 0, coordinate_pt = (2,2), parent = None)
        temp_grid = deepcopy(EMPTY_GRID)

        # occupying left and righht adjacent neighbors
        temp_grid[2][1] = 1  # LEFT
        temp_grid[2][3] = 1  # RIGHT
        temp_grid[1][2] = 1  # UP

        actual = find_neighbours(node=parent_node, width=5, height=5, gridmap=temp_grid, resolution=STEP_COST)

        expected.append(Node(grid_cost = 1, coordinate_pt = (3,2), parent = parent_node)) # DOWN

        assert(len(actual) == len(expected))

        # assert coordinates are as expected
        self.assertEqual(expected[0].get_coordinate_pt(), actual[0].get_coordinate_pt())
        
        # assert grid cost is as expected
        self.assertEqual(expected[0].grid_cost, actual[0].grid_cost)

        # assert parent node is as expected
        for node in actual:
            self.assertEqual(node.parent, parent_node)

    
    def test_cell_has_no_free_neighbors(self):
        parent_node = Node(grid_cost = 0, coordinate_pt = (2,2), parent = None)
        temp_grid = deepcopy(EMPTY_GRID)

        # occupying all adjacent neighbors around parent node
        temp_grid[2][1] = 1  # LEFT
        temp_grid[2][3] = 1  # RIGHT
        temp_grid[1][2] = 1  # UP
        temp_grid[3][2] = 1  # DOWN

        actual = find_neighbours(node=parent_node, width=5, height=5, gridmap=temp_grid, resolution=STEP_COST)
        self.assertEqual(len(actual), 0)

    def test_shortest_path_in_empty_grid(self):
        expected_coordinates = list()
        # generates shortest path from starting point = (bottom left corner) to goal_point = (top right corner) as an L shape traversal
        path = return_shortest_path(start_point = (4,0), goal_point = (0,4), width = 5, height = 5, gridmap= EMPTY_GRID, resolution = STEP_COST)
        expected_coordinates.extend([(4,0), (4,1), (4,2), (4,3), (4,4), (3,4), (2,4), (1,4), (0,4)])
        assert len(path) == len(expected_coordinates)
        for i in range(0, len(path)):
            assert path[i].get_coordinate_pt() == expected_coordinates[i]
    
    def test_shortest_path_does_not_exist(self):
        # Recall rover cannot travel diagonally hence when
        # rover is boxed in, there is no shortest path!
        path = return_shortest_path(start_point = (2,2), goal_point = (0,4), width = 5, height = 5, gridmap= BOXED_IN_GRID, resolution = STEP_COST)
        self.assertIsNone(path)

    def test_shortest_path_in_diagonally_occupied_grid(self):
        expected_coordinates = list()
        # generates shortest path from starting point = (bottom left corner) to goal_point = (top right corner) as a Zig Zag shape traversal
        path = return_shortest_path(start_point = (4,0), goal_point = (0,4), width = 5, height = 5, gridmap= DIAGONAL_OCCUPIED_GRID, resolution = STEP_COST)
        expected_coordinates.extend([(4,0), (4,1), (4,2), (3,2), (2,2), (2,3), (2,4), (1,4), (0,4)])
        assert len(path) == len(expected_coordinates)
        for i in range(0, len(path)):
            assert path[i].get_coordinate_pt() == expected_coordinates[i]

    
    def test_shortest_path_in_occupied_grid1(self):
        expected_coordinates = list()
        # generates shortest path from starting point = (bottom left corner) to goal_point = (top right corner) as a Zig Zag shape traversal
        path = return_shortest_path(start_point = (4,0), goal_point = (0,4), width = 5, height = 5, gridmap= OCCUPIED_GRID1, resolution = STEP_COST)
        expected_coordinates.extend([(4,0), (3,0), (3,1), (2,1), (1,1), (1,2), (1,3), (1,4), (0,4)])

        assert len(path) == len(expected_coordinates)
        for i in range(0, len(path)):
            assert path[i].get_coordinate_pt() == expected_coordinates[i]
        

if __name__ == '__main__':
    unittest.main()
import unittest
import boggle

class TestBoggle(unittest.TestCase):
    """
    our test suite for boggle solver
    """
    def test_can_create_an_empty_grid(self):
        """
        test to see if we can create an empty grid
        """
        grid = boggle.make_grid(0,0)
        self.assertEqual(len(grid),0)
        
    def test_grid_size_is_width_times_height(self):
        """
        test size is width times height
        """
        grid = boggle.make_grid(2, 3)
        self.assertEqual(len(grid), 6)
        
    def test_grid_coordinates(self):
        """
        Test to ensure that all coordinates can be reached
        """
        grid = boggle.make_grid(2, 2)
        self.assertIn((0, 0),grid)
        self.assertIn((0, 1),grid)
        self.assertIn((1, 0),grid)
        self.assertIn((1, 1),grid)
        self.assertNotIn((2, 2),grid)
        
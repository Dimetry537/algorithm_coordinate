import unittest
from src.path_finder import PathFinder

class TestPathFinder(unittest.TestCase):
    def setUp(self):
        self.pathfinder = PathFinder()
        
    def test_empty_path(self):
        coords = [(0, 0), (1, 1)]
        path, distance = self.pathfinder.find_path(coords, (0, 0), (1, 1))
        
        self.assertEqual(len(path), 2)
        self.assertAlmostEqual(distance, 1.41, places=2)
        
    def test_longer_path(self):    
        coords = [(0, 0), (1, 1), (2, 2)] 
        path, distance = self.pathfinder.find_path(coords, (0, 0), (2, 2))
        
        self.assertEqual(len(path), 3)
        self.assertAlmostEqual(distance, 2.83, places=2)
        
    def test_unreachable_node(self):
        coords = [(0, 0), (1, 1)]
        path, distance = self.pathfinder.find_path(coords, (0, 0), (2, 2))
        
        self.assertIsNone(path)
        self.assertIsNone(distance)

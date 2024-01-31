import unittest
from src.graph_executor import GraphExecutor

class TestGraphExecutor(unittest.TestCase):

    def test_start_end_points(self):
        start = {"coordinates": [1, 2]}
        end = {"coordinates": [4, 5]}
        executor = GraphExecutor(start, end)
        
        self.assertEqual(executor.start_point(), (1, 2)) 
        self.assertEqual(executor.end_point(), (4, 5))

    def test_grid_size(self):
        start = {"coordinates": [1, 2]} 
        end = {"coordinates": [4, 5]}
        executor = GraphExecutor(start, end)
        
        vertices = executor.generate_grid()
        self.assertEqual(executor.grid_size, 0.5)
        self.assertAlmostEqual(vertices[1][0] - vertices[0][0], 0.5)

    def test_grid_coverage(self):
        start = {"coordinates": [1.2, 2.7]}
        end = {"coordinates": [4.8, 5.1]} 
        executor = GraphExecutor(start, end)
        
        vertices = executor.generate_grid()
        self.assertIn(start["coordinates"], vertices) 
        self.assertIn(end["coordinates"], vertices)
        
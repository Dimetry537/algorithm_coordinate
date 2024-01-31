import unittest
from src.my_polygon import MyPolygon

class TestMyPolygon(unittest.TestCase):

    def test_few_points(self):
        data = {"coordinates": [[(1, 1), (2, 2)]]} 
        with self.assertRaises(ValueError):
            poly = MyPolygon(data)
            
    def test_normal_case(self):
        data = {"coordinates": [[(1, 1), (2, 2), (2, 1), (1, 1)]]}
        poly = MyPolygon(data)
        edges = poly._polygon_lines()
        self.assertEqual(len(edges), 4)

    def test_ray_method(self):
        data = {"coordinates": [[(1, 1), (2, 2), (2, 1)]]}
        poly = MyPolygon(data)
        edges = []
        new_edges = poly.ray_method(edges)
        self.assertEqual(len(new_edges), 3)

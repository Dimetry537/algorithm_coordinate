import json
from numpy import arange
from shapely.geometry import Point

class GraphExecutor:
    def __init__(self, start_geojson, end_geojson):
        start_point = json.loads(start_geojson)  
        end_point = json.loads(end_geojson)
        
        start_coords = start_point["coordinates"]
        end_coords = end_point["coordinates"]
        
        self.start = Point(start_coords)
        self.end = Point(end_coords)  
        
        self.grid_size = 0.5

    def generate_grid(self):
        x_min = min(self.start.x, self.end.x) - 1
        x_max = max(self.start.x, self.end.x) + 1
        y_min = min(self.start.y, self.end.y) - 1 
        y_max = max(self.start.y, self.end.y) + 1
        
        xs = arange(x_min, x_max, self.grid_size)
        ys = arange(y_min, y_max, self.grid_size)
        vertices = [[x, y] for x in xs for y in ys]

        return vertices

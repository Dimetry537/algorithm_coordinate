import json
import numpy as np
from shapely.geometry import Point

class GraphExecutor:
    def __init__(self, start_point, end_point, polygon_data) -> None:
        self.start_point = start_point
        self.end_point = end_point
        self.polygon_data = polygon_data


    def max_and_min_coords(self, all_coords):
        lats = np.fromiter((lat for coords in all_coords for lat, _ in coords), dtype=float)
        lons = np.fromiter((lon for coords in all_coords for _, lon in coords), dtype=float)
        
        min_lat = lats.min()
        max_lat = lats.max()
        min_lon = lons.min()
        max_lon = lons.max()

        max_bounds = [(max_lat, max_lon)]
        min_bounds = [(min_lat, min_lon)]

        return max_bounds, min_bounds


    def generate_grid(self):
        x_min = min(self.start.x, self.end.x)
        x_max = max(self.start.x, self.end.x)
        y_min = min(self.start.y, self.end.y) 
        y_max = max(self.start.y, self.end.y)
        
        xs = np.arange(x_min, x_max + self.grid_size, self.grid_size)
        ys = np.arange(y_min, y_max + self.grid_size, self.grid_size)
        
        vertices = [[x, y] for x in xs for y in ys]
        
        if self.start.coords[0] not in vertices:
            vertices.append(list(self.start.coords[0])) 
        if self.end.coords[0] not in vertices:
            vertices.append(list(self.end.coords[0]))

        vertices = [tuple(vertex) for vertex in vertices]
            
        return vertices
    
    def start_point(self):
        return self.start.coords[0]
    
    def end_point(self):
        return self.end.coords[0]

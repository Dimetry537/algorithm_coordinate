import json
from numpy import arange
from shapely.geometry import Point

class GraphExecutor:
    def __init__(self, start_point, end_point) -> None:
        
        start_coords = start_point["coordinates"]
        end_coords = end_point["coordinates"]
        
        self.start = Point(start_coords)
        self.end = Point(end_coords)
        
        self.grid_size = 0.5

    def generate_grid(self):
        x_min = min(self.start.x, self.end.x)
        x_max = max(self.start.x, self.end.x)
        y_min = min(self.start.y, self.end.y) 
        y_max = max(self.start.y, self.end.y)
        
        xs = arange(x_min, x_max + self.grid_size, self.grid_size)
        ys = arange(y_min, y_max + self.grid_size, self.grid_size)
        
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

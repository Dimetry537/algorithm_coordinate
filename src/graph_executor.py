import numpy as np

class GraphExecutor:
    def max_and_min_coords(self, convert_coords):
        lats = np.fromiter((lat for coords in convert_coords for lat, _ in coords), dtype=float)
        lons = np.fromiter((lon for coords in convert_coords for _, lon in coords), dtype=float)
        
        min_lat = lats.min()
        max_lat = lats.max()
        min_lon = lons.min()
        max_lon = lons.max()

        southeast_coordinate = [(min_lat, max_lon)]
        northeast_coordinate = [(max_lat, max_lon)]
        northwest_coordinate = [(max_lat, min_lon)]
        southwest_coordinate = [(min_lat, min_lon)]


        return southeast_coordinate, southwest_coordinate, northeast_coordinate, northwest_coordinate


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
    
    def generate_coordinates(se, sw, ne, nw, step=0.1):
        coordinates = []
        print(se[0])

        for lat in range(int(se[0] * 10), int(ne[0] * 10) + 1, int(step * 10)):
            for lon in range(int(sw[1] * 10), int(se[1] * 10) + 1, int(step * 10)):
                lat /= 10.0
                lon /= 10.0
                coordinates.append((lat, lon))

        return coordinates
    
    def start_point(self):
        return self.start.coords[0]
    
    def end_point(self):
        return self.end.coords[0]

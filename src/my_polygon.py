from shapely.geometry import LineString
class MyPolygon:

    def __init__(self, polygon_data):
        self._coordinates = polygon_data
        edges = self._coordinates
        
        if len(edges) < 3:
            raise ValueError("Недостаточно точек для построения полигона (минимум 3)")

        self._coordinates = edges

    
    def polygon_lines(self):
        edges = []
        for i in range(len(self._coordinates)):
            start = self._coordinates[i]
            end = self._coordinates[(i+1) % len(self._coordinates)]
            edge = LineString([start, end])
            edges.append(edge)
            return edges
    

    def ray_method(self, edges):
        for i in range(len(self._coordinates)):
            start = self._coordinates[i]
            end = self._coordinates[(i+1) % len(self._coordinates)]
            edge = LineString([start, end])
            edges.append(edge)
            return edges

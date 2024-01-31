from shapely.geometry import LineString
class MyPolygon:

    def __init__(self, polygon_data):
        coordinates = polygon_data["coordinates"]
        
        if len(coordinates[0]) < 3:
            raise ValueError("Недостаточно точек для построения полигона (минимум 3)")

        self._coordinates = coordinates[0]

    
    def _polygon_lines(self):
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

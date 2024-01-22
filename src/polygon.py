import json
from shapely.geometry import Polygon

class MyPolygon:

    def __init__(self, geojson_polygon):
        polygon_data = json.loads(geojson_polygon)
        coordinates = polygon_data["coordinates"]
        
        if len(coordinates[0]) < 3:
            raise ValueError("Недостаточно точек для построения полигона (минимум 3)")

        self._coordinates = coordinates[0]
        self._polygon = Polygon(self._coordinates)
    
    @property
    def polygon(self):
        return self._polygon

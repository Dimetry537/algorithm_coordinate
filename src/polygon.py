import json
from shapely.geometry import Polygon
import matplotlib.path as mplPath
import numpy as np

class MyPolygon:

    def __init__(self, geojson_polygon):
        polygon_data = json.loads(geojson_polygon)
        coordinates = polygon_data["coordinates"]
        
        if len(coordinates[0]) < 3:
            raise ValueError("Недостаточно точек для построения полигона (минимум 3)")

        self._coordinates = coordinates[0]
        self._polygon = Polygon(self._coordinates)
        inner_coordinates = self.get_inner_coords()
        MyPolygon.all_coordinates.append(self._coordinates)
        MyPolygon.all_coordinates.append(inner_coordinates)
    
    @property
    def polygon(self):
        return self._polygon

    def get_inner_coords(self):
        path = mplPath.Path(self._coordinates)

        min_x = np.floor(min(p[0] for p in self._coordinates))
        min_y = np.floor(min(p[1] for p in self._coordinates)) 

        max_x = np.ceil(max(p[0] for p in self._coordinates))
        max_y = np.ceil(max(p[1] for p in self._coordinates))

        x_coords = np.arange(min_x, max_x, 0.1)
        y_coords = np.arange(min_y, max_y, 0.1)

        inner_coords = []
        for x in x_coords:
            for y in y_coords:
                if path.contains_point((x, y)):
                    inner_coords.append([x, y])

        return inner_coords
    
    @staticmethod
    def get_all_coordinates():
        return MyPolygon.all_coordinates
    
    def __repr__(self) -> str:
        return f"MyPolygon({self._coordinates})"
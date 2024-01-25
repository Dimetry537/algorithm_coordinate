import json
import random
import shapely.geometry
class MyPolygon:

    def __init__(self, geojson_polygon):
        polygon_data = json.loads(geojson_polygon)
        coordinates = polygon_data["coordinates"]
        
        if len(coordinates[0]) < 3:
            raise ValueError("Недостаточно точек для построения полигона (минимум 3)")

        self._coordinates = coordinates[0]

    def _lats_and_lons(self):
        data = self._coordinates
        polygon = shapely.geometry.Polygon(data)
        area = polygon.area
        lats = [coord[0] for coord in data]
        lons = [coord[1] for coord in data]
        lats_max = max(lats)
        lons_max = max(lons)
        lats_min = min(lats)
        lons_min = min(lons)
        return lats_max, lons_max, lats_min, lons_min, area
    
    
    def ray_method(self, lats_max, lons_max, lats_min, lons_min, area):

        if area < 4:
            for i in range(100):
                random_lat = random.randint(int(lats_min*100000), int(lats_max*100000))/100
                random_lon = random.randint(int(lons_min*100000), int(lons_max*100000))/100
                yield random_lat, random_lon
        else:
            for i in range(1000):
                random_lat = random.randint(int(lats_min*100000), int(lats_max*100000))/100
                random_lon = random.randint(int(lons_min*100000), int(lons_max*100000))/100
                yield random_lat, random_lon


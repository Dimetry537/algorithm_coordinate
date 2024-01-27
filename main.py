from src.my_polygon import MyPolygon
from src.graph_executor import GraphExecutor

if __name__ == "__main__":
    start_point = '{ "type": "Point", "coordinates": [54.99629, 73.35857]}'
    end_point = '{ "type": "Point", "coordinates": [54.98093, 82.88871]}'
    first_polygon = '{"type": "Polygon", "coordinates": [[[53.97930, 78.36354], [52.86596, 78.46006], [52.89925, 81.67985], [55.05971, 81.58333], [54.99648, 80.07340], [54.54308, 78.94958], [53.97930, 78.36354]]]}'
    second_polygon = '{"type": "Polygon", "coordinates": [[[56.09846, 77.23969], [54.92263, 78.13330], [55.64655, 79.74431], [56.32245, 78.83812], [56.09846, 77.23969]]]}'
    third_polygon = '{"type": "Polygon", "coordinates": [[[54.07576, 74.84552], [54.34116, 76.09654], [55.06049, 76.63007], [56.02501, 76.24372], [56.14818, 74.97430], [55.71880, 74.18322], [54.60841, 74.13416], [54.07576, 74.84552]]]}'
    polygon = MyPolygon(first_polygon)
    polygon1 = MyPolygon(second_polygon)
    polygon2 = MyPolygon(third_polygon)

    print("Полигон:")
    all_coords = MyPolygon.get_all_coordinates(polygon)
    print(all_coords)

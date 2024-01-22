from src.polygon import MyPolygon
from src.graph_executor import GraphExecutor

if __name__ == "__main__":
    try:
        geojson_polygon = '{"type": "Polygon", "coordinates": [[[53.97930, 78.36354], [52.86596, 78.46006], [52.89925, 81.67985], [55.05971, 81.58333], [54.99648, 80.07340], [54.54308, 78.94958], [53.97930, 78.36354]]]}'
        polygon_object = MyPolygon(geojson_polygon)
        polygon_coordinates = polygon_object.get_polygon_coordinates()

        print(polygon_coordinates)
        
        # polygon_string_bad = '{"type":"Polygon","coordinates":[[[30,10],[40,40]]]}'
        # bad_polygon = Polygon(polygon_string_bad)
        # print(bad_polygon)
    except ValueError as ve:
        print(f"Ошибка: {ve}")

    # try:
    #     start_geojson = '{"type":"Point","coordinates":[0,0]}'
    #     end_geojson = '{"type":"Point","coordinates":[2,2]}'
    #     graph_executor = GraphExecutor(start_geojson, end_geojson)
    #     grid_vertices = graph_executor.generate_grid()
        
    #     print("Сгенерированные вершины сетки:")
    #     for vertex in grid_vertices:
    #         print(vertex)
    # except ValueError as ve:
    #     print(f"Ошибка: {ve}")

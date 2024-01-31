from src.my_polygon import MyPolygon
from src.graph_executor import GraphExecutor
from src.path_finder import PathFinder
from src.input_data import first_polygon, second_polygon, third_polygon, start_point, end_point

if __name__ == "__main__":
    polygon = MyPolygon(first_polygon)
    polygon1 = MyPolygon(second_polygon)
    polygon2 = MyPolygon(third_polygon)

    graph = GraphExecutor(start_point, end_point)
    coordinates = graph.generate_grid()
    start_coords = graph.start_point()
    end_coords = graph.end_point()
    print(coordinates)
    print(start_coords)
    print(end_coords)

    path = PathFinder()
    shortest_path, total_distance = path.find_path(coordinates, start_coords, end_coords)
    print(shortest_path)
    print(total_distance)
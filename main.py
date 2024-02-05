from src.input_data import first_polygon, second_polygon, third_polygon, start_point, end_point
from src.json_encoder import JsonEncoder
from src.my_polygon import MyPolygon
from src.graph_executor import GraphExecutor


if __name__ == "__main__":
    json = JsonEncoder()
    graph_executor = GraphExecutor()
    # polygon = MyPolygon()

    start_point = json.decode_points(start_point)
    end_point = json.decode_points(end_point)
    first_polygon = json.decode_polygon(first_polygon)
    second_polygon = json.decode_polygon(second_polygon)
    third_polygon = json.decode_polygon(third_polygon)

    print(start_point)
    print(end_point)
    print(first_polygon)
    print(second_polygon)
    print(third_polygon)

    all_coords = [first_polygon, start_point, second_polygon, end_point, third_polygon]

    southeast_coordinate, southwest_coordinate, northeast_coordinate, northwest_coordinate = graph_executor.max_and_min_coords(all_coords)


    print(f'southeast_coordinate: {southeast_coordinate}')
    print(f'southwest_coordinate: {southwest_coordinate}')
    print(f'northeast_coordinate: {northeast_coordinate}')
    print(f'northwest_coordinate: {northwest_coordinate}')

    greed = graph_executor.generate_coordinates(
        southwest_coordinate,
        northeast_coordinate,
        northwest_coordinate,
        step=0.1
    )

    print(greed)
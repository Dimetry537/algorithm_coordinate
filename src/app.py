from input_data import first_polygon, second_polygon, third_polygon, start_point, end_point
from json_encoder import JsonEncoder
from my_polygon import MyPolygon
from graph_executor import GraphExecutor

start_point = JsonEncoder(start_point)
end_point = JsonEncoder(end_point)
first_polygon = JsonEncoder(first_polygon)
second_polygon = JsonEncoder(second_polygon)
third_polygon = JsonEncoder(third_polygon)

start_point_coords = start_point.decode()
end_point_coords = end_point.decode()
first_polygon_coords = first_polygon.decode()
second_polygon_coords = second_polygon.decode()
third_polygon_coords = third_polygon.decode()
# polygon = MyPolygon()
# graph_executor = GraphExecutor()
print(start_point_coords)
print(end_point_coords)
print(first_polygon_coords)
print(second_polygon_coords)
print(third_polygon_coords)

# all_coords = [first_polygon, second_polygon, third_polygon, start_point, end_point]

# min_coords, max_coords = graph_executor.max_and_min_coords(all_coords)

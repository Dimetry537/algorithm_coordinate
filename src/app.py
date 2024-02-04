from input_data import first_polygon, second_polygon, third_polygon, start_point, end_point
from json_encoder import JsonEncoder
from my_polygon import MyPolygon
from graph_executor import GraphExecutor

json = JsonEncoder()
# polygon = MyPolygon()
# graph_executor = GraphExecutor()

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

# all_coords = [first_polygon, second_polygon, third_polygon, start_point, end_point]

# min_coords, max_coords = graph_executor.max_and_min_coords(all_coords)

import networkx as nx
from geopy.distance import geodesic

class PathFinder:
    def __init__(self) -> None:
        self.G = nx.Graph()
        
    def find_path(self, coordinates, start_point, end_point):
        for coord in coordinates:
            self.G.add_node(tuple(coord))

        for i in range(len(coordinates)):
            for j in range(i + 1, len(coordinates)):
                coord1, coord2 = coordinates[i], coordinates[j]
                distance = geodesic(coord1, coord2).km
                self.G.add_edge(tuple(coord1), tuple(coord2), weight=distance)

        shortest_path = nx.shortest_path(self.G, source=tuple(start_point), target=tuple(end_point), weight='weight')
        total_distance = sum(self.G[tuple(shortest_path[i])][tuple(shortest_path[i + 1])]['weight'] for i in range(len(shortest_path) - 1))
        
        return shortest_path, total_distance


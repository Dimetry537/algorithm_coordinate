import json

class JsonEncoder:
    def decode_points(self, data):
        self.data = json.loads(data)
        self.coordinates = self.data['coordinates']
        coordinates = tuple(self.coordinates)
        return coordinates
    
    
    def decode_polygon(self, data):
        self.data = json.loads(data)
        self.coordinates = self.data['coordinates'][0]
        coordinates = [(coords[0], coords[1]) for coords in self.coordinates]
        return coordinates
    
    
    # def encode_line_string(self, coordinates):
    #     line_string = {
    #         "type": "LineString",
    #         "coordinates": coordinates
    #     }
    #     return self.data_encoded(line_string)

import json

class JsonEncoder:
    def __init__(self, data):
        self.data = json.loads(data)
        self.coordinates = self.data['coordinates'][0]

    def decode(self):
        coordinates = [(coords[0], coords[1]) for coords in self.coordinates]
        return [coordinates]
    
    def encode_line_string(self, coordinates):
        line_string = {
            "type": "LineString",
            "coordinates": coordinates
        }
        return self.data_encoded(line_string)

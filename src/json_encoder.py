import json

class JsonEncoder:
    def __init__(self, data):
        self.data = json.loads(data)
        self.data_encoded = json.dumps(self.data)

    def encode(self):
        return self.data
    
    def decode(self):
        return self.data_encoded
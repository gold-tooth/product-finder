import json

class DataManager():

    def __init__(self):
        self.filename = "products.json"

    def save(self, products):
        with open(self.filename, 'w')   as f:
            json.dump(products, f)

    def load(self, format='json'):
        with open(self.filename, 'r')   as f:
            jstr = f.read()
            if format == 'json':
                return json.loads(jstr)
            elif format == 'list':
                return jstr
                

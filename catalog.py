import json

class Catalog:
    @staticmethod
    def read(filename):
        with open(filename, 'r') as catalog:
            data = json.load(catalog)
        return data


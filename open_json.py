import json

def open_json(name):
    file = f'data/{name}.json'

    with open(file, 'r') as open_file:
        return json.load(open_file)
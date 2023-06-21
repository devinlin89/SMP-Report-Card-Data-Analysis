import json

def open_json(name: str):
    file = f'data/{name}.json'

    with open(file, 'r') as open_file:
        return json.load(open_file)
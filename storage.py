import json

def read(location):
    with open(location + '.json', 'r') as file:
        return json.load(file)

def write(location, data):
    with open(location + '.json', 'w') as file:
        # json.dump(data['forecast']['forecastday'][0]['day'], file)
        json.dump(data, file)

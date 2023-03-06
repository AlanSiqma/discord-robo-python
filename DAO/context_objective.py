
import json
FILEPATH = 'data.json'


def get_json_data():
    with open(FILEPATH) as json_file:
        data = json.load(json_file)

    return data


def store_json_data(data):
    with open(FILEPATH, 'w') as outfile:
        json.dump(data, outfile)

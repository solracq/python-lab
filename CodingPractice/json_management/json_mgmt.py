"""
    Python Json management:
    FUNCTION            INPUT           OUTPUT          USECASE
    json.load()         file obj        python obj      read JSON from a file
    json.loads()        String          python obj      read JSON from a string
    json.dump()         python obj      file obj        write JSON to a file
    json.dumps()        python obj      string          convert python obj -> JSON string
"""

import json

def read_json_from_file(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    print(f"Loaded from a JSON file to python object: {data}")
    print(data["name"])

def read_json_string(json_str):
    data = json.loads(json_str)
    print(f"Loaded from a JSON string to python object: {data}")
    print(data["city"])

def write_json_to_file(json_obj):
    # write json_obj to a file
    with open("output.json", "w") as f:
        data = json.dump(json_obj, f, indent=4)
    # read json_file to python obj
    with open("output.json", "r") as f:
        data = json.load(f)
    print(data)
    print(data["skills"][0])

def write_json_to_string(json_obj):
    data = json.dumps(json_obj, indent=2)
    print(f"Writing JSON to a string: {data}")

if __name__ == "__main__":
    json_file = "data.json"
    read_json_from_file(json_file)

    json_str = '{"city": "Toronto", "country": "Canada"}'
    read_json_string(json_str)

    person = {
        "name": "John",
        "age": 25,
        "skills": [
            "Python",
            "SDET",
            "AWS"
        ]
    }
    write_json_to_file(person)

    write_json_to_string(person)
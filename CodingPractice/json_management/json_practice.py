import json

def store_list_file_json(json_file, array):
    # Checking if the new array line exists
    with open(json_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            if "['a', 'b', 'c', 'd']" in line:
                print(f"{array} already exists in JSON file")
                return 0
    # Appending the array line to the json file
    with open(json_file, "a") as f:
        json.dump(array, f, indent=4)
    # Read the content of the json file
    # with open(json_file, "r") as file:
    #     data = json.load(file)
    # print(data)

def read_json_from_string(json_str):
    data = json.loads(json_str)
    print(data)

def write_json_to_string(s):
    dictionary = {s[i]: s.count(s[i]) for i in range(len(s))}
    data = json.dumps(dictionary, indent=4, sort_keys=True)
    print(data)

if __name__ == "__main__":
    json_file = "numbers.json"
    array = ["a", "b", "c", "d"]
    store_list_file_json(json_file, array)

    json_string = '{"name": "John", "age": 30, "city": "New York"}'
    read_json_from_string(json_string)

    s = "Testing is very dupper fun"
    write_json_to_string(s)
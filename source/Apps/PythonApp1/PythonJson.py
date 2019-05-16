import json

data = {
    "user": {
        "name": "Vlad",
        "age": 25
    }
}

with open("data.json", "w") as write_file:
    json.dump(data, write_file, indent = 4)

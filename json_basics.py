import json

car_data = {"name": "tesla", "engine": "electric"} #dictionary

print(type(car_data))

# 2 methods in JSON
# json.dumps() - Seriallises json to a formatted string
# json.dump() - Creates a stream object and expects a file object to write to

car_data_json_string = json.dumps(car_data)

print(car_data_json_string)

print(type(car_data_json_string))

car_data = {"name": "tesla", "engine": "electric"}

with open("new_json_file.json", "w") as jsonfile:
    json.dump(car_data, jsonfile)


# Using json.load

with open("new_json_file.json") as jsonfile:
    car = json.load(jsonfile)

    print(car)
    print(type(car))
    print(car["name"])
    print(car["engine"])
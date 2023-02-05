# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary


import json

# Sample JSON

userJSON_hd = '{"first_name": "Hamze", "last_name": "Daher", "age": 21}'

# Parse to dict

user_hd = json.loads(userJSON_hd)

print(user_hd)

print(user_hd['first_name'])


car_hd = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON_hd = json.dumps(car_hd)

print(carJSON_hd)


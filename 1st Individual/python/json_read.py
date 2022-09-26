import json

with open('./Files/data.json') as f:
    data = json.load(f)

print(data)

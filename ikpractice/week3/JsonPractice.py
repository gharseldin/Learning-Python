import json

with open('Sample.json', 'r') as file:
    data = json.load(file)
print(data)

print(data['name'])
print(data['address'])

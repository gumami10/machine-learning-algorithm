import json


with open('Takeout/Historico/local.json') as json_file:
    data = json.load(json_file)

print(len(data['locations']))
#for local in data['locations']:
#    print(local)


# locations

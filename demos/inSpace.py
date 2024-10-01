import requests

#url from http://open-notify.org/Open-Notify-API/People-In-Space/
res = requests.get('http://api.open-notify.org/astros.json')

json = res.json()

for person in json['people']:
    print(person) #prints all info about people

print('The people currently in space are:')
#just their names
for person in json['people']:
    print(person['name'])
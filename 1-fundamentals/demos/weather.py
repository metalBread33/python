import requests

url = 'http://api.weatherapi.com/v1/current.json?key=8876060024a44a85be6171620240110&q=macon&aqi=no'
res = requests.get(url).json()

temp = res.get('current').get('temp_f')
description = res.get('current').get('condition').get('text')
print ("Today's temperature in Macon, GA is", temp, 'degrees F and', description)
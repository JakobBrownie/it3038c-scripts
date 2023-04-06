import json
import requests

r = requests.get('http://localhost:3000')
data = r.json()
print(data[0]['name'], "is", data[0]['color'])
print(data[1]['name'], "is", data[1]['color'])
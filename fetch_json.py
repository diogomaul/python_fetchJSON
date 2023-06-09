import requests
import json

url = 'https://edfreitas.me/test/wired_brain.json'
response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)
    for item in data:
        print(item)
else:
    print("Error fetching data. Status code:", response.status_code)
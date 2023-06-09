import json
import os

json_path = 'coffee_sales'

for filename in os.listdir(json_path):
    if filename.endswith('.json'):
        with open(os.path.join(json_path, filename)) as f:
            data = json.load(f)            
            print('File:', filename)
            print('Type:', type(data))
            
            if isinstance(data, list):
                print('List Items:')
                for item in data:
                    print(item)
            elif isinstance(data, dict):
                print('Dictionary Items:')
                for key, value in data.items():
                    print(key, ':', value)
            else:
                print('Data:')
                print(data)
            print('-------------------------')
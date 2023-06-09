import os
import json

directory = 'coffee_sales/'
combined_data = []

for filename in os.listdir(directory):
    if filename.endswith('.json'):
        with open(os.path.join(directory, filename), 'r') as f:
            data = json.load(f)
            combined_data.extend(data)

for item in combined_data:
    print(item)

output_file = 'output.json'

with open(output_file, 'w') as f:
    json.dump(combined_data, f)
import json

input_file1 = 'coffee_sales/coffee_sales_1.json'
input_file2 = 'coffee_sales/coffee_Sales_2.json'

output_file = 'output2.json'

with open(input_file1) as f:
    data1 = json.load(f)

with open(input_file2) as f:
    data2 = json.load(f)

combined_data = []
combined_data.extend(data1)
combined_data.extend(data2)

with open(output_file, 'w') as f:
    json.dump(combined_data, f)

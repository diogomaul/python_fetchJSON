import json

with open('coffee_sales/coffee_sales.json', 'r') as f:
    data = json.load(f)

sales_data = data['sales']
locations = [location['name'] for location in data['locations']]
dates = [sale['date'] for sale in sales_data]
sales = [sale['sales'] for sale in sales_data]
coffee_data = {'locations': locations, 'dates': dates, 'sales': sales}

print(coffee_data)
output_file = 'summary.json'

with open(output_file, 'w') as f:
    json.dump(coffee_data, f)
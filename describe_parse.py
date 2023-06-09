import json

with open('coffee_sales/coffee_sales.json', 'r') as f:
    data = json.load(f)

print(type(data))

json_string = json.dumps(data)

print(type(json_string))

new_data = json.loads(json_string)

print(type(new_data))

sales_data = new_data['sales']

locations = [location['name'] for location in new_data['locations']]
print(locations)

dates = [sale['date'] for sale in sales_data]
print(dates)

sales = [sale['sales'] for sale in sales_data]
print(sales)

total_sales = sum(total['sales'] for total in sales_data)
print(total_sales)

coffee_data = {'locations': locations, 'dates': dates, 'sales': sales, 'totalsales': total_sales}

print(coffee_data)
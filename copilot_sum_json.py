import json

# Load the first JSON file
with open('coffee_sales/coffee_sales_1.json') as f:
    sales1 = json.load(f)

# Load the second JSON file
with open('coffee_sales/coffee_sales_2.json') as f:
    sales2 = json.load(f)

# Combine the sales data
all_sales = sales1 + sales2

# Calculate the total sales
total_sales = sum(sale['sales'] for sale in all_sales)

# Create a dictionary with the total sales
result = {'total_sales': total_sales}

# Write the result to a new JSON file
with open('total_sales.json', 'w') as f:
    json.dump(result, f)
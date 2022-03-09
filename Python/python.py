import csv

# csv header
fieldnames = ['name', 'country_code2']

# csv data
rows = [
    {'name': 'Albania',
    'country_code2': 'AL',
    {'name': 'Algeria',
    'country_code2': 'DZ',
    {'name': 'American Samoa',
    'country_code2': 'AS',
]

with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
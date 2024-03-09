import csv
import json

# Read the CSV file
with open('worldcities.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Generate a JSON array file with city, country, iso2, iso3
with open('city_country.json', 'w') as f:
    json_data = [{'name': row['city'], 'countryName': row['country'], 'code': row['iso3']} for row in data]
    json.dump(json_data, f)

# Generate a JSON array file with unique country, iso2, iso3 entries
with open('unique_country.json', 'w') as f:
    unique_data = list({(row['country'], row['iso2'], row['iso3']): row for row in data}.values())
    json_data = [{'name': row['country'], 'code': row['iso3']} for row in unique_data]
    json.dump(json_data, f)

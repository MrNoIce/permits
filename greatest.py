# This function grabs the list stored locally and sorts based on the highest commercial value.
# Note the 'float' function for converting the string values of 'cost' to numerical values.

import json

def permits_sort(permits):
    return float(permits['cost'])

with open('../permit_info.json', 'r') as f:
    data = json.load(f)

data = [item for item in data if 'Commercial' in item['description']] #Sorting values based on commercial description
data = [item for item in data if item['cost'] != "1"] #ignoring values where the cost = "1"

data.sort(key=permits_sort, reverse=True)

data_str = json.dumps(data, indent=2)

print(data[0])
#messing with the open data portal on building permits and saving some data locally

import json
import time
import requests

r = requests.get('https://data.nashville.gov/resource/3h5w-q8b7.json')
permits_json = r.json()

results = []

t1 = time.perf_counter()

for permit in permits_json:
    
    permit_num = permit.get('permit')
    permit_desc = permit.get('permit_type_description')
    permit_cost = permit.get('const_cost')
    permit_purpose = permit.get('purpose')

    data = {
        'permit': permit_num,
        'description': permit_desc,
        'cost': permit_cost,
        'purpose': permit_purpose
    }

    results.append(data)

    # time.sleep(r.elapsed.total_seconds())

    # print(f'got {permit_num} in {r.elapsed.total_seconds()} seconds')

t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds')

with open('permit_info.json', 'w') as f:
    json.dump(results, f, indent=2)


permit_str = json.dumps(permits_json[15].get('purpose'), indent=2)
print(permit_str)


# print(len(permits_str)) = 1634839








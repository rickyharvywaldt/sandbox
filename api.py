import requests as r

response = r.get("https://api.data.gov.sg/v1/environment/air-temperature").json()

for item in response:

    stations = response["metadata"]["stations"]

    for station in stations:

        print(f'De id van {station["name"]} = {station["id"]}')

import requests
import json
from config import API_PARAMS as prms

url = "https://api.themoviedb.org/3/discover/movie?"

params = {'api_key': prms['key'],
          'language': 'pt-BR',
          'region' : 'BR',
          'release_date.gte': prms['startDate'],
          'release_date.lte': prms['endDate'],
          'page' : 1}

response = requests.get(url, params=params)

if response.status_code == 200:

    payload = response.json()
    dataobj = json.dumps(payload, ensure_ascii=False, indent=4)
    print(dataobj)
    
    with open(file='sample.json', mode='w', encoding='utf-8') as file:
        file.write(dataobj)

else:
    print("Error: Unable to retrieve data from API")




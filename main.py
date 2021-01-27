# https://randommer.io/api/api/Card

import requests
url = 'https://randommer.io/api/Card'
headers = {'X-Api-Key':'fc7c869b5d48d49ea32fbabe1cc43a'}
payload = {
    'type': 'Visa',

}
r = requests.get(url, headers=headers, params=payload)

data = r.json()

print(data)
#1610753174:AAHpqhQf1kdJ1AFOKdZFS14gleR76XwzSHQ

import requests
token = '1610753174:AAHpqhQf1kdJ1AFOKdZFS14gleR76XwzSHQ'

url = f'https://api.telegram.org/bot{token}/getMe'

r = requests.get(url)

print(r.json())
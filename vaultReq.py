# -*-coding: UTF-8-*-

import json
import requests

headers = {'User-Agent': 'Mozilla/5.0'}
payload = {'name':'noname','password':'nonamepass', 'email':'gava@gama.com'}
url = 'https://goto.msk.ru/vault/admin'

session = requests.Session()
post = session.post(url) #, headers=headers, data=payload)
print(post)


import requests
import json
key = 'yMnLCobSvBhYeKjKMw'
url = "https://gender-api.com/get?"

while True:
    name = input('enter your name: ').strip()
    if name == 'q':
        break
    params = {
        'key' : key,
        'name' : name
    }
    res = requests.get(url,params=params)
    res = json.loads(res.text)
    print(res['gender'])
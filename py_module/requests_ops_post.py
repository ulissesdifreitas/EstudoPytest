import requests
import json

url = "https://httpbin.org/post"
payload = {'key1': 'value1', 'key2': 'value2'}
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
r = requests.post(url, data=json.dumps(payload), headers=headers)
print(r.url)
print(r.status_code)
print(r.text)
print(r.request.headers)
print(r.headers)
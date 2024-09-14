import requests
import json
url = "https://www.google.com/"

r = requests.get(url)
print(r.text)
print(r.status_code)
print(r.headers)
print(r.request.headers)
# print(r.json())
print(r.headers['Date'])
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# url = "https://regres.in/api/users"
# r = requests.get(url)
# print(r.status_code)
# print(r.headers)~

url = "https://httpbin.org/get"
myparams = {'key1': 'value1', 'key2': 'value2'}
l = requests.get(url, params=myparams)
print(l.url)
print(l.text)
data = json.loads(l.text)

for key, value in data.items():
    print(key, ":", value)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(data['headers']['Host'])


import requests

url = "https://httpbin.org/post"
data = dict(title="Learn Python Programming")
response = requests.post(url, data=data)
print("Response for POST")
print(response.json())

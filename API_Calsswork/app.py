import requests

res = requests.get("https://zenquotes.io/api/quotes")

data = res.json()
for item in data:
    print(item['q'] + " - " + item['a'])
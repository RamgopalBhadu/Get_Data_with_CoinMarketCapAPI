import requests
import json

api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=10&convert=USD&CMC_PRO_API_KEY=7f766470-57a5-4071-8849-8cb29e28212f")

api = json.loads(api_request.content)

for i in range(0,6):
    print(api["data"][i]["symbol"])
    print(api["data"][i]["quote"]["USD"]["price"])

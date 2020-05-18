import requests
import json

api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=2&convert=USD&CMC_PRO_API_KEY=7f766470-57a5-4071-8849-8cb29e28212f")

api = json.loads(api_request.content)

print(api["data"][0]["symbol"])
print(api["data"][0]["quote"]["USD"]["price"])

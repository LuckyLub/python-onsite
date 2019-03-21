'''
Sign up for an API key with the new coinmarketcap API.

Using their documentation, fetch all listed cryptocurrencies.
From the result, create a new JSON file that includes the following:
* cmc_rank
* name
* symbol
* platform
* quote

Save that info to a file.

'''

from Documents import coinmarketcap_key

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from pprint import pprint

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD',
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': coinmarketcap_key.key
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

result = []

for dict_ in data["data"]:
    result_dict = {}
    result_dict["cmc_rank"] = dict_["cmc_rank"]
    result_dict["name"] = dict_["name"]
    result_dict["symbol"] = dict_["symbol"]
    result_dict["platform"] = dict_["platform"]
    result_dict["quote"] = dict_["quote"]
    result.append(result_dict)

pprint(result)
file = "Documents/cryptocurrencies2.JSON"

with open(file, "w") as fout:
    json.dump(result, fout)



'''
http://docs.nomics.com/
Using the nomics API, repeatedly fetch the price of Bitcoin for a duration of 10 minutes.
Store each value in a dictionary that uses the time of query as a key.

After the script stopped running, determine programmatically at what query time the price
was the highest, and when the lowest.

HINTS:
- request an API key first and remember to include it in your queries
- the /prices endpoint of the nomics API can be used for achieving this task
- remember to use packages from the standard library, e.g. for time keeping and dates

BONUS: Explore the logging package for easier tracking

'''
import requests
from datetime import datetime
from datetime import timedelta
from time import sleep

key_path = "Documents/nomics_key"
with open(key_path,"r") as fin:
    key = fin.read()
url = f"https://api.nomics.com/v1/prices?key={key}"

time_to_fetch = 10 #in minutes
start_time = datetime.now()
end_time = start_time + timedelta(minutes=time_to_fetch)

results = {}

while True:

    res = requests.get(url).json()
    now = datetime.now()

    for dict in res:
        if dict["currency"] == "BTC":
            results[now.__str__()] = dict["price"]
    print(results)
    sleep(10)
    if now > end_time:
        break


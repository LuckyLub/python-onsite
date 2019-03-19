'''
Write a script that connects to the http://numbersapi.com/ and fetches trivia on all
numbers from 0 through 100.

Store the responses in a new JSON file called numbers.json

BONUS:
* fetch information of all the prime numbers from 1-1000
* cycle through the different endpoints the API provides (trivia, math, date, year)
  in a way that they change in binary chunks, e.g.:
  - the info on the first 2 numbers are of type trivia
  - info on the next 4 numbers are of type math
  - the next 8 are on dates
  - etc. (cycle back to the trivia after year)

'''

import requests
import json

url = "http://numbersapi.com/"

prime_numbers=[1]
count = 0
trans = 2
cycle = 1

prime_numbers_dict = {}


for number in range(1, 100):
    is_prime = True
    if number != 1:
        for div in range(2, number):
            if number % div == 0 and number != div:
                is_prime = False
    if is_prime:

        if cycle == 1:
            prime_numbers_dict[number] = requests.get(url + str(number)).text + "/trivia"
            count += 1
            if count == trans:
                trans = trans ** 2
                cycle = 2

        elif cycle == 2:
            prime_numbers_dict[number] = requests.get(url + str(number)).text + "/math"
            count += 1
            if count == trans:
                trans = trans ** 2
                cycle = 3

        elif cycle == 3:
            prime_numbers_dict[number] = requests.get(url + str(number)).text + "/date"
            count += 1
            if count == trans:
                trans = trans ** 2
                cycle = 4

        else:
            prime_numbers_dict[number] = requests.get(url + str(number)).text + "/year"
            count += 1
            if count == trans:
                trans = trans ** 2
                cycle = 1

with open("Documents/numbers.json", "w") as fout:
    json.dump(prime_numbers_dict, fout)


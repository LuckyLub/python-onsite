'''
Use the countries API https://restcountries.eu/ to fetch information
on your home country and the country you're currently in.

In your python program, parse and compare the data of the two responses:
* Which country has the larger population?
* How much does the are of the two countries differ?
* Print the native name of both countries, as well as their capitals

'''
import requests

def country_data(country):
    dict_ = dict()
    url = f"https://restcountries.eu/rest/v2/name/{country}"
    dict_["name"] = country
    dict_["population"] = requests.get(url).json()[0]["population"]
    dict_["area"] = requests.get(url).json()[0]["area"]
    dict_["nativeName"] = requests.get(url).json()[0]["nativeName"]
    dict_["capital"] = requests.get(url).json()[0]["capital"]
    return dict_

current_country = "Indonesia"
home_country = "Netherlands"

current_country_data = country_data(current_country)
home_country_data = country_data(home_country)

if current_country_data["population"] > home_country_data["population"]:
    print(f"With a population of {current_country_data['population']} the country you are currently in "
          f"({current_country_data['name']}), has a larger population than your home country, which only has a"
          f"population of {home_country_data['population']}.")

elif current_country_data["population"] < home_country_data["population"]:
    print(f"With a population of {current_country_data['population']} the country you are currently in "
          f"({current_country_data['name']}) has a smaller population than your home country, which only has a"
          f"population of {home_country_data['population']}.")

else:
    print(f"With a population of {current_country_data['population']} the country you are currently in "
          f"({current_country_data['name']}) and your home country have an equally large population.")

area_dif = abs(current_country_data["area"] - home_country_data["area"])

if current_country_data["area"] > home_country_data["area"]:
    print(f"The country you are currently in ({current_country_data['name']}) is larger than your home country, "
          f"with a difference of {area_dif} square kilometers.")

elif current_country_data["area"] < home_country_data["area"]:
    print(f"The country you are currently in ({current_country_data['name']}) is smaller than your home country, "
          f"with a difference of {area_dif} square kilometers.")

else:
    print(f"The country you are currently in ({current_country_data['name']}) has the same size as your home country")


print(f"Did you know that the native name of {current_country_data['name']} is {current_country_data['nativeName']}.\n"
      f"The native name of your home country is {home_country_data['nativeName']}, but you probably already knew that.")



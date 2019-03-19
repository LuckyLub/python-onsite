'''
Using the PokéAPI https://pokeapi.co/docs/v2.html#pokemon
fetch the name and height of all 151 Pokémon of the main series.

Create a text document that describes each Pokémon using the information
available in the JSON response.
NOTE: only using 'height' is enough, but if you want more, go crazy.

BONUS: Using your script, create a folder and download the main 'front_default'
       sprites for each Pokémon using requests into that folder.
       Name the files appropriately using the name data from your response.

'''

import requests

url = "https://pokeapi.co/api/v2/pokemon/"
file = "Documents/pokemonheights.txt"
pokeID = 0

print(requests.get("https://pokeapi.co/api/v2/pokemon/1").json()["name"])
print(requests.get("https://pokeapi.co/api/v2/pokemon/1").json()["height"])

poke_dict = {}

while True:
    pokeID += 1
    print(pokeID)
    res = requests.get(url + str(pokeID))
    if res.__str__() == "<Response [404]>":
        break
    poke_dict[res.json()["name"]] = res.json()["height"]

with open(file, "w") as fout:
    for k, v in poke_dict.items():
        fout.write(f"{k}: {v}\n")





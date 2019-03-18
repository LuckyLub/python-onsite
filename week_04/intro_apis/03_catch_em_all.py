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
pokeID = 0

print(requests.get("https://pokeapi.co/api/v2/pokemon/1").json()["name"])
print(requests.get("https://pokeapi.co/api/v2/pokemon/1").json()["height"])

with open("pokemonheights.txt", "w") as fout:
    for pokeID in range(1, 400):
        res = requests.get(url)
        if res.__init__() == "<Response [404]>":
            break
        poke_name = res.json()["name"]
        poke_height = res.json()["height"]
        fout.write(f"{poke_name}: {poke_height}cm\n")





'''
Using the Chuck Norris API in combination with the datamuse API
( https://api.chucknorris.io/ - https://www.datamuse.com/api/ )

* Query the chucknorris api for a sentence
* Use the last word of that sentence to send a query to the Datamuse API
  and use the rel_rhy (or rel_nry) query parameter to fetch a word that rhymes
* Repeat a coupe of times and store the sentences and rhyme words
* Synthesize the collected results into an avant-garde poem and present it to class ;)

'''

import requests

file = "Documents/rhymes.txt"

repeats = 10
count = 0

with open(file,"w") as fout:
    while True:
        url_chuck = "https://api.chucknorris.io/jokes/random"
        joke = requests.get(url_chuck).json()["value"]
        last_word = joke.split()[-1].strip(".!? ")

        try:
            url_word = f"https://api.datamuse.com/words?rel_rhy={last_word}"
            rhyme_word = requests.get(url_word).json()[0]["word"]
        except IndexError as ie:
            continue

        fout.write(joke + "\n")
        fout.write(rhyme_word + "\n")

        count += 1
        if count == repeats:
            break

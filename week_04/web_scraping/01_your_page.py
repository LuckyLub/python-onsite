'''
Using python's request library, retrieve the HTML of the website you created
that now lives online at <your-gh-username>.github.io/<your-repo-name>

BONUS: extend your python program so that it reads your original HTML file
       and returns True if the HTML from the response is the same as the
       the contents of the original HTML file.
<<<<<<< HEAD
'''


import requests
import os

url = "https://lubcountcooper.github.io/my_sites/"
file = "/home/robert-jan/Documents/CodingNomads/Extras/my_sites/index.html"

with os.fdopen(os.open(file, os.O_RDONLY), "r") as fin:
    original = fin.read()

content = requests.get(url).text

if original == content:
    print(True)
else:
    print(False)




'''
>>>>>>> 52cba3b05b42df043df4904b236c3e044812bb5f'''

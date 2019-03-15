'''
Using requests_html scrape information from a wikipedia page that interests you.
( you can use: https://en.wikipedia.org/wiki/Ubud )

Collect:
* all the information recorded in the infobox on the right
* 2 links to images on the site
* an interesting fact or quote from the page
* a collection of all the resources (titles and links) related to the page

Store the information in a nicely formatted text file.

'''

import random
from requests_html import HTMLSession

url = "https://en.wikipedia.org/wiki/Ubud"
# url = 'https://en.wikipedia.org/wiki/Indonesia#Culture'

session = HTMLSession()
r = session.get(url)


# all the information recorded in the infobox on the right

info = r.html.find("#mw-content-text > div > table.infobox.geography.vcard > tbody")

info_list =[]

for tr in info[0].find('tr'):
    info_list.append(tr.text)

print(info_list)


# 2 links to images on the site
img = r.html.find("img")

links =[]

for pic in img:
    links.append(pic.attrs["src"])

print(links)


# an interesting fact or quote from the page
paragraphs = r.html.find("p")
random_fact_nr = random.randrange(0, len(paragraphs))

print(paragraphs[random_fact_nr].text)


# a collection of all the resources (titles and links) related to the page
# i can't get the links.

refs = r.html.xpath('//*[@id="mw-content-text"]/div/ul[1]/li')


for item in refs:
    print(item.text)





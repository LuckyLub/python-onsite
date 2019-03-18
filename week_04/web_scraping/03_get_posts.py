'''
Create an account at freecycle or use the following:
user: martin-martin
pwd:  bali2019

Using python's request_html library:
* log in to the website
* navigate to the site that contains all posts for the Denver, CO group
* retrieve all post titles from the first page
* save the titles to a file called 'denver_posts.txt'

BONUS: use pagination features to retrieve all posts of all pages in the group
       and save them to the file

'''

from requests_html import HTMLSession

payload = {'username': 'martin-martin', 'pass': 'bali2019'}
url = 'https://my.freecycle.org/login'


session = HTMLSession()
r = session.post(url, data=payload)
r = session.get('https://groups.freecycle.org/group/DenverCO/posts/all')
titles = r.html.find("#group_posts_table > tr > td:nth-child(2) > a")

with open("Documents/denver_posts.txt", "w") as fout:
    for title in titles:
        fout.write(title.text)
        fout.write("\n")



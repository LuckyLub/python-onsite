'''
* BONUS TASK *
* DISCLAIMER: THIS IS PROBABLY HARD AND REQUIRES SOME TWEAKING *

Explore whether you can use the JavaScript support with requests_html,
to scrape the youtube comments from a video page you are interested in.
( you can use: https://www.youtube.com/watch?v=M54UFvJqQ5I )

Parse the content, locate the usernames of the people who commented,
and save all comments to file in the following form:

username:
    comment text

username:
    comment text

etc.

If requests_html doesn't quite make it and you want to learn more
about scraping dynamic page content, check out 'selenium'.

'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def get_comments():
    list_ = []
    comments = browser.find_elements_by_tag_name("ytd-comment-renderer")
    for comment in comments:
        aut = comment.find_element_by_id("author-text").text
        com = comment.find_element_by_id("content-text").text
        list_.append((aut, com))
    return list_


try:

    browser = webdriver.Chrome("/home/robert-jan/Documents/CodingNomads/python-onsite/week_04/web_scraping/Documents/"
                               "chromedriver")
    browser.get('https://www.youtube.com/watch?v=z-OxzIC6pic&feature=youtu.be&t=914')

    WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.ID, 'page-manager')))
    SCROLL_PAUSE_TIME = 2

    # Get scroll height
    last_height = "return document.querySelector('#page-manager').scrollHeight"

    while True:
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.querySelector('#page-manager').scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.querySelector('#page-manager').scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    with open("Documents/Comments_on_youtube.txt", "w") as fout:
        comments = browser.find_elements_by_tag_name("ytd-comment-renderer")
        for comment in comments:
            aut = comment.find_element_by_id("author-text").text
            com = comment.find_element_by_id("content-text").text
            fout.write(f"{aut}: \n    {com}\n\n")

    browser.close()


except Exception as e:
    browser.close()
    raise e

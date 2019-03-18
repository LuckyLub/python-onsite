'''
Using the JavaScript support in requests_html, parse the contents of
an Instagram page you are interested in.

Fetch and prepare all the image links - and only the image links!
* How can you exclude other links present on the page?
* BONUS: Can you find a way to download those images and save them to
         your computer using python?

'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
import time

def get_images(set_):
    images = browser.find_elements_by_class_name("FFVAD")
    for image in images:
        set_.add(image.get_attribute("src"))



try:

    browser = webdriver.Chrome("/home/robert-jan/Documents/CodingNomads/python-onsite/week_04/web_scraping/Documents/"
                               "chromedriver")
    browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    name = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.NAME, 'username')))
    pw = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.NAME, 'password')))

    name.send_keys('martin.breuss')
    pw.send_keys('bali2019' + Keys.RETURN)

    WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'FFVAD')))

    collected_images = set()
    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        get_images(collected_images)

        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    image_index = 1
    for image in collected_images:
        urllib.request.urlretrieve(image, f"Documents/pic{image_index}.jpeg")
        image_index += 1

    browser.close()

except Exception as e:
    browser.close()
    raise e


from selenium import webdriver

import requests
from bs4 import BeautifulSoup
import urllib.request
from datetime import datetime
import time


SEARCH_TERM = "Cobreloa"
ACCOUNT = ""
SINCE = "2018-01-01"
UNTIL = "2018-12-31"

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(30)
verificationErrors = []
accept_next_alert = True

driver.get(("https://twitter.com/search?f=tweets&q={}" +
            "%20since%3A{}%20until%3A{} " +
            "&src=typd&lang=en").format(SEARCH_TERM, SINCE, UNTIL))

for i in range(1, 10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.5)

html_source = driver.page_source
data = html_source.encode('utf-8')
soup = BeautifulSoup(data, 'html.parser')
tws = soup.find_all('div', class_='tweet')
for t in tws:
    if 'RetweetDialog-tweet' not in t.attrs['class']:
        timestamp = t.find('a', class_='tweet-timestamp').find('span')['data-time']
        tweetuser = t.find('a', class_='account-group')['href'][1:]
        date = datetime.fromtimestamp(float(timestamp))
        text = t.find('p', class_='tweet-text').text
        # print(s + " | " + str(date) + row["text"] + row["user_screen_name"])
        # print(HASHTAG, text, str(date))
        print(text)
        print("######")

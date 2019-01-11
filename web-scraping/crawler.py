from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import sys

import unittest, time, re

import requests
from bs4 import BeautifulSoup
import urllib.request
from datetime import datetime


HASHTAG = "Robo"
ACCOUNT = ""
SINCE = "2017-03-01"
UNTIL = "2017-04-18"


driver = webdriver.Firefox()
driver.implicitly_wait(30)
verificationErrors = []
accept_next_alert = True

driver.get(("https://twitter.com/search?f=tweets&q=%23{}" +
            "%20since%3A{}%20until%3A{} " +
            "&src=typd&lang=en").format(HASHTAG, SINCE, UNTIL))

for i in range(1, 20):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.5)

link = driver.find_element_by_link_text('Latest')
link.click()

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
        if len(text) > 199:
            # print("BUU")
            # print(text)
            text = text[:199]
        # print(s + " | " + str(date) + row["text"] + row["user_screen_name"])
        # print(HASHTAG, text, str(date))
        print(text)

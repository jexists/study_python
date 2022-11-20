
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import time
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip # 임시 저장소

import random

import re

from dotenv import load_dotenv
import os
import string

import csv

load_dotenv()

# 크롬 옵션 설정
options = webdriver.ChromeOptions()
# options.headless = True
options.add_argument('window-size=1000,1000')
options.add_argument('no-sandbox')

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
chrome.get('https://www.fifa.com/fifaplus/ko/tournaments/mens/worldcup/qatar2022/teams/argentina/squad')
wait = WebDriverWait(chrome, 10)


def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def find_presence(css):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))

def finds_presence(css):
    find_presence(css)
    return chrome.find_elements(By.CSS_SELECTOR, css)

def find_visible(css):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))

def finds_visible(css):
    find_visible(css)
    return chrome.find_elements(By.CSS_SELECTOR, css)


board = finds_visible(".player-badge-card_badgeCard__2DJ4B")
print(len(board))

re4mo = []
for idx, val in enumerate(board):
    chrome.implicitly_wait(10)
    title = board[idx].find_element(By.CSS_SELECTOR, '.player-badge-card_playerFirstname__1HlN6').get_attribute('innerText')
    position = board[idx].find_element(By.CSS_SELECTOR, '.player-badge-card_playerPosition__wjnoI').get_attribute('innerText')

    # print(title)

    # chrome.set_window_size(1000,10000)
    # contents = find_visible('.se-main-container')
    save_path = "./argentina"
    # os.mkdir(save_path)
    # contents.screenshot(save_path + "/" + str(idx)+".png")

    imgs = board[idx].find_elements(By.CSS_SELECTOR, '.player-badge-card_playerImage__301X0')

    for img in imgs:
        src = img.value_of_css_property("background-image")
        print(title, ' ', position)
        print("\"photo_img\" :"+ src + ',',)
        # t = urlopen(src.lstrip('url("').rstrip('")')).read()
        # file = open(os.path.join(save_path, title + ".png"), "wb")
        # file.write(t)


chrome.quit()
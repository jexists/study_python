
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import time
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip # 임시 저장소

from bs4 import BeautifulSoup
import random

from dotenv import load_dotenv
import os

import csv

load_dotenv()

# 크롬 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument('window-size=1000,1000')
options.add_argument('no-sandbox')

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
chrome.get('https://cafe.naver.com/re4mo')
wait = WebDriverWait(chrome, 10)

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


find_presence(".gnb_btn_login").click()

time.sleep(3)

input_id = find_visible('input#id')
input_pw = find_visible('input#pw')

time.sleep(3)

pyperclip.copy(os.environ.get("ID"))
input_id.send_keys(Keys.COMMAND, 'v')

time.sleep(3)
pyperclip.copy(os.environ.get("PASSWORD"))
input_pw.send_keys(Keys.COMMAND, 'v')
input_pw.send_keys('\n')

save_btn = find_visible('.btn_upload a.btn')
save_btn.click()


find_visible('.gnb_my_namebox')

chrome.implicitly_wait(0.5)

find_presence("#menuLink277").click()
chrome.implicitly_wait(0.5)
chrome.switch_to.frame("cafe_main")

    
time.sleep( random.randint(0,5) )
    
board = finds_visible(".article-board")
lists = board[1].find_elements(By.CSS_SELECTOR, 'tbody .td_article')
print(len(lists))

for idx, val in enumerate(lists):
    chrome.implicitly_wait(10)
    print(idx)
    if idx >= 1:
        chrome.switch_to.frame("cafe_main")
        board = finds_visible(".article-board")
        lists = board[1].find_elements(By.CSS_SELECTOR, 'tbody .td_article')
        chrome.implicitly_wait(10)
    lists[idx].find_element(By.CSS_SELECTOR, '.board-list .article').click()
    chrome.implicitly_wait(10)
    chrome.switch_to.default_content()
    time.sleep(3)
    print(chrome.title)
    chrome.switch_to.frame("cafe_main")
    chrome.implicitly_wait(10)

    contents = chrome.find_elements(By.CSS_SELECTOR, '.se-main-container')

    chrome.implicitly_wait(10)
    chrome.back()
    time.sleep(3)
    chrome.switch_to.default_content()
    chrome.implicitly_wait(10)

# chrome.switch_to.frame("cafe_main")
time.sleep(3)

chrome.quit()



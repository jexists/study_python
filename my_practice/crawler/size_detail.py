
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
load_dotenv()

# 크롬 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument('window-size=1000,1000')
options.add_argument('no-sandbox')

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
chrome.get('https://cafe.naver.com/re4mo')
wait = WebDriverWait(chrome, 10)

def find(wait, css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

find(wait, ".gnb_btn_login").click()

time.sleep(3)

input_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'input#id')))
input_pw = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'input#pw')))

time.sleep(3)

pyperclip.copy(os.environ.get("ID"))
input_id.send_keys(Keys.COMMAND, 'v')

time.sleep(3)
pyperclip.copy(os.environ.get("PASSWORD"))
input_pw.send_keys(Keys.COMMAND, 'v')
input_pw.send_keys('\n')

save_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.btn_upload a.btn')))
save_btn.click()


wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.gnb_my_namebox')))

find(wait, "#menuLink277").click()

chrome.implicitly_wait(0.5)
chrome.switch_to.frame("cafe_main")

# article_board = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.article-board')))
# print(article_board)

article_board = chrome.find_elements(By.CSS_SELECTOR(".article-board"))
print(article_board)
print(article_board[1])

chrome.quit()

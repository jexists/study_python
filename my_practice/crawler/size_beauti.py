

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

### 키워드 수집 정보
num_per_page = 15          # 페이지당 게시글 갯수(default: 15개)
address_list=[]
page = 1

l=True
while l:
    
    time.sleep( random.randint(0,5) )
    
    ### 현재 페이지의 html 불러오기

    r = chrome.page_source
    page_html = BeautifulSoup(r, "html.parser")

    content = page_html.find_all("div", class_="article-board")
    main = content[1].find("tbody")
    body = main.find_all("tr")
    for x in body:
        temp_dict={}
        if x.find("div", class_="inner_number") is not None:
            print(x.find("div", class_="inner_number").text.strip())
            print(' '.join(x.select_one("div.inner_list > a.article").get_text().split()))
            # print(x.select_one("div.inner_list > a.article").get_text().strip())
            print("======================")
        # print(x.select("div.inner_list > a.article").text.strip())
        # https://riverkangg.github.io/%ED%81%AC%EB%A1%A4%EB%A7%81/crawling-2naverCafe/
    l = False

chrome.quit()

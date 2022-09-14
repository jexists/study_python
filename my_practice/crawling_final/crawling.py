
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

from dotenv import load_dotenv
import os
import string

import csv

load_dotenv()

# 크롬 옵션 설정
options = webdriver.ChromeOptions()
options.headless = True
# options.add_argument('window-size=1000,1000')
options.add_argument('no-sandbox')

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
chrome.get('https://cafe.naver.com/re4mo')
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

# 50개 목록 불러오기
find_presence(".select_box").click()
time.sleep( random.randint(0,5) )
find_presence(".select_list li:nth-child(7) a").click()
time.sleep( random.randint(0,5) )
#
# find_presence(".prev-next a:nth-child(0)").click()
# time.sleep( random.randint(0,5) )
    
board = finds_visible(".article-board")
lists = board[1].find_elements(By.CSS_SELECTOR, 'tbody .td_article')
print(len(lists))

re4mo = []
# for idx, val in enumerate(lists):
for idx, val in enumerate([1,2,3]):
    chrome.implicitly_wait(10)
    if idx >= 1:
        chrome.switch_to.frame("cafe_main")
        board = finds_visible(".article-board")
        lists = board[1].find_elements(By.CSS_SELECTOR, 'tbody .td_article')
        chrome.implicitly_wait(10)
    title = lists[idx].find_element(By.CSS_SELECTOR, '.board-list .article').get_attribute('innerText').replace(",","..")
    link = lists[idx].find_element(By.CSS_SELECTOR, '.board-number .inner_number').get_attribute('innerText')
    print(idx, title, link)

    lists[idx].find_element(By.CSS_SELECTOR, '.board-list .article').click()
    chrome.implicitly_wait(10)
    chrome.switch_to.default_content()
    time.sleep(3)
    chrome.switch_to.frame("cafe_main")
    chrome.implicitly_wait(10)
    time.sleep(5)

    chrome.set_window_size(1000,10000)
    contents = find_visible('.se-main-container')
    save_path = "./re4mo/" + str(idx) + "_" + link
    os.mkdir(save_path)
    contents.screenshot(save_path + "/" + str(idx)+".png")

    content = contents.get_attribute('innerText').strip()
    date = chrome.find_element(By.CSS_SELECTOR, '.article_info .date').get_attribute('innerText')
    nickname = chrome.find_element(By.CSS_SELECTOR, '.nick_box .nickname').get_attribute('innerText')

    imgs = contents.find_elements(By.CSS_SELECTOR, 'img')
    for img in imgs:
        src = img.get_attribute('src')
        t = urlopen(src).read()
        file = open(os.path.join(save_path, link + id_generator() + ".jpg"), "wb")
        file.write(t)

    chrome.implicitly_wait(10)
    chrome.back()
    time.sleep(3)
    chrome.switch_to.default_content()
    chrome.implicitly_wait(10)

    temp = []
    temp.append(link)
    temp.append(title)
    temp.append(date)
    temp.append(nickname)
    temp.append(content)
    temp.append(save_path + "/" + str(idx)+".png")
    re4mo.append(temp) #list 안에 list 가 들어가는 형태

time.sleep(3)

chrome.quit()

f = open(f're4mo_size.csv','w',encoding='utf-8-sig',newline='') #파일오픈
csvWriter = csv.writer(f)#열어둔 파일
csv_title = ["링크", "제목", "날짜", "닉네임", "내용", "이미지"]
csvWriter.writerow(csv_title)
for i in re4mo:
    csvWriter.writerow(i) 

f.close()
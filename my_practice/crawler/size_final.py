
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

from bs4 import BeautifulSoup
import random
import base64

from dotenv import load_dotenv
import os
import string

from openpyxl import Workbook
from openpyxl.drawing.image import Image
# pip install openpyxl

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

# 게시판 번호
find_presence("#menuLink277").click()
chrome.implicitly_wait(0.5)
chrome.switch_to.frame("cafe_main")

time.sleep( random.randint(0,5) )
    
board = finds_visible(".article-board")
lists = board[1].find_elements(By.CSS_SELECTOR, 'tbody .td_article')
print(len(lists))

re4mo = []
for idx, val in enumerate([1,2,3]):
# for idx, val in enumerate(lists):
    chrome.implicitly_wait(10)
    if idx >= 1:
        chrome.switch_to.frame("cafe_main")
        board = finds_visible(".article-board")
        lists = board[1].find_elements(By.CSS_SELECTOR, 'tbody .td_article')
        chrome.implicitly_wait(10)
    title = lists[idx].find_element(By.CSS_SELECTOR, '.board-list .article').get_attribute('innerText')
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
    if idx == 0:
      os.mkdir("./re4mo")
    save_path = "./re4mo/" + str(idx) + "_" + link
    os.mkdir(save_path)
    screenshot = save_path + "/" + str(idx)+".png"
    contents.screenshot(screenshot)

    with open(screenshot, "rb") as image:
      encoded_string = base64.b64encode(image.read())
      # encoded_string.decode('utf-8')
      image = encoded_string.decode('utf-8')

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

    # 엑셀 쓰기위한 준빈
    wb = Workbook()
    sheet = wb.active
    img = Image(screenshot) 

    allList = []
    for row in sheet.iter_rows(min_row=1, max_row=10, min_col=2, max_col=5):
        a = []
        for cell in row:
            a.append(cell.value)
        allList.append(a)
    sheet.add_image(img, 'A' + str(idx + 1))
    sheet.column_dimensions['A'].width = 30
    # sheet.row_dimensions[1].height = 174
    sheet.append(link)
    sheet.append(title)
    sheet.append(date)
    sheet.append(nickname)
    sheet.append(content)
    sheet.append(image)

time.sleep(3)

chrome.quit()


sheet.save('test.xlsx')
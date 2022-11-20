
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

import random
import string
import csv


# 크롬 옵션 설정
options = webdriver.ChromeOptions()
# options.headless = True
options.add_argument('window-size=1000,1000')
options.add_argument('no-sandbox')

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 파일 이름 (링크) ################
chrome.get('https://www.fifa.com/fifaplus/ko/tournaments/mens/worldcup/qatar2022/teams/netherlands/squad')
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

re4mo = []
for idx, val in enumerate(board):
    chrome.implicitly_wait(10)
    title = board[idx].find_element(By.CSS_SELECTOR, '.player-badge-card_playerFirstname__1HlN6').get_attribute('innerText')
    position = board[idx].find_element(By.CSS_SELECTOR, '.player-badge-card_playerPosition__wjnoI').get_attribute('innerText')

    # csv 저장하는 위치
    save_path = "./"

    imgs = board[idx].find_elements(By.CSS_SELECTOR, '.player-badge-card_playerImage__301X0')

    for img in imgs:
        src = img.value_of_css_property("background-image")

        temp = []
        temp.append(title)
        temp.append(position)
        temp.append("\"photo_img\" :"+ src + ',')
        re4mo.append(temp) #list 안에 list 가 들어가는 형태

chrome.quit()


# 파일 이름 (나라) ################
f = open(f'netherlands.csv','w',encoding='utf-8-sig',newline='') #파일오픈
csvWriter = csv.writer(f)#열어둔 파일
csv_title = ["타이틀", "포지션", "링크"]
csvWriter.writerow(csv_title)
for i in re4mo:
    csvWriter.writerow(i) 

f.close()
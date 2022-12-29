
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
chrome.get('https://m.sports.naver.com/qatar2022/nation/index?teamCode=4756&tab=players')
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


board = finds_visible(".NationSquad_nation_squad__8P_7Z .NationSquad_player_item__UQ2-n")
print(len(board))
re4mo = []
for idx, val in enumerate(board):
    chrome.implicitly_wait(10)
    title = board[idx].find_element(By.CSS_SELECTOR, '.NationSquad_name__2n74U').get_attribute('innerText')
    number = board[idx].find_element(By.CSS_SELECTOR, '.NationSquad_number__1Tthy').get_attribute('innerText')
    team = board[idx].find_element(By.CSS_SELECTOR, '.NationSquad_club__3YmmI').get_attribute('innerText')
    try:
        weight, height = board[idx].find_element(By.CSS_SELECTOR, '.NationSquad_info__2H0GN .NationSquad_sub__o5ASs:first-of-type').get_attribute('innerText').split(', ')
    except ValueError as e: 
        weight = ""
        height = ""
    age = board[idx].find_element(By.CSS_SELECTOR, '.NationSquad_sub__o5ASs:last-of-type').get_attribute('innerText')
    print(title)
    print(number)
    print(team)
    print(weight)
    print(height)
    print(age) #

    temp = []
    temp.append(title)
    temp.append('"number" : ' + number + ',')
    temp.append('"team" : "' + team + '",')
    temp.append('"weight" : "' + weight.replace("cm","") + '",')
    temp.append('"height" : "' + height.replace("kg","") + '",')
    temp.append('"age" : ' + age.replace("살","") + ',')
    re4mo.append(temp) #list 안에 list 가 들어가는 형태
    # csv 저장하는 위치
    save_path = "./naver"
    
chrome.quit()


# 파일 이름 (나라) ################
f = open(f'Costa.csv','w',encoding='utf-8-sig',newline='') #파일오픈
csvWriter = csv.writer(f)#열어둔 파일
csv_title = ["타이틀", "번호", "팀", "몸무게", "키", "나이"]
csvWriter.writerow(csv_title)
for i in re4mo:
    csvWriter.writerow(i) 

f.close()
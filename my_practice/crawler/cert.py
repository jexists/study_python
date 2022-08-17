
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from webdriver_manager.chrome import ChromeDriverManager


# 크롬 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument('window-size=1000,1000')
options.add_argument('no-sandbox')

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
chrome.get('https://cafe.naver.com/re4mo')
wait = WebDriverWait(chrome, 10)

def find(wait, css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

find(wait, "#menuLink330").click()

time.sleep(3)

 
time.sleep(3)

chrome.close()

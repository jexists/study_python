import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# 파이썬 프로그램 멈추기
time.sleep(3)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.get('https://naver.com/')

time.sleep(3)

chrome.close()
# 크롬 멈추기
chrome.implicitly_wait(3)

# 찾는 원수가 존재할경우까지
WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[name=query]")))
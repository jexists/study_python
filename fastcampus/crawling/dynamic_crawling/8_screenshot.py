
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
chrome.get('https://www.naver.com/')
wait = WebDriverWait(chrome, 10)

def find_presence(css):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))

def find_visible(css):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))

def finds_visible(css):
    find_visible(css)
    return chrome.find_element(By.CSS_SELECTOR, css)

find_visible("input#query").send_keys("레사모\n")

find_presence(wait, "#menuLink330").click()

e = find_visible("li[data-cr-rank='3']")
# 일부 스크린샷
e.screenshot("./test.png")

chrome.save_screenshot("./test.png")
time.sleep(3)

 
chrome.close()

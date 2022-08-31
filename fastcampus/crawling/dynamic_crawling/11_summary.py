
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from webdriver_manager.chrome import ChromeDriverManager


# 크롬 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument('no-sandbox')

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(chrome, 10)

def find_presence(css):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))

def finds_presence(css):
    find_presence(css)
    return chrome.find_element(By.CSS_SELECTOR, css)

def find_visible(css):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))

def finds_visible(css):
    find_visible(css)
    return chrome.find_element(By.CSS_SELECTOR, css)

chrome.get('https://www.naver.com/')

find_visible("input#query").send_keys("레사모\n")

e = find_visible("li[data-cr-rank='3']")

body = find_visible("body")
body.screenshot("./test10.png")

chrome.save_screenshot("./test11.png")
chrome.set_window_size(1000,10000)
chrome.save_screenshot("./test12.png")

# window 사이즈를 넉넉하게 잡아줘야함
body = find_visible("body")
body.screenshot("./test13.png")

chrome.execute_script("""
    document.querySelector("li[data-cr-rank='3']").setAttribute('style','border: 10px solid red')
    """)
body.screenshot("./test14.png")
 
chrome.close()

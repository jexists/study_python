
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
chrome.get('https://shopping.naver.com/')
wait = WebDriverWait(chrome, 10)

def find(wait, css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

search = find(wait, "._searchInput_search_input_QXUFf")
# 검색어 입력
search.send_keys('피규어')
# 검색어 입력 후 엔터
# search.send_keys('피규어\n')
 
button = find(wait,'button._searchInput_button_search_1n1aw')
# 클릭하기
button.click()
time.sleep(3)

chrome.close()

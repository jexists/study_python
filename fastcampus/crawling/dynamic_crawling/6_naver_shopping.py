
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

import time
import os
import pyperclip # 임시 저장소
#pip install pyperclip



# 크롬 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument('window-size=1000,1000')
options.add_argument('no-sandbox')

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(chrome, 10)
short_wait = WebDriverWait(chrome, 3)

chrome.get('https://shopping.naver.com/')

def find(wait, css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

# login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.gnb_btn_login')))
# 보이는 상태인지 확인
# login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.gnb_btn_login')))
# print(login_button.text)
# login_button.click()


wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.gnb_btn_login'))).click()

input_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'input#id')))
input_pw = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'input#pw')))

# input_id.send_keys('아이디')
# input_pw.send_keys(os.getenv(pw))
# input_pw.send_keys('\n')

# pip install pyperclip
pyperclip.copy('id')
# input_id.send_keys(Keys.CONTROL, 'v') #window
input_id.send_keys(Keys.COMMAND, 'v')
pyperclip.copy('password!')
input_pw.send_keys(Keys.COMMAND, 'v')
input_pw.send_keys('\n')

save_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.btn_upload a.btn')))
save_btn.click()




wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.gnb_my_namebox')))

search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[class^=_searchInput_search_input]')))
search.send_keys("피규어")
time.sleep(1)
search.send_keys("\n")

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class^=basicList_info_area__]')))

# 스크롤
# chrome.execute_script("window.scrollBy(0, 10000)")
# chrome.execute_script("window.scrollBy(0, document.body.scrollHeight)")
for i in range(8):
    chrome.execute_script("window.scrollBy(0," +str((i+1) *500)+")")
    time.sleep(1)

items = chrome.find_elements(By.CSS_SELECTOR, "div[class^=basicList_info_area__]")


print("아이템 길이 =====",len(items))
for item in items:
    # 광고 빼기 
    try:
        item.find_element(By.CSS_SELECTOR,"button[class^=ad_ad]")
        continue
    except:
        pass
    print(item.find_element(By.CSS_SELECTOR,"a[class^=basicList_link__]").text)

time.sleep(3)

chrome.close()


# CSS Selector    
# basicList_link__1MaTN
# <a class="logout_button">
# a[class="logout_button"]
# a[class^="logout"] 시작
# a[class&="button"] 끝
# a[class*="out_but"] 포함




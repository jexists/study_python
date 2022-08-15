from selenium import webdriver
import time

# 크롬 > 도움말 > 크롬 정보 > 크롬 버전 같은 chromedriver 다운
# https://chromedriver.chromium.org/downloads

# 개발자를 확인할 수 없기 때문에 ‘chromedriver’을(를) 열 수 없습니다.
# chromedriver 있는 폴더로 이동
# xattr -d com.apple.quarantine chromedriver

browser = webdriver.Chrome("./chromedriver")
browser.get("https://www.naver.com/")
time.sleep(10)
browser.close()
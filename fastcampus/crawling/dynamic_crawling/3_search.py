
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import time
from webdriver_manager.chrome import ChromeDriverManager


# 크롬 옵션 설정
options = webdriver.ChromeOptions()

# 윈도우 사이즈 (width,height)
options.add_argument('window-size=100,100')
# 샌드박스: 외부로부터 들어온 프로그램이 보호된 영역에서 동작해 시스템이 부정하게 조작되는 것을 막는 보안 형태
options.add_argument('no-sandbox')
# 창을 안보이게 하는 것 (CPU, 메모리 최소화)
# options.add_argument('headless')

# 크롬 드라이버 생성
chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# chrome = webdriver.Chrome('./chromedriver', options=options)

# 페이지 이동
chrome.get('https://www.naver.com/')
chrome.get('https://shopping.naver.com/')
chrome.back()
chrome.forward()

# 파이썬 프로그램 멈추기
time.sleep(3)
# 크롬 멈추기
chrome.implicitly_wait(3)


# 크롬 종료 (무조건 해야함)
chrome.close()

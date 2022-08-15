# selenium/standalone-chrome
# docker run -p 4444:4444 selenium/standalone-chrome

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# 원격으로 
brower = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
brower.get("http://naver.com")
print(brower.title)
brower.close()
# pip install selenium-stealth


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
import time
from webdriver_manager.chrome import ChromeDriverManager

# https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html

# https://pypi.org/project/selenium-stealth/

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# languages=["en-US", "en"],
stealth(chrome,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
url = "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"
chrome.get(url)
wait = WebDriverWait(chrome, 10)

time.sleep(5)

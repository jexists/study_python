
from distutils import text_file
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

def leftFrame():
    chrome.switch_to.parent_frame()
    find_visible("#ifrFormSumit")
    chrome.switch_to.frame("ifrFormSumit")

def rightFrame():
    chrome.switch_to.parent_frame() # 부모 프레임으로 이동
    find_visible("#ifrFormSumit")
    chrome.switch_to.frame("ifrFormSumit")

def choose_one(text, options):
    print('-------')
    print(text_file)
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")
    choose = input("-> ")
    return int(choose) - 1


category = {
    "cpu":"873",
    "메인보드":"875",
}

chrome.get("https://shop.danawa.com/virtualestimate/?controller=estimateMain&methods=index&marketPlaceSeq=16")

# find_visible("#ifrFormSumit")
# chrome.switch_to.frame("ifrFormSumit")
category_css = {
    c: "dd.category_" + category[c] + " a" for c in category
}
print(category_css)

print("dd.category_"+category["메인보드"])
mainboard = find_visible("dd.category_"+category["메인보드"]+" a")
mainboard.click()
time.sleep(5)
chrome.quit()

# 제조사 불러오기
leftFrame()
options = finds_visible("select[name=srcMaker] option:not([value]='')")
# print("제조사를 골라주세요.")
# for i in range(len(options)):
#     print(str(i+1) + ". " + options[i].text)

i = choose_one('제조사를 골라주세요.', [x.text for x in options])
print(options[i])

options[i].click()

products = finds_visible("div.search_scroll_box tr[class^=productList_]")
cpus = []
for p in products:
    name = p.find_element(By.CSS_SELECTOR, "p.subject a").text
    try: 
        price = p.find_element(By.CSS_SELECTOR, "span.prod_price").text
    except:
        pass
    cpus.append((name, price))

for cpu in cpus:
    print(cpu)
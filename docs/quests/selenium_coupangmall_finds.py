from selenium import webdriver       # * 웹 크롤링 동작

browser = webdriver.Chrome()         # - chrome browser 열기

html_file = browser.get("https://www.coupang.com/np/categories/194276")         # - 주소 (해당 사이트 주소) 입력

pass                                  # - 가능 여부에 대한 OK 받음

html = browser.page_source            # - html 파일 받음(and 확인)
print(html)

# - 정보 획득
from selenium.webdriver.common.by import By

## 여러개 elements 정보 가져오기
selector_value = "div.name"
elements_path = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)

for webelement in elements_path:                                              # 상품명 추출
    title = webelement.text
    print("{}".format(title))
pass

browser.quit()
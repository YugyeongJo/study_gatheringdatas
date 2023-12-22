from selenium import webdriver       # * 웹 크롤링 동작

browser = webdriver.Chrome()         # - chrome browser 열기

html_file = browser.get("https://corners.auction.co.kr/corner/categorybest.aspx")         # - 주소 (해당 사이트 주소) 입력

# - 정보 획득
from selenium.webdriver.common.by import By
selector_value = "div.mg-list"
browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)

for element_item in element_bundle[10:41]:
    element_title = element_item.find_element(by=By.CSS_SELECTOR, value="div > div.info > em")
    title = element_title.text
    
browser.quit()
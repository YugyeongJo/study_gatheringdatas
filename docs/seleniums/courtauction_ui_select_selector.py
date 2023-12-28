# * 웹 크롤링 동작
from selenium import webdriver

# - chrome browser 열기
browser = webdriver.Chrome()

# - 주소 입력
browser.get("https://www.w3schools.com/")

# - 가능 여부에 대한 OK 받음
# - html 파일 받음(and 확인)
html = browser.page_source
# print(html)

# iframe 으로 전환
browser.switch_to.frame('indexFrame')

# - 정보 획득
from selenium.webdriver.common.by import By
# click menu : #menu > h1:nth-child(5) > a > img
browser.find_element(by=By.CSS_SELECTOR, value="#menu > h1:nth-child(5) > a > img").click()

from selenium.webdriver.support.ui import Select
# 법원/소재지 리스트 : #idJiwonNm > option
element_courts = browser.find_elements(by=By.CSS_SELECTOR, value="#idJiwonNm > option")
for index in range(len(element_courts)) :
    select_court = Select(browser.find_element(by=By.CSS_SELECTOR, value="#idJiwonNm")) 
    select_court.select_by_index(index)
    # 검색 클릭 : #contents > form > div.tbl_btn > a:nth-child(1) > img
    url = "#contents > form > div.tbl_btn > a:nth-child(1) > img"
    browser.find_element(by=By.CSS_SELECTOR, value=url).click()
    time.sleep(1)

    # 이전 화면 : #contents > div.table_contents > form:nth-child(1) > div > div > a:nth-child(5) > img
    url = "#contents > div.table_contents > form:nth-child(1) > div > div > a:nth-child(5) > img"
    browser.find_element(by=By.CSS_SELECTOR, value=url).click()
    time.sleep(3)
    pass
pass

# 브라우저 종료
browser.quit()
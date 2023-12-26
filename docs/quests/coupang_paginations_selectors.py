# * 웹 크롤링 동작
from selenium import webdriver
import time

# - chrome browser 열기
browser = webdriver.Chrome()

# - 주소 입력
for page_number in range(1, 17):
    url = "https://www.coupang.com/np/campaigns/348?page={}".format(page_number)
    browser.get(url)
    time.sleep(3)
pass
# - 가능 여부에 대한 OK 받음
# - html 파일 받음(and 확인)
html = browser.page_source
# print(html)

# - 정보 획득
from selenium.webdriver.common.by import By
# browser.save_screenshot('./formats.png')

# 브라우저 종료
browser.quit()
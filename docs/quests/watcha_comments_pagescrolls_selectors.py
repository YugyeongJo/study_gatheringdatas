from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")

# database 연결
database = mongoClient["local"]

# collection 작업
collection = database['watcha_comments_pagescrolls_selectors']


# * 웹 크롤링 동작
from selenium import webdriver
import time

# - chrome browser 열기
browser = webdriver.Chrome()

# - 주소 입력
browser.get("https://pedia.watcha.com/ko-KR/contents/m53mZg6/comments")

# - 가능 여부에 대한 OK 받음
# - html 파일 받음(and 확인)
html = browser.page_source
# print(html)

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

## 스크롤 이동
element_body = browser.find_element(by=By.CSS_SELECTOR, value="body")
previous_scrollHeight = 0
# while True :
for i in range(3):
    element_body.send_keys(Keys.END)
    current_scrollHeight = browser.execute_script("return document.body.scrollHeight")
    if previous_scrollHeight >= current_scrollHeight :
        break
    else :
        previous_scrollHeight = current_scrollHeight
    time.sleep(1)
    pass

comments = browser.find_elements(by=By.CSS_SELECTOR, value = "ul > div.css-13j4ly.egj9y8a4")

for i in comments:
    element_writer = i.find_element(by=By.CSS_SELECTOR, value="div.css-eldyae.e10cf2lr1")
    element_rating = i.find_element(by=By.CSS_SELECTOR, value="div.css-31ods0.egj9y8a0 > span")
    element_contents = i.find_element(by=By.CSS_SELECTOR, value="div.css-2occzs.egj9y8a1")
    collection.insert_one({"writer": element_writer.text,
                        "rating": element_rating.text, 
                        "contents": element_contents.text})

# 브라우저 종료
browser.quit()
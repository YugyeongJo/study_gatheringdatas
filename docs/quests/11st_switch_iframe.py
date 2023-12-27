#mongodb에 연결
from pymongo import MongoClient
mongoClient = MongoClient("mongodb://localhost:27017")
database = mongoClient["gatheringdatas"]
collection = database['11st_comments']


# * 웹 크롤링 동작
from selenium import webdriver
import time
# - chrome browser 열기
browser = webdriver.Chrome()
# - 주소 입력
browser.get("https://www.11st.co.kr/products/5266817192?inpu=&trTypeCd=&trCtgrNo=")
# - 가능 여부에 대한 OK 받음
# - html 파일 받음(and 확인)
html = browser.page_source
from selenium.webdriver.common.by import By

#전체 데이터 삭제
pass
collection.delete_many({})
pass

# iframe 으로 전환
browser.switch_to.frame('ifrmReview')

#상품평 더보기 클릭
while True : 
    try :
        browser.find_element(by=By.CSS_SELECTOR, value="#review-list-page-area > div > button").click()
    except : 
        break
    time.sleep(3)
    pass

#정보 획득
comments = browser.find_elements(by=By.CSS_SELECTOR, value = "#review-list-page-area > ul > li")
pass

for i in comments:
    try : 
        element_writer = i.find_element(by=By.CSS_SELECTOR, value="#review-list-page-area > ul > li > dl > dt.name")
        element_writer = element_writer.text
    except : 
        element_writer = ""
    try : 
        element_option = i.find_element(by=By.CSS_SELECTOR, value="div.option")
        element_option = element_option.text
    except : 
        try : 
            element_option = i.find_element(by=By.CSS_SELECTOR, value="div.value")
            element_option = element_option.text
        except : 
            element_option = ""
    try : 
        element_grade = i.find_element(by=By.CSS_SELECTOR, value="#review-list-page-area > ul > li > div > p.grade")
        element_grade = element_grade.text
    except : 
        element_grade = ""
    try : 
        element_contents = i.find_element(by=By.CSS_SELECTOR, value="div.cont_text_wrap")
        element_contents = element_contents.text
    except : 
        element_contents = ""
    pass
    time.sleep(1)
    
    #DB전송
    collection.insert_one({"writer": element_writer,
                        "option": element_option,
                        "grade" : element_grade,
                        "contents": element_contents})
    pass



# 브라우저 종료
browser.quit()
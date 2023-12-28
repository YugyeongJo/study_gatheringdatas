#mongodb에 연결
from pymongo import MongoClient
mongoClient = MongoClient("mongodb://localhost:27017")
database = mongoClient["gatheringdatas"]
collection01 = database['11st_item']
collection02 = database['11st_item_comments']

# * 웹 크롤링 동작
from selenium import webdriver
import time
# - chrome browser 열기
browser = webdriver.Chrome()
# - 주소 입력
browser.get("https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb")
# - 가능 여부에 대한 OK 받음
# - html 파일 받음(and 확인)
html = browser.page_source
from selenium.webdriver.common.by import By

#전체 데이터 삭제
pass
collection01.delete_many({})
collection02.delete_many({})
pass

##상품상세정보
# 상품 4개 선정 리스트화
time.sleep(3)

item = ["#thisClick_6173429244 > div > a", "#thisClick_6577469889 > div > a", "#thisClick_5925154481 > div > a", "#thisClick_2281264645 > div > a" ]
for i in item:
    browser.find_element(by=By.CSS_SELECTOR, value = i).click()    #상품상세페이지 click
    time.sleep(3)

    element_title = browser.find_element(by=By.CSS_SELECTOR, value="h1.title")
    img = browser.find_element(by=By.CSS_SELECTOR, value="div.img_full > img")
    element_img = img.get_attribute('src')
    element_price = browser.find_element(by=By.CSS_SELECTOR, value="dd > strong > span.value")
    element_detail = browser.find_element(by=By.CSS_SELECTOR, value="table.prdc_detail_table")
    
    collection01.insert_one({"title": element_title.text,
                        "img": element_img,
                        "price" : element_price.text,
                        "detail": element_detail.text})
    
    pass

    ##상품평
    #정보 획득
    browser.switch_to.frame('ifrmReview')
    comments = browser.find_elements(by=By.CSS_SELECTOR, value = "#review-list-page-area > ul.area_list > li")
    pass
    #iframe 으로 전환
    

    for x in comments:
        try : 
            element_writer = x.find_element(by=By.CSS_SELECTOR, value="#review-list-page-area > ul > li > dl > dt.name")
            element_writer = element_writer.text
        except : 
            element_writer = ""
        try : 
            element_option = x.find_element(by=By.CSS_SELECTOR, value="div.option")
            element_option = element_option.text
        except : 
            try : 
                element_option = x.find_element(by=By.CSS_SELECTOR, value="div.value")
                element_option = element_option.text
            except : 
                element_option = ""
        try : 
            element_grade = x.find_element(by=By.CSS_SELECTOR, value="#review-list-page-area > ul > li > div > p.grade")
            element_grade = element_grade.text
        except : 
            element_grade = ""
        try : 
            element_contents = x.find_element(by=By.CSS_SELECTOR, value="div.cont_text_wrap")
            element_contents = element_contents.text
        except : 
            element_contents = ""
        pass
        time.sleep(3)
        
        #DB전송
        collection02.insert_one({"writer": element_writer,
                            "option": element_option,
                            "grade" : element_grade,
                            "contents": element_contents})
        pass
    
    browser.back()
    pass


# 브라우저 종료
browser.quit()
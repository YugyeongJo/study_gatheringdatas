# * 웹 크롤링 동작
from selenium import webdriver

# - chrome browser 열기
browser = webdriver.Chrome()

# - 주소 입력
browser.get("https://www.jobplanet.co.kr/users/sign_in?_nav=gb")

# - 가능 여부에 대한 OK 받음
# - html 파일 받음(and 확인)
html = browser.page_source
# print(html)

# - 정보 획득
from selenium.webdriver.common.by import By
element_login_field = browser.find_element(by=By.CSS_SELECTOR, value="#user_email")
element_login_field.send_keys("whdb5893@naver.com")

element_password_field = browser.find_element(by=By.CSS_SELECTOR, value="#user_password")
element_password_field.send_keys("")


element_login_button = browser.find_element(by=By.CSS_SELECTOR, value = "#signInSignInCon > div.signInsignIn_wrap > div > section.section_email.er_r > fieldset > button")
element_login_button.click()

# 브라우저 종료
browser.quit()

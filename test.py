from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')

#사이트 접속
driver.get('https://papago.naver.com/')
#페이지 로딩 대기
time.sleep(2)
#자동완성 해제
auto_complete_btn = driver.find_element_by_css_selector('#root > div > div.wrap___1rX6i.rwd.rwd___3Qe-c.banner_active___3MQbf > section > div > div:nth-child(1) > div:nth-child(2) > div > div.autocomplete_area___2alwE.active___3VPGL > label')
auto_complete_btn.click()

#입력창에 입력
input_box = driver.find_element_by_css_selector('#txtSource')
input_box.send_keys('안녕하세요 피로그래밍입니다.')

#번역하기 버튼 클릭
trans_btn = driver.find_element_by_css_selector('#btnTranslate')
trans_btn.click()
#페이지 로딩 대기
time.sleep(2)

#번역결과 출력
output_box = driver.find_element_by_css_selector('#txtTarget').text
print(output_box)
#페이지 로딩 대기
time.sleep(2)


driver.close()
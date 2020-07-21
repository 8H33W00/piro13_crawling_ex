from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get('https://map.kakao.com/')
time.sleep(1)
# 이상한 버튼 없애기
driver.find_element_by_css_selector('div.view_coach').click()

# 강남 마라탕 입력하기
input_box = driver.find_element_by_css_selector('#search\.keyword\.query')
input_box.send_keys('강남 마라탕')
input_box.send_keys(Keys.ENTER)

# 찾기 버튼 누르기
search_btn = driver.find_element_by_css_selector('#search\.keyword\.submit')
search_btn.click()
time.sleep(1)

# 15개 가게 컨테이너 추출하기
stores = driver.find_elements_by_css_selector('.PlaceItem')

# 가게 리스트에서 이름 번호 주소 프린트 해주기
for store in stores:
    name = store.find_element_by_css_selector('a.link_name').text
    try:
        phone = store.find_element_by_css_selector('span.phone').text
    except:
        phone = '번호 없음'
    try:
        addr = store.find_element_by_css_selector('div.addr > p:nth-child(1)').text
    except:
        addr = '주소 없음'
    print(name, phone, addr)
time.sleep(1)

# 장소 더보기 눌러주기
more_place_btn = driver.find_element_by_css_selector('#info\.search\.place\.more')
more_place_btn.send_keys('\n')
time.sleep(1)

# 2페이지부터 11페이지까지 크롤링 하기
for n in range(2, 11):
    # 매번 페이지가 로딩 될 때 time.sleep 시키기
    time.sleep(1)

    # 현재 페이지에 있는 가게 컨테이너들 한꺼번에 추출하기
    stores = driver.find_elements_by_css_selector('li.PlaceItem')

    # 가게에서 이름, (번호 주소)있으면 추출하기. 없으면 없다고 표현
    for store in stores:
        name = store.find_element_by_css_selector('a.link_name').text

        try:
            phone = store.find_element_by_css_selector('span.phone').text
        except:
            phone = '번호 없음'
        try:
            addr = store.find_element_by_css_selector('div.addr > p:nth-child(1)').text
        except:
            addr = '주소 없음'

        print(name, phone, addr)

    # 이전 버튼, 1, 2, 3, 4, 5, 다음 버튼을 모두 포함한 것들 한꺼번에 추출하기
    page_bar = driver.find_elements_by_css_selector('div#info\.search\.page div.pageWrap > *')

    # 5로 나눈 나머지가 0이 아닐 때 1, 2, 3, 4, 5에 해당하는 index에 맞게 페이지 이동하기
    if n % 5 != 0:
        page_bar[n % 5 + 1].click()

    # 5로 나눈 나머지가 0일 땐 현재 페이지가 5, 10, 15, ...페이지라는 의미. 그러므로 다음 버튼 클릭
    else:
        page_bar[6].click()

# 크롤링이 제대로 먹었는지 브라우저에서 확인하기 위해서 sleep
time.sleep(5)

driver.close()
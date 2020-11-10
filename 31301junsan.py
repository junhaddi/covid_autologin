# -*- coding: utf-8 -*-




from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 크롬 헤드리스 옵션
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# 드라이버 설정
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=chrome_options)
driver.implicitly_wait(10)
driver.get('https://hcs.eduro.go.kr')

# 자가진단 참여하기
driver.find_element_by_id('btnConfirm2').click()

# 학교검색
driver.find_element_by_xpath('//input[@title="학교 입력"]').click()

# 시/도
driver.find_element_by_xpath('//select/option[text()="경기도"]').click()

# 학교급
driver.find_element_by_xpath('//select/option[text()="고등학교"]').click()

# 학교명
driver.find_element_by_xpath('//input[@class="searchArea"]').send_keys('양명고등학교')

# 검색
driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click()
driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/p/a').click()

# 학교선택
driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()

# 성명
name = '강준산'
driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr[3]/td/input').send_keys(name)

# 생년월일
birth = '020503'
driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr[4]/td/input').send_keys(birth)

# 확인
driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()

# 비밀번호
password = '1234'
time.sleep(3)
driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr/td/input').click()
driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr/td/input').send_keys(password)

# 확인
driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()

# 참여자 목록
time.sleep(3)
element = driver.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul/li/a')
driver.execute_script('arguments[0].click();', element)

# 1) 학생 본인이 37.5'C 이상 발열 또는 발열감이 있나요??
#    단, 기저질환 등으로 코로나19와 관계없이 평소에 발열 증상이 계속되는 경우는 제외
radio = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="container"]/div/div/div[2]/div[2]/dl[1]/dd/ul/li[1]/label')))
driver.execute_script("arguments[0].click();", radio)

# 2) 학생에게 코로나19가 의심되는 아래의 임상증상*이 있나요?
#    *(주요 임상증상) 기침, 호흡곤란, 오한, 근육통, 두통, 인후통, 후각·미각 소실 또는 폐렴
#    단, 기저질환 등으로 코로나19와 관계없이 평소에 다음 증상이 계속되는 경우는 제외
radio = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="container"]/div/div/div[2]/div[2]/dl[2]/dd/ul/li[1]/label')))
driver.execute_script("arguments[0].click();", radio)

# 3) 학생 본인 또는 동거인이 방역당국에 의해 현재 자가격리가 이루어지고 있나요?
#    ※ <방역당국 지침> 최근 14일 이내 해외 입국자, 확진자와 접촉자 등은 자가격리 조치
#    단, 직업특성상 잦은 해외 입·출국으로 의심증상이 없는 경우 자가격리 면제
radio = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="container"]/div/div/div[2]/div[2]/dl[3]/dd/ul/li[1]/label')))
driver.execute_script("arguments[0].click();", radio)

# 제출
driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()

driver.quit()

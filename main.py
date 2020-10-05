from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 드라이버 설정
path = 'C:\\chromedriver'
driver = webdriver.Chrome(path)
driver.implicitly_wait(10)
driver.get('https://hcs.eduro.go.kr')

# 자가진단 참여하기
driver.find_element_by_id('btnConfirm2').click()

# 학교검색
driver.find_element_by_xpath('//input[@title="학교 입력"]').click()

# 시/도
driver.find_element_by_xpath('//select/option[text()="서울특별시"]').click()

# 학교급
driver.find_element_by_xpath('//select/option[text()="고등학교"]').click()

# 학교명
driver.find_element_by_xpath('//input[@class="searchArea"]').send_keys('선린인터넷고등학교')

# 검색
driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click()
driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/p/a').click()

# 학교선택
driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()

# 성명
name = '강준하'
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
element = driver.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul/li/a')
driver.execute_script('arguments[0].click();', element)

# 1) 학생의 몸에 열이 있나요?
radio = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="container"]/div/div/div[2]/div[2]/dl[1]/dd/ul/li[1]/label')))
driver.execute_script("arguments[0].click();", radio)

# 2) 학생에게 코로나19가 의심되는 증상이 있나요?
radio = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="container"]/div/div/div[2]/div[2]/dl[2]/dd/ul/li[1]/label')))
driver.execute_script("arguments[0].click();", radio)

# 3) 학생이 최근(14일 이내) 해외여행을 다녀온 사실이 있나요?
radio = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="container"]/div/div/div[2]/div[2]/dl[3]/dd/ul/li[1]/label')))
driver.execute_script("arguments[0].click();", radio)

# 4) 동거가족 중 최근(14일 이내) 해외여행을 다녀온 사실이 있나요?
radio = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="container"]/div/div/div[2]/div[2]/dl[4]/dd/ul/li[1]/label')))
driver.execute_script("arguments[0].click();", radio)

# 5) 동거가족 중 현재 자가격리 중인 가족이 있나요?
radio = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="container"]/div/div/div[2]/div[2]/dl[5]/dd/ul/li[1]/label')))
driver.execute_script("arguments[0].click();", radio)

# 제출
driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()

driver.quit()

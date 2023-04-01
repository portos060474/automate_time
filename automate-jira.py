import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime
from calendar import monthrange


username = "your email" 
password = "your password" 
year = 23
month = "Feb"
remove_days = [13,14,15,16,17]
datetime_object = datetime.strptime(month, "%b")
month_number = datetime_object.month
# print(month_number)
month_number = datetime_object.month
_,max_days = monthrange(2000 + year,month_number)
# print(max_days)
days = [ x for x in range(1,max_days+1) ]
for day in remove_days:
	days.remove(day)
print(days)
# days.remove()


sys.exit()

driver = webdriver.Chrome('/Users/crco/Downloads/chromedriver') 
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://jira.computas.com/")

time.sleep(5)

print("login")
element = driver.find_element(by=By.ID, value='login-form-workaccount')
element.send_keys(f"{username}")
element.send_keys(Keys.RETURN)
time.sleep(5)

element = driver.find_element(by=By.XPATH, value='//*[@id="i0116"]')
element.send_keys(f"{username}")
element.send_keys(Keys.RETURN)
time.sleep(5)

element = driver.find_element(by=By.XPATH, value='//*[@id="i0118"]')
element.send_keys(f"{password}")
element.send_keys(Keys.RETURN)
time.sleep(10)

element = driver.find_element(by=By.ID, value='idSIButton9')
element.click()
time.sleep(10)

# TimesheetInfo_TimeDetailRecordList_0__DayList_2__UIEnterUnit

print(driver.title)

wait = WebDriverWait(driver, 100) # timeout after 10 seconds
results = wait.until(lambda driver: driver.find_element(by=By.ID, value='create-menu'))

driver.get("https://jira.computas.com/browse/CDCIK-1")
print("navigate to ticket")
time.sleep(10)

for day in days:

	d = datetime(year, datetime.strptime(month, "%b").month, day);
	if d.weekday() > 4:
		print('Given date is weekend.')
		continue
	else:
		print('Given data is weekday.')


	print("logging work")
	element = driver.find_element(by=By.ID, value='log-work-link')
	element.click()

	time.sleep(2)

	element = driver.find_element(by=By.ID, value='log-work-time-logged')
	element.send_keys("8")
	element = driver.find_element(by=By.ID, value='log-work-date-logged-date-picker')
	element.clear()
	print(f"{day}/{month}/{year} 1:55 PM")
	element.send_keys(f"{day}/{month}/{year} 1:55 PM")
	element = driver.find_element(by=By.ID, value='log-work-submit')
	element.click()
	time.sleep(2)

# element.send_keys(Keys.RETURN)








# search_bar.clear()
# search_bar.send_keys("getting started with python")




# driver.get("https://cdchrm.computas.com/client/#/")

# element = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/div/div/form/div[4]/div/input')
# element.send_keys('crco')
# element = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/div/div/form/div[5]/div/input')
# element.send_keys('Maimutikis2022!A')
# # element = driver.find_element_by_id("pass")
# # element.send_keys(password)
# element.send_keys(Keys.RETURN)
# print(driver.current_url)

# # primul buton "go to vacation plan"
# element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[3]/button'))).click()

# # log work"
# element = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/div/div/nav/div/form/span/button/span')
# element.click()

# time.sleep(5)
# element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[1]/div/div/div/div/input'))).send_keys('08.08.2022')
# # element = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div/div[2]/form/div[1]/div/div/div/div/input')
# # element.send_keys('08.06.2022')
# element = driver.find_element(by=By.NAME, value="startTime")
# element.clear()
# element.send_keys('09:00')
# element = driver.find_element(by=By.NAME, value="endTime")
# element.clear()
# element.send_keys('17:00')
time.sleep(25)
driver.close()
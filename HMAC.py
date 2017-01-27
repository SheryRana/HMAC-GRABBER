import pickle
import selenium.webdriver 

driver = selenium.webdriver.Chrome()
driver.get('http://www.adidas.co.uk/eqt-support-93-17-shoes/BB1234.html')
cookies_list = driver.get_cookies()
for cookie in cookies_list:
	print cookie

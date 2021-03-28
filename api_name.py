from selenium import webdriver
import time

driver =webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()

driver.find_element_by_name('wd').send_keys('surui')
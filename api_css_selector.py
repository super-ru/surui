from selenium import webdriver
import time

driver =webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
driver.maximize_window()

driver.find_element_by_css_selector('')
from selenium import webdriver
import time

driver =webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
driver.maximize_window()


driver.find_element_by_id('cart_num').click()#通过id去定位地方，然后如果想操作通过click去点击
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')


driver.find_element_by_xpath("//div[@class='schbox']/form/input[1]").send_keys('你说我真棒')
driver.find_element_by_xpath("//div[@class='schbox']/form/input[1]").send_keys(Keys.BACKSPACE)
driver.find_element_by_xpath("//div[@class='schbox']/form/input[1]").send_keys(Keys.CONTROL,'x')
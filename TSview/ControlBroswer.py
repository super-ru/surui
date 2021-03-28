from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
driver.maximize_window()

driver.find_element_by_link_text('秒杀').click()

driver.refresh()#当前页面的刷新
time.sleep(2)
driver.back()#从当前页面返回上一级页面
time.sleep(2)
driver.forward()#前进

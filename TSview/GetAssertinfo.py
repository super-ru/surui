from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
driver.maximize_window()


tittle = driver.title#获取你的标题信息
print(tittle)

#获取你当前页面的地址信息
driver.find_element_by_link_text('首页').click()
url = driver.current_url
print(url)
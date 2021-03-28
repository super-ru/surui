from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver =webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
driver.maximize_window()

#对于下拉选择框通过select_by_visible_text()
s = driver.find_element_by_id("J_roomCountList")
Select(s).select_by_visible_text("2间")

Select(s).select_by_index(3)
#通过select_by_value("  ")去选择下拉选择框
Select(s).select_by_value("5")#s里面的内容在init里面
#只有运用了select标签才能使用select类里面的方法
from selenium.webdriver.common.action_chains import ActionChains
#/路径：External/Lib/site packages/selenium/webdriver/common/action_chains.py
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
driver.maximize_window()

#移动鼠标到某个控件位置上
case03=driver.find_element_by_link_text('男上衣')
ActionChains(driver).move_to_element(case03).perform()#perform 实现你所有的动作

#右击某个控件
ActionChains(driver).context_click(case03)

#双击某个控件
ActionChains(driver).double_click(case03)


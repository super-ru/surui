from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')

#设置浏览器固定尺寸
driver.set_window_size(800,1000)#第一个宽，第二个高度

time.sleep(2)

#设置浏览器最大化
driver.maximize_window()
time.sleep(2)
driver.set_window_size(800,1000)
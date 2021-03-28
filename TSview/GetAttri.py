#属性的获取
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
driver.maximize_window()
#获取某一个控件的尺寸，属性方法没有（）
size=driver.find_element_by_xpath("//div[@class='schbox']/form/input[1]").size
print(type(size))#字典类型
print(size)
print(size['height'])#获取字典类型的值
time.sleep(2)
#获取控件上的文本信息,属性方法没有（）
#运用非常广泛
text=driver.find_element_by_xpath("//span[@class='name']/em").text
print(type(text))
print(text)

#获取控件上的控件对应的属性值
case=driver.find_element_by_xpath("//div[@class='schbox']/form/input[2]").get_attribute('value')
print(case)

#判断控件是否显示出来：布尔类型
driver.find_element_by_xpath("//div[@class='schbox']/form/input[1]").send_keys('nike')
case02=driver.find_element_by_xpath("//div[@class='schbox']/form/input[1]").is_displayed()
print(case02)
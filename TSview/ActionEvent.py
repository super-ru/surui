from selenium import  webdriver
import  time
driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
driver.maximize_window()


#在搜索框发送信息
driver.find_element_by_xpath("//div[@class='schbox']/form/input[1]").send_keys('nike')
time.sleep(2)
#清空搜索框
driver.find_element_by_xpath("//div[@class='schbox']/form/input[1]").clear()
time.sleep(2)
#对于任何的控件都能够进行点击操作
driver.find_element_by_xpath("//div[@class='schbox']/form/input[1]").send_keys('surui')
driver.find_element_by_xpath("//div[@class='schbox']/form/input[2]").click()
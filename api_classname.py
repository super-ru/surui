from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()

driver.find_element_by_class_name('soutu-btn').click()#对于 class中含有复合类的不建议用其去定位
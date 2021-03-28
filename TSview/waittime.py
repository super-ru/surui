from selenium import  webdriver
import  time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
driver.maximize_window()


driver.find_element_by_xpath("//div[@class='schbox']/form/input[1]")
#强制等待时间
time.sleep(2)
#如果是from time import sleep
#直接sleep（2）

#隐式等待时间
driver.implicitly_wait(10)

#显示等待时间
ele=WebDriverWait(driver,15,0.5).until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='schbox']/form/input[1]")))
ele.sen_keys('123456')#最大等待时间是15s ,每个0.5s去检查一次直到当前页面加载出了xpath路径下的控件为止
time.sleep(2)
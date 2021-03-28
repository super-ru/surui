
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'
desired_caps['appActivity'] = '.ui.base.SplashActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(40)
driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/iconTabItem")[1].click()

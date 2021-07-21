from appium import webdriver
import os,time
from logs import logger



def starUp():
    logger.info('启动中。。。。')
    desire_caps = {
        # "deviceName": "C7YVB20526000119",
        "deviceName": "127.0.0.1:21503",
        "platformName": "Android",
        # "platformVersion": "10",
        "platformVersion": "5.1.1",
        "appPackage":"com.ss.android.article.news",
        "appActivity":"com.ss.android.article.news.activity.MainActivity",
        "noReset" : True,
        "unicodeKeyboard": True
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_caps)
    logger.info('启动成功，等待6s')
    time.sleep(1)
    # 定位元素，进行操作
    # driver.find_element()
    # 关闭app

if __name__ == '__main__':
    starUp()
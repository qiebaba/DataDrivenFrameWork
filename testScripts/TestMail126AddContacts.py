from selenium import webdriver
from appModules.LoginAction import LoginAction
import time
from util.ParseExcel import ParseExcel
from config.VarConfig import *

excelObj = ParseExcel()
excelObj.loadWorkBook(dataFilePath)

def testMailLogin():
    try:
        driver=webdriver.Firefox()
        driver.get("http://mail.126.com")
        driver.implicitly_wait(30)
        driver.maximize_window()
        LoginAction.login(driver,"aaaa","bbbb")
        time.sleep(5)
        assert u"未读邮件" in driver.page_source
    except Exception as e:
        raise e
    finally:
        driver.quit()

if __name__ == '__main__':
    testMailLogin()
    print(u"登录邮箱成功")
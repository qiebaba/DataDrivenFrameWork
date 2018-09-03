from util.ObjectMap import *
from util.ParseConfigurationFile import ParseCofigFile
class LoginPage():

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseCofigFile()
        self.loginOptions = self.parseCF.getItemsSection("126mail_login")

    def switchToFram(self):
        try:
            locatorExperssion = self.loginOptions["loginPage.frame".lower()].split(":")[1]
            self.driver.switch_to.frame(locatorExperssion)
        except Exception as e:
            raise e

    def switchToDefaultFrame(self):
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            raise e

    def userNameObj(self):
        try:
            locateType,locatorExperssion = self.loginOptions["loginPage.username".lower()].split(":")
            elementObj = getElement(self.driver,locateType,locatorExperssion)
            return elementObj
        except Exception as e:
            raise e

    def passwordObj(self):
        try:
            locateType,locatorExperssion = self.loginOptions["loginPage.password".lower()].split(":")
            elementObj = getElement(self.driver,locateType,locatorExperssion)
            return elementObj
        except Exception as e:
            raise e

    def loginButton(self):
        try:
            locateType,locatorExperssion = self.loginOptions["loginPage.loginbutton".lower()].split(":")
            elementObj = getElement(self.driver,locateType,locatorExperssion)
            return elementObj
        except Exception as e:
            raise e

if __name__ == '__main__':
    from selenium import webdriver
    driver =webdriver.Firefox()
    driver.get("http://mail.126.com")
    import time
    time.sleep(5)
    login =  LoginPage(driver)
    login.switchToFram()
    login.userNameObj().send_keys("aaaa")
    login.passwordObj().send_keys("bbbb")
    login.loginButton().click()
    login.switchToDefaultFrame()
    assert u"未读邮件" in driver.page_source
    driver.quit()
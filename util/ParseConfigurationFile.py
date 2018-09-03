import configparser    #configparser模块
from config.VarConfig import pageElementLocatorPath

class ParseCofigFile():
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(pageElementLocatorPath)

    #读取配置文件
    def getItemsSection(self,sectionName):
        optionsDict = dict(self.cf.items(sectionName))
        return optionsDict
    def getOptionValue(self,sectionName,optionName):
        value = self.cf.get(sectionName,optionName)
        return value

if __name__ == '__main__':
    pc = ParseCofigFile()
    print(pc.getItemsSection("126mail_login"))
    print(pc.getOptionValue("126mail_login","loginpage.frame"))
#定义全局变量
import os

#当前文件所在目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#页面元素文件的绝对路径
pageElementLocatorPath = os.path.join(parentDirPath,"config\\PageElementLocator.ini")

#数据文件存放路径
dataFilePath = parentDirPath+u"\\testData\\testdata.xlsx"

#126账号表
account_username = 2
account_password = 3
account_dataBook = 4
account_isExecute = 5
account_testResult = 6

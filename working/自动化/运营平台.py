from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Operation_platform:
    def __init__(self,mechanism_name='',path='http://192.168.0.58:81/#/Login',userphone='18888888888',password='123456'):
        self.driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        self.mechanism_name = mechanism_name
        self.path = path
        self.userphone = userphone
        self.password = password
        self.login(path=self.path,userphone=self.userphone,password=self.password)

    def login(self,path='http://192.168.0.58:81/#/Login',userphone='18888888888',password='123456'):
        login_dict = {
            '账号': ['//*[@id="app"]/div/section/aside/div/div[2]/form/div[2]/div/div/input', userphone],
            '密码': ['//*[@id="app"]/div/section/aside/div/div[2]/form/div[4]/div/div/input', password],
            '登录': '//*[@id="app"]/div/section/aside/div/div[2]/div/span'
        }

        self.driver.maximize_window()
        self.driver.get(path)

        for i in login_dict:
            if i == '登录':
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, login_dict['登录']))
                )
                self.driver.find_element_by_xpath(login_dict['登录']).click()
            else:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, login_dict[i][0]))
                )
                self.driver.find_element_by_xpath(login_dict[i][0]).send_keys(login_dict[i][1])

    def Merchant_management(self):
        Platform_name = '资产系统'
        Module_name1 = '业务管理'
        Module_name2 = '业务配置'
        Module_name3 = '平台服务'
        Module_name4 = '流程中心'
        Module_name5 = '客户管理'

        Platform_name2 = '公共服务'
        Module_name6 = 'OA管理'
        Module_name7 = '系统设置'
        Module_name8 = '个人中心'


        Merchant_management_dict = {
            '搜索框' : ['文本','//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div[1]/input',self.mechanism_name],
            '查询按钮' : ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/button[1]'],
            '修改' : ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[4]/div[2]/table/tbody/tr/td[11]/div/span[1]'],
            '合作平台' : ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[2]/div[12]/div/div/div[1]/div[2]/input'],
            '合作平台-值1' : ['按钮','/html/body/div[3]/div[1]/div[1]/ul/li[1]'],
            '展开业务管理' : ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name + '"]/../../div[2]//div/div/span[text()="' + Module_name1 + '"]/../span'],
            '勾选业务导航' : ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name + '"]/../../div[2]//div/div/span[text()="' + Module_name1 + '"]/../../div[2]//div/div/span[text()="业务导航"]/../label'],
            '勾选面签管理' : ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name + '"]/../../div[2]//div/div/span[text()="' + Module_name1 + '"]/../../div[2]//div/div/span[text()="面签管理"]/../label'],
            '勾选核行管理' : ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name + '"]/../../div[2]//div/div/span[text()="' + Module_name1 + '"]/../../div[2]//div/div/span[text()="核行管理"]/../label'],
            '勾选打折申请' : ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name + '"]/../../div[2]//div/div/span[text()="' + Module_name1 + '"]/../../div[2]//div/div/span[text()="打折申请"]/../label'],
            '展开业务导航' : ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name + '"]/../../div[2]//div/div/span[text()="' + Module_name1 + '"]/../../div[2]//div/div/span[text()="业务导航"]/../span[1]'],
            '反选担保单合同录入' : ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name + '"]/../../div[2]//div/div/span[text()="' + Module_name1 + '"]/../../div[2]//div/div/span[text()="业务导航"]/../../div[2]//div/div/span[text()="担保单合同录入"]/../label'],
            '反选担保单查档查看' : ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name + '"]/../../div[2]//div/div/span[text()="' + Module_name1 + '"]/../../div[2]//div/div/span[text()="业务导航"]/../../div[2]//div/div/span[text()="担保单查档查看"]/../label'],
            '反选修改要件' : ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name + '"]/../../div[2]//div/div/span[text()="' + Module_name1 + '"]/../../div[2]//div/div/span[text()="业务导航"]/../../div[2]//div/div/span[text()="修改要件"]/../label'],
            # '反选单据详情-费用修改' : ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name + '"]/../../div[2]//div/div/span[text()="' + Module_name1 + '"]/../../div[2]//div/div/span[text()="业务导航"]/../../div[2]//div/div/span[text()="单据详情-费用修改"]/../label'],
            '展开业务配置': ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name + '"]/../../div[2]//div/div/span[text()="' + Module_name2 + '"]/../span'],
            '勾选报单模板管理': ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name + '"]/../../div[2]//div/div/span[text()="' + Module_name2 + '"]/../../div[2]//div/div/span[text()="报单模板管理"]/../label'],
            '勾选银行管理': ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name + '"]/../../div[2]//div/div/span[text()="' + Module_name2 + '"]/../../div[2]//div/div/span[text()="银行管理"]/../label'],
            '勾选合作方管理': ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name + '"]/../../div[2]//div/div/span[text()="' + Module_name2 + '"]/../../div[2]//div/div/span[text()="合作方管理"]/../label'],
            '勾选业务类型设置': ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name + '"]/../../div[2]//div/div/span[text()="' + Module_name2 + '"]/../../div[2]//div/div/span[text()="业务类型设置"]/../label'],
            '勾选平台服务': ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name + '"]/../../div[2]//div/div/span[text()="' + Module_name3 + '"]/../label'],
            '展开平台服务': ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name + '"]/../../div[2]//div/div/span[text()="' + Module_name3 + '"]/../span'],
            '反选二次还款': ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name + '"]/../../div[2]//div/div/span[text()="' + Module_name3 + '"]/../../div[2]//div/div/span[text()="二次还款"]/../label'],
            '反选保函管理': ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name + '"]/../../div[2]//div/div/span[text()="' + Module_name3 + '"]/../../div[2]//div/div/span[text()="保函管理"]/../label'],
            '勾选流程中心': ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name + '"]/../../div[2]//div/div/span[text()="' + Module_name4 + '"]/../label'],
            '展开流程中心': ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name + '"]/../../div[2]//div/div/span[text()="' + Module_name4 + '"]/../span'],
            '反选流程监控（旧）': ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name + '"]/../../div[2]//div/div/span[text()="' + Module_name4 + '"]/../../div[2]//div/div/span[text()="流程监控（旧）"]/../label'],
            '勾选客户管理': ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name + '"]/../../div[2]//div/div/span[text()="' + Module_name5 + '"]/../label'],
            '勾选OA管理': ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name2 + '"]/../../div[2]//div/div/span[text()="' + Module_name6 + '"]/../label'],
            '勾选系统设置': ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name2 + '"]/../../div[2]//div/div/span[text()="' + Module_name7 + '"]/../label'],
            '展开系统设置': ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name2 + '"]/../../div[2]//div/div/span[text()="' + Module_name7 + '"]/../span'],
            '勾选个人中心': ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name2 + '"]/../../div[2]//div/div/span[text()="' + Module_name8 + '"]/../label'],
            '反选法定假日管理': ['按钮','//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/form/div[8]/div/div//div/div/span[text()="' + Platform_name2 + '"]/../../div[2]//div/div/span[text()="' + Module_name7 + '"]/../../div[2]//div/div/span[text()="法定假日管理"]/../label'],

        }

        for i in Merchant_management_dict:
            if Merchant_management_dict[i][0] == '文本':
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, Merchant_management_dict[i][1]))
                )
                self.driver.find_element_by_xpath(Merchant_management_dict[i][1]).send_keys(Merchant_management_dict[i][2])
            # elif i =='勾选报单模板管理':
            #     bug=self.driver.find_element_by_xpath(Merchant_management_dict[i][1])
            #     print(bug.get_attribute('outerHTML'))
            else:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, Merchant_management_dict[i][1]))
                )

                # 拖动滚动条到target元素位置上
                try:
                    target = Merchant_management_dict[i][1]
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
                except:
                    pass
                #点击按钮
                self.driver.find_element_by_xpath(Merchant_management_dict[i][1]).click()


if __name__ == '__main__':
    o = Operation_platform(mechanism_name='四川众信汇丰金融服务外包有限公司',path='http://op.fangdaiyun.cn/#/Login',userphone='18888888888',password='FDY2020')
    o.Merchant_management()
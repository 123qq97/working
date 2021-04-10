from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class Automatic_integration:
    def __init__(self,path='http://192.168.0.58:82',userphone='17666121214',password='',user_name='',business_name=''):
        self.driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        self.path = path
        self.login_url = self.path + '/login'
        self.userphone= userphone
        self.password = password
        self.business_name = business_name
        self.login(path=self.login_url,userphone=self.userphone,password=self.password)
        self.Process_center()

    #登录
    def login(self,path='http://192.168.0.58:82/login',userphone='17666121214',password=''):
        if password == '':
            password =userphone[-6:]

        login_dict = {
            '账号': ['//*[@id="app"]/div/section/aside/div/div[2]/form/div[2]/div/div/input',userphone],
            '密码': ['//*[@id="app"]/div/section/aside/div/div[2]/form/div[4]/div/div/input',password],
            '登录': '//*[@id="app"]/div/section/aside/div/div[2]/div/span'
        }

        self.driver.maximize_window()
        self.driver.get(path)

        #判断是否为登录
        for i in login_dict:
            if i == '登录':
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, login_dict['登录']))
                )
                self.driver.find_element_by_xpath(login_dict['登录']).click()
            else:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, login_dict[i][0]))
                )
                self.driver.find_element_by_xpath(login_dict[i][0]).send_keys(login_dict[i][1])

    #流程中心
    def Process_center(self):
        # 左侧菜单1
        menu_name1 = '流程管理-新1'
        menu_name1_sub1='功能类型管理'
        menu_name1_sub2='节点管理'
        menu_name1_sub3='事项管理'
        menu_name1_sub4='流程配置'

        Process_center_dict = {
            '展开流程中心': ['按钮','//*[@id="app"]/section/section/aside/div/div/div[1]/div/ul//li/div/span[text()="' + menu_name1 + '"]/../i[2]'],
            '流程配置': ['按钮','//*[@id="app"]/section/section/aside/div/div/div[1]/div/ul//li/div/span[text()="' + menu_name1 + '"]/../../ul//li[text()="' + menu_name1_sub4 + '"]'],
            '流程配置-新建流程': ['按钮', '//*[@id="pane-first"]/div/div[1]/div/div/button[3]/span'],

        }

        for i in Process_center_dict:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, Process_center_dict[i][1]))
            )

            #文本操作
            if Process_center_dict[i][0] == '文本':
                #执行输入文本
                element = self.driver.find_element_by_xpath(Process_center_dict[i][1])
                element.clear()
                element.send_keys(Process_center_dict[i][2])

            #按钮操作
            else:
                # 拖动滚动条到target元素位置上
                try:
                    target = Process_center_dict[i][1]
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
                except:
                    pass

                #执行点击
                time.sleep(0.2)
                element = self.driver.find_element_by_xpath(Process_center_dict[i][1])
                self.driver.execute_script("arguments[0].click();", element)                #使用js点击
                time.sleep(0.6)

if __name__ == '__main__':
    a = Automatic_integration(userphone='13377121517',password='121517')
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time

class Automatic_integration:
    def __init__(self,path='http://192.168.0.58:82',userphone='17666121214',password='',user_name='',business_name=''):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
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
        #流程配置需增加的变量
        add_y = 0

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
            '开始/结束节点': ['移动','//*[@id="mainBox"]/div[2]/div/div/div[1]/div/ul/li[1]/ul/li/ul/div//li','//*[@id="flowContainer"]'],
            '报单/审查节点': ['移动','//*[@id="mainBox"]/div[2]/div/div/div[1]/div/ul/li[2]/ul/li/ul/div//li','//*[@id="flowContainer"]'],
            '开始-报单': ['连线','//*[@id="flowContainer"]//div/div/span[text()="开始节点"]/../i','//*[@id="flowContainer"]//div/div/span[text()="报单"]'],
            '报单-审查': ['连线','//*[@id="flowContainer"]//div/div/span[text()="报单"]/../i','//*[@id="flowContainer"]//div/div/span[text()="审查"]'],
            '审查-结束': ['连线','//*[@id="flowContainer"]//div/div/span[text()="审查"]/../i','//*[@id="flowContainer"]//div/div/span[text()="结束节点"]'],
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
            elif Process_center_dict[i][0] == '按钮':
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

            elif Process_center_dict[i][0] == '移动':
                # 元素列表
                drag_to = self.driver.find_elements_by_xpath(Process_center_dict[i][1])
                to_drop = self.driver.find_element_by_xpath(Process_center_dict[i][2])
                drag_to_list = {}

                #筛选出节点放入drag_to_list
                for li in drag_to:
                    if '开始节点' in li.text :
                        drag_to_list[0] = li
                    elif '结束节点' in li.text:
                        drag_to_list[3] = li
                    elif '报单' in li.text:
                        drag_to_list[1] = li
                    elif '审查' in li.text:
                        drag_to_list[2] = li

                for drage_path in drag_to_list:
                    # 拖动滚动条到target元素位置上(1331 229)
                    try:
                        target = drag_to_list[drage_path]
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                    except:
                        pass

                    # 节点的y轴位置增加对应100px
                    add_y = 100 * int(drage_path)

                    #被拖拽元素的x，y轴节点
                    drage_to_x = drag_to_list[drage_path].location['x']+150
                    drage_to_y = drag_to_list[drage_path].location['y']+250

                    #判断节点为报单、审查，y轴增加300px
                    if drage_path == 1 or drage_path == 2:
                        drage_to_y = drag_to_list[drage_path].location['y'] + 300

                    #执行拖拽
                    pyautogui.moveTo(drage_to_x, drage_to_y)
                    pyautogui.dragTo(to_drop.location['x']+550,to_drop.location['y']+250+add_y,duration=0.3)

            else:
                drag_to = self.driver.find_element_by_xpath(Process_center_dict[i][1])
                to_drop = self.driver.find_element_by_xpath(Process_center_dict[i][2])
                drage_to_x = drag_to.location['x']+210
                drage_to_y = drag_to.location['y']+215
                to_drop_x = to_drop.location['x']+180
                to_drop_y = to_drop.location['y']+240

                if i == '报单-审查':
                    drage_to_y = drag_to.location['y'] + 235
                    to_drop_y = to_drop.location['y'] + 260
                elif i == '审查-结束':
                    drage_to_y = drag_to.location['y'] + 255
                    to_drop_y = to_drop.location['y'] + 280

                pyautogui.moveTo(drage_to_x, drage_to_y)
                pyautogui.dragTo(to_drop_x,to_drop_y , duration=0.3)


if __name__ == '__main__':
    a = Automatic_integration(userphone='13377121517',password='121517',path='http://189i0341c8.iok.la:27031')
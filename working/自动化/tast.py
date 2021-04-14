from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time

class Automatic_integration:
    def __init__(self,path='http://192.168.0.58:82',userphone='17666121214',password='',user_name='',business_name=''):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        self.path = path
        self.login_url = self.path + '/login'
        self.userphone= userphone
        self.password = password
        self.business_name = business_name
        self.login(path=self.login_url,userphone=self.userphone,password=self.password)
        # self.Process_center()
        self.businessType()

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
            '流程配置-新建流程-流程名称': ['文本', '//*[@id="mainBox"]/div[1]/form/div/div[1]/div/div/input','业务主流程'],
            '流程配置-新建流程-所属功能类型': ['按钮', '//*[@id="mainBox"]/div[1]/form/div/div[3]/div/div/div[1]/input'],
            '流程配置-新建流程-所属功能类型-业务主流程': ['按钮', '/html/body/div[2]/div[1]/div[1]/ul//li/span[text()="业务主流程"]'],
            '开始/结束节点': ['移动','//*[@id="mainBox"]/div[2]/div/div/div[1]/div/ul/li[1]/ul/li/ul/div//li','//*[@id="flowContainer"]'],
            '报单/审查节点': ['移动','//*[@id="mainBox"]/div[2]/div/div/div[1]/div/ul/li[2]/ul/li/ul/div//li','//*[@id="flowContainer"]'],
            '开始-报单': ['连线','//*[@id="flowContainer"]//div/div/span[text()="开始节点"]/../i','//*[@id="flowContainer"]//div/div/span[text()="报单"]'],
            '报单-审查': ['连线','//*[@id="flowContainer"]//div/div/span[text()="报单"]/../i','//*[@id="flowContainer"]//div/div/span[text()="审查"]'],
            '审查-结束': ['连线','//*[@id="flowContainer"]//div/div/span[text()="审查"]/../i','//*[@id="flowContainer"]//div/div/span[text()="结束节点"]'],
            '报单-节点设置-编辑按钮': ['按钮','//div[@id="flowContainer"]//div/div/span[text()="报单"]/../div/i'],
            '报单-节点设置-事项名称': ['按钮','//*[@id="pane-first"]/div/div[3]/div/div[3]/table/tbody/tr/td[2]/div/div/div/div/div/input'],
            '报单-节点设置-事项名称-报单': ['按钮','/html/body/div[5]/div[1]/div[1]/ul//li/span[text()="报单"]'],
            '报单-节点设置-必要事项': ['按钮','//*[@id="pane-first"]/div/div[3]/div/div[3]/table/tbody/tr/td[3]/div/div/div/div/div[1]/input'],
            '报单-节点设置-必要事项-是': ['按钮','/html/body/div[6]/div[1]/div[1]/ul//li/span[text()="是"]'],
            '报单-节点设置-通过条件key': ['按钮','//*[@id="pane-first"]/div/div[3]/div/div[3]/table/tbody/tr/td[4]/div/div[1]/div/div/div[1]/input'],
            '报单-节点设置-通过条件key-等于': ['按钮','/html/body/div[7]/div[1]/div[1]/ul//li/span[text()="等于"]'],
            '报单-节点设置-通过条件value': ['按钮','//*[@id="pane-first"]/div/div[3]/div/div[3]/table/tbody/tr/td[4]/div/div[2]/div/div/div/input'],
            '报单-节点设置-通过条件value-已报单': ['按钮','/html/body/div[8]/div[1]/div[1]/ul//li/span[text()="已报单"]'],
            '报单-节点设置-顺序': ['文本','//*[@id="pane-first"]/div/div[3]/div/div[3]/table/tbody/tr/td[8]/div/div/div/div/input','1'],
            '报单-节点设置-保存': ['按钮','/html/body/div[4]/div/div[3]/span//button/span[text()="确定"]'],
            '审查-节点设置-编辑按钮': ['按钮', '//div[@id="flowContainer"]//div/div/span[text()="审查"]/../div/i'],
            '审查-节点设置-事项名称1': ['按钮','//*[@id="pane-first"]/div/div[3]/div/div[3]/table/tbody/tr/td[2]/div/div/div/div/div/input'],
            '审查-节点设置-事项名称1-审查员接收': ['按钮', '/html/body/div[5]/div[1]/div[1]/ul//li/span[text()="审查员接收"]'],
            '审查-节点设置-必要事项1': ['按钮','//*[@id="pane-first"]/div/div[3]/div/div[3]/table/tbody/tr/td[3]/div/div/div/div/div[1]/input'],
            '审查-节点设置-必要事项1-是': ['按钮', '/html/body/div[6]/div[1]/div[1]/ul//li/span[text()="是"]'],
            '审查-节点设置-通过条件key1': ['按钮','//*[@id="pane-first"]/div/div[3]/div/div[3]/table/tbody/tr/td[4]/div/div[1]/div/div/div[1]/input'],
            '审查-节点设置-通过条件key1-等于': ['按钮', '/html/body/div[7]/div[1]/div[1]/ul//li/span[text()="等于"]'],
            '审查-节点设置-通过条件value1': ['按钮','//*[@id="pane-first"]/div/div[3]/div/div[3]/table/tbody/tr/td[4]/div/div[2]/div/div/div/input'],
            '审查-节点设置-通过条件value1-已接收': ['按钮', '/html/body/div[8]/div[1]/div[1]/ul//li/span[text()="已接收"]'],
            '审查-节点设置-顺序1': ['文本','//*[@id="pane-first"]/div/div[3]/div/div[3]/table/tbody/tr/td[8]/div/div/div/div/input','1'],
            '审查-节点设置-新增': ['按钮','//*[@id="pane-first"]/div/div[3]/div/div[4]/div[2]/table/tbody/tr//td/div/span[text()="新增"]'],
            '审查-节点设置-事项名称2': ['按钮','//*[@id="pane-first"]/div/div[3]/div/div[3]/table/tbody/tr[2]/td[2]/div/div/div/div/div[1]/input'],
            '审查-节点设置-事项名称2-审查': ['按钮','/html/body/div[9]/div[1]/div[1]/ul//li/span[text()="审查"]'],
            '审查-节点设置-必要事项2': ['按钮','//*[@id="pane-first"]/div/div[3]/div/div[3]/table/tbody/tr[2]/td[3]/div/div/div/div/div[1]/input'],
            '审查-节点设置-必要事项2-是': ['按钮', '/html/body/div[10]/div[1]/div[1]/ul//li/span[text()="是"]'],
            '审查-节点设置-通过条件key2': ['按钮','//*[@id="pane-first"]/div/div[3]/div/div[3]/table/tbody/tr[2]/td[4]/div/div[1]/div/div/div[1]/input'],
            '审查-节点设置-通过条件key2-等于': ['按钮', '/html/body/div[11]/div[1]/div[1]/ul//li/span[text()="等于"]'],
            '审查-节点设置-通过条件value2': ['按钮','//*[@id="pane-first"]/div/div[3]/div/div[3]/table/tbody/tr[2]/td[4]/div/div[2]/div/div/div/input'],
            '审查-节点设置-通过条件value2-已审查': ['按钮', '/html/body/div[12]/div[1]/div[1]/ul//li/span[text()="已审查"]'],
            '审查-节点设置-顺序2': ['文本','//*[@id="pane-first"]/div/div[3]/div/div[3]/table/tbody/tr[2]/td[8]/div/div/div/div/input','2'],
            '审查-节点设置-保存': ['按钮', '/html/body/div[4]/div/div[3]/span//button/span[text()="确定"]'],
            '流程配置-新建流程-保存': ['按钮','//*[@id="mainBox"]/div[3]/div/button[1]/span[text()="保存"]'],
        }

        for i in Process_center_dict:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, Process_center_dict[i][1]))
            )

            # 拖动滚动条到target元素位置上
            try:
                target = Process_center_dict[i][1]
                self.driver.execute_script("arguments[0].scrollIntoView();", target)
            except:
                pass

            #文本操作
            if Process_center_dict[i][0] == '文本':
                #执行输入文本
                element = self.driver.find_element_by_xpath(Process_center_dict[i][1])
                element.clear()
                element.send_keys(Process_center_dict[i][2])

            #按钮操作
            elif Process_center_dict[i][0] == '按钮':
                #执行点击
                time.sleep(0.2)
                element = self.driver.find_element_by_xpath(Process_center_dict[i][1])
                self.driver.execute_script("arguments[0].click();", element)                #使用js点击
                time.sleep(0.6)

            #拖拽操作
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
                    # 节点的y轴位置增加对应100px
                    add_y = 100 * int(drage_path)

                    #被拖拽元素的x，y轴节点
                    drage_to_x = drag_to_list[drage_path].location['x']+150
                    drage_to_y = drag_to_list[drage_path].location['y']+130

                    #判断节点为报单、审查，y轴增加300px
                    if drage_path == 1 or drage_path == 2:
                        drage_to_y = drag_to_list[drage_path].location['y'] + 150

                    #执行拖拽
                    pyautogui.moveTo(drage_to_x, drage_to_y)
                    pyautogui.dragTo(to_drop.location['x']+550,to_drop.location['y']+250+add_y,duration=0.3)

            #连线操作
            else:
                #连线的开始drag_to、结束元素to_drag的位置
                drag_to = self.driver.find_element_by_xpath(Process_center_dict[i][1])
                to_drop = self.driver.find_element_by_xpath(Process_center_dict[i][2])
                #分辨率不同产生的偏差，开始/结束的x、y轴进行微调
                drage_to_x = drag_to.location['x']+10
                drage_to_y = drag_to.location['y']+120
                to_drop_x = to_drop.location['x']-20
                to_drop_y = to_drop.location['y']+130

                #每个节点的y轴位置微调
                if i == '报单-审查':
                    drage_to_y = drag_to.location['y'] + 125
                    to_drop_y = to_drop.location['y'] + 160
                elif i == '审查-结束':
                    drage_to_y = drag_to.location['y'] + 130
                    to_drop_y = to_drop.location['y'] + 140

                pyautogui.moveTo(drage_to_x, drage_to_y)
                pyautogui.dragTo(to_drop_x,to_drop_y , duration=0.3)

    #业务类型设置
    def businessType(self):
        #左侧菜单
        menu_name1 = '业务配置'
        menu_name1_sub1 = '业务类型设置'

        businessType_dict = {
            '展开业务配置': ['按钮','//*[@id="app"]/section/section/aside/div/div/div[1]/div/ul//li/div/span[text()="' + menu_name1 + '"]/../i[2]'],
            '业务类型设置': ['按钮','//*[@id="app"]/section/section/aside/div/div/div[1]/div/ul//li/div/span[text()="' + menu_name1 + '"]/../../ul//li[text()="' + menu_name1_sub1 + '"]'],
            '新增业务类型按钮': ['按钮','//*[@id="mainBox"]/div[1]/div//button/span[text()="业务类型"]'],

            '（交易现金）基本信息-业务名称': ['文本','//*[@id="pane-first"]/div/div/div/div/form//div/label[text()="业务名称："]/../div/div/input','交易类现金赎楼'],
            '（交易现金）基本信息-分公司': ['按钮','//*[@id="pane-first"]/div/div/div/div/form//div/label[text()="分公司："]/../div/div/div/input'],
            '（交易现金）基本信息-分公司-选中第一个': ['按钮','/html/body/div[3]/div[1]/div[1]/ul/li/span'],
            '（交易现金）基本信息-资金分类': ['按钮','//*[@id="pane-first"]/div/div/div/div/form//div/label[text()="资金分类："]/../div/div/div/input'],
            '（交易现金）基本信息-资金分类-选中现金': ['按钮','/html/body/div[4]/div[1]/div[1]/ul//li/span[text()="现金"]'],
            '（交易现金）基本信息-报单模板': ['按钮','//*[@id="pane-first"]/div/div/div/div/form//div/label[text()="报单模板："]/../div/div/div/input'],
            '（交易现金）基本信息-报单模板-选中第二个值': ['按钮','/html/body/div[5]/div[1]/div[1]/ul/li[2]/span'],
            '（交易现金）基本信息-产品类型': ['按钮','//*[@id="pane-first"]/div/div/div/div/form//div/label[text()="产品类型："]/../div/div/span/span/span'],
            '（交易现金）基本信息-产品类型-选中产品': ['按钮','/html/body/div[6]/div/div[2]/div/div/div[3]/table/tbody/tr/td[1]'],
            '（交易现金）基本信息-产品类型-保存': ['按钮','/html/body/div[6]/div/div[3]/span/button[2]//span[text()="确 定"]'],
            '（交易现金）基本信息-下一步': ['按钮','//*[@id="mainBox"]/div[3]/div/div/div[3]/span//button/span[text()="下一步"]'],
            '（交易现金）费率设置-是否开启收费-否': ['按钮','//*[@id="pane-second"]/div/div/div/div/form/div/div/div/div/div/label[2]/span[1]'],
            '（交易现金）费率设置-下一步': ['按钮', '//*[@id="mainBox"]/div[3]/div/div/div[3]/span//button/span[text()="下一步"]'],
            '（交易现金）资料设置-下一步': ['按钮', '//*[@id="mainBox"]/div[3]/div/div/div[3]/span//button/span[text()="下一步"]'],
            '（交易现金）平台资料-下一步': ['按钮', '//*[@id="mainBox"]/div[3]/div/div/div[3]/span//button/span[text()="下一步"]'],
            '（交易现金）流程配置-关联流程': ['按钮', '//*[@id="pane-flowset"]/div/div/div[3]/table/tbody/tr/td[4]/div/div/div[1]/input'],
            '（交易现金）流程配置-关联流程-选中流程': ['按钮', '/html/body/div[6]/div[1]/div[1]/ul/li[1]'],
            '（交易现金）业务配置-保存': ['按钮', '//*[@id="mainBox"]/div[3]/div/div/div[3]/span//button/span[text()="保存"]'],

            '（非交易现金）基本信息-业务名称': ['文本','//*[@id="pane-first"]/div/div/div/div/form//div/label[text()="业务名称："]/../div/div/input','非交易类现金赎楼'],
            '（非交易现金）基本信息-分公司': ['按钮','//*[@id="pane-first"]/div/div/div/div/form//div/label[text()="分公司："]/../div/div/div/input'],
            '（非交易现金）基本信息-分公司-选中第一个': ['按钮', '/html/body/div[3]/div[1]/div[1]/ul/li/span'],
            '（非交易现金）基本信息-交易类型': ['按钮','//*[@id="pane-first"]/div/div/div/div/form//div/label[text()="交易类型："]/../div/div/div/input'],
            '（非交易现金）基本信息-资金分类-选中非交易类': ['按钮', '/html/body/div[4]/div[1]/div[1]/ul//li/span[text()="非交易类"]'],
            '（非交易现金）基本信息-资金分类': ['按钮','//*[@id="pane-first"]/div/div/div/div/form//div/label[text()="资金分类："]/../div/div/div/input'],
            '（非交易现金）基本信息-资金分类-选中现金': ['按钮', '/html/body/div[5]/div[1]/div[1]/ul//li/span[text()="现金"]'],
            '（非交易现金）基本信息-报单模板': ['按钮','//*[@id="pane-first"]/div/div/div/div/form//div/label[text()="报单模板："]/../div/div/div/input'],
            '（非交易现金）基本信息-报单模板-选中第二个值': ['按钮','/html/body/div[6]/div[1]/div[1]/ul/li[2]/span'],
            '（非交易现金）基本信息-产品类型': ['按钮','//*[@id="pane-first"]/div/div/div/div/form//div/label[text()="产品类型："]/../div/div/span/span/span'],
            '（非交易现金）基本信息-产品类型-选中产品': ['按钮', '/html/body/div[7]/div/div[2]/div/div/div[3]/table/tbody/tr[2]/td[1]'],
            '（非交易现金）基本信息-产品类型-保存': ['按钮','/html/body/div[7]/div/div[3]/span//button/span[text()="确 定"]'],
            '（非交易现金）基本信息-下一步': ['按钮','//*[@id="mainBox"]/div[3]/div/div/div[3]/span//button/span[text()="下一步"]'],
            '（非交易现金）费率设置-是否开启收费-否': ['按钮','//*[@id="pane-second"]/div/div/div/div/form/div/div/div/div/div/label[2]/span[1]'],
            '（非交易现金）费率设置-下一步': ['按钮', '//*[@id="mainBox"]/div[3]/div/div/div[3]/span//button/span[text()="下一步"]'],
            '（非交易现金）资料设置-下一步': ['按钮', '//*[@id="mainBox"]/div[3]/div/div/div[3]/span//button/span[text()="下一步"]'],
            '（非交易现金）平台资料-下一步': ['按钮', '//*[@id="mainBox"]/div[3]/div/div/div[3]/span//button/span[text()="下一步"]'],
            '（非交易现金）流程配置-关联流程': ['按钮', '//*[@id="pane-flowset"]/div/div/div[3]/table/tbody/tr/td[4]/div/div/div[1]/input'],
            '（非交易现金）流程配置-关联流程-选中流程': ['按钮', '/html/body/div[7]/div[1]/div[1]/ul/li[1]'],
            '（非交易现金）业务配置-保存': ['按钮', '//*[@id="mainBox"]/div[3]/div/div/div[3]/span//button/span[text()="保存"]'],
        }

        for i in businessType_dict:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, businessType_dict[i][1]))
            )

            # 拖动滚动条到target元素位置上
            try:
                target = businessType_dict[i][1]
                self.driver.execute_script("arguments[0].scrollIntoView();", target)
            except:
                pass

            #文本操作
            if businessType_dict[i][0] == '文本':
                #执行输入文本
                element = self.driver.find_element_by_xpath(businessType_dict[i][1])
                element.clear()
                element.send_keys(businessType_dict[i][2])

            #按钮操作
            elif businessType_dict[i][0] == '按钮':
                #执行点击
                time.sleep(0.2)
                element = self.driver.find_element_by_xpath(businessType_dict[i][1])
                self.driver.execute_script("arguments[0].click();", element)                #使用js点击
                time.sleep(0.6)

if __name__ == '__main__':
    a = Automatic_integration(userphone='13323594169',password='123456',path='http://189i0341c8.iok.la:27031')      #13377121517
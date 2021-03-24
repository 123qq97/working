import requests
from 接口.公共.登录 import login
from 接口.其他.流程配置 import process_configuration
import json
import time


class task_approval:
    def __init__(self, odd_num,configCode,handing_username='17666121214',handing_password='123456',head_url='http://192.168.0.58:82'):

        self.configCode=configCode
        self.head_url = head_url
        self.odd_num = odd_num
        self.handing_username = handing_username  # 推荐使用平台商户管理员账号
        self.handing_password = handing_password  # 推荐使用平台商户管理员密码
        self.html, result = login(head_url=self.head_url, username=self.handing_username, password=self.handing_password)

        global null, true, false
        null = ''
        true = ''
        false = ''

        #登录人参数
        time.sleep(0.1)
        pickPersonInfo_url = self.head_url + '/web-surety/security/open/personalInfo/pickPersonInfo'
        pickPersonInfo_text = self.html.get(pickPersonInfo_url).text
        pickPersonInfo_dict = eval(pickPersonInfo_text)
        self.finishPerson = pickPersonInfo_dict['result']['id']
        self.positionId = pickPersonInfo_dict['result']['positionLinkId']

        #流程参数
        self.p = Process_monitoring(head_url=self.head_url,handing_username=self.handing_username,handing_password=self.handing_password,odd_num=self.odd_num,configCode=self.configCode)
        task_detail_dict = self.p.Process_monitoring_get()
        self.processInstanceId=task_detail_dict['processInstanceId']
        self.bizCode=task_detail_dict['bizCode']
        self.node_name=task_detail_dict['node_name']




    # 平台流程审批
    def platform_task(self):
        # 流程审批窗口
        task_select_url = self.head_url + '/web-surety/security/open/task/getAllTaskListByProcInstId?id=' + self.processInstanceId
        # 流程审批办理
        task_handle_url = self.head_url + '/web-surety/security/workflow/task/passTask'

        response = self.html.get(task_select_url).text
        response = eval(response)

        for j, i in enumerate(response['result']):
            if i['taskStatus'] == 'RUNNING':
                operatorId = response['result'][j]['updateOperatorId']
                taskId = response['result'][j]['id']
                nodeId = response['result'][j]['nodeId']

                #转单
                self.p.Process_monitoring(taskId)

                # 流程审批办理
                data1 = {"operatorId": operatorId, "taskId": taskId, "remark": ""}
                data1 = json.dumps(data1, ensure_ascii=False)
                response1 = self.html.post(task_handle_url, data1.encode(),headers={'Content-Type': 'application/json'})
                print(response1.text, '-------------'+self.node_name+'审批')
                self.platform_task()
                break

#   流程监控
class Process_monitoring():
    def __init__(self, odd_num,handing_username='17666121214',handing_password='123456',head_url='http://192.168.0.58:82',configCode=''):
        self.configCode = configCode
        self.head_url = head_url
        self.odd_num = odd_num
        self.handing_username = handing_username  # 推荐使用平台商户管理员账号
        self.handing_password = handing_password  # 推荐使用平台商户管理员密码
        self.html, result = login(head_url=self.head_url, username=self.handing_username,password=self.handing_password)

        global null, true, false
        null = ''
        true = ''
        false = ''

        # 登录人参数
        time.sleep(0.1)
        pickPersonInfo_url = self.head_url + '/web-surety/security/open/personalInfo/pickPersonInfo'
        pickPersonInfo_text = self.html.get(pickPersonInfo_url).text
        pickPersonInfo_dict = eval(pickPersonInfo_text)
        self.finishPerson = pickPersonInfo_dict['result']['id']
        self.positionId = pickPersonInfo_dict['result']['positionLinkId']

    def Process_monitoring_get(self):
        # 查询configCode所属平台
        processConfigList_url = self.head_url + '/web-surety/security/workflow/processConfig/processConfigList'
        processConfigList_result = self.html.get(processConfigList_url).text
        processConfigList_result = eval(processConfigList_result)

        name = None
        systemKey = None
        for i in processConfigList_result['result']:
            if self.configCode == i['configCode']:
                systemKey = i['systemKey']
                name = i['name']

        # 查询流程监控列表
        queryTaskMonitor_url = self.head_url + '/web-surety/security/workflow/taskMonitor/queryTaskMonitorPage?keyword=' + self.odd_num + '&configCode=' + self.configCode + '&platFormIdentity=' + systemKey
        queryTaskMonitor_result = self.html.get(queryTaskMonitor_url).text
        queryTaskMonitor_result = eval(queryTaskMonitor_result)
        processInstanceId = queryTaskMonitor_result['result']['items'][0]['processInstanceId']
        bizCode = queryTaskMonitor_result['result']['items'][0]['bizCode']
        node_name = name
        task_detail_dict = {'processInstanceId': processInstanceId, 'bizCode': bizCode,'node_name': node_name}
        return task_detail_dict

    def Process_monitoring(self, id):
        # 转单办理
        changeTask_url = self.head_url + '/web-surety/security/workflow/taskMonitor/changeTask'
        data1 = {"id": id, "personId": self.finishPerson}
        data1 = json.dumps(data1, ensure_ascii=False)
        response1 = self.html.post(changeTask_url, data1.encode(), headers={'Content-Type': 'application/json'})



if __name__ == '__main__':
    t = task_approval(head_url='http://192.168.0.65:82', odd_num='X2103190015',configCode='RISK_DELAY_APPLY',handing_username='18888888888',handing_password='888888')
    t.platform_task()

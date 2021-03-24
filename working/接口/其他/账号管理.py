import requests
from 接口.公共.登录 import login
import time
from threading import Thread
from 接口.公共.线程与进程案例 import myThread


class account_number():
    def __init__(self,account_name,assignType,assignEntityId,login_number='17666121214',password='123456',head_url='http://192.168.0.58:82'):
        '''
        login_number:登录账号；尽量拿数据权限多的账号，否则会查询不到对应账号信息；考虑到不同环境测试账号不同，改为输入形式
        account_name：审批人或岗位名称；用于过滤数据
        assignType：审批类型；用于判断是按岗位id或人员id过滤数据
        assignEntityId：岗位id或人员id；用于找到对应审批账号
        head_url:域名;考虑不同环境测试，所以设为变量
        '''
        self.head_url = head_url
        self.account_name=account_name
        self.assignType=assignType
        self.assignEntityId=assignEntityId
        self.login_number=login_number
        self.password=password
        self.html,self.login_detail = login(username=self.login_number,password=self.password,head_url=self.head_url)
        time.sleep(0.1)
        global null, true,false
        null = 'null'
        true = 'true'
        false = 'false'


    #获取账号信息：  姓名、岗位、账号
    def queryPersonLink(self):
        # try:
        # 查询所有平台机构orgid：   平台机构与平台机构是同级，都在亮度金服下，拿到不同机构orgid查询对应机构账号
        orgid_list=[]
        queryOrgTree_url=self.head_url+'/web-surety/security/open/org/queryOrgTree?status=ENABLED'
        org_response=self.html.get(queryOrgTree_url).text
        org_response=eval(org_response)
        for i in org_response['result']:
            orgid_list.append(i['id'])


        #查询对应机构账号
        account_number_list = []
        for orgId in orgid_list:
            #账号管理列表
            queryPersonLink_url =self.head_url+ '/web-surety/security/erp/auth/person/queryPersonLink?orgId='+orgId+'&searchName='+self.account_name
            response=self.html.get(queryPersonLink_url).text
            response=eval(response)
            threadNum_list = []

            #根据岗位类型，找出对应的id的人或岗位,且该员工为启用状态
            for i in response['result']['itemList']:
                # 获取审批人员的信息
                def get_person_message(id,assignEntityId,assignType,positionLinkId,phone,suretyStatus):
                    if assignType=='PERSON' and id==assignEntityId and suretyStatus=='ENABLED':
                        # print(phone,i['name'],i['positionName'])
                        account_number_list.append(phone)
                    elif assignType=='POSITION' and positionLinkId==assignEntityId and suretyStatus=='ENABLED':
                        account_number_list.append(phone)
                        # print(phone,i['name'],i['positionName'])

                threadNum_list.append(myThread(get_person_message, kwargs={'id': i['id'],'assignEntityId': self.assignEntityId,'assignType':self.assignType,'positionLinkId': i['positionLinkId'],'phone': i['phone'],'suretyStatus':i['suretyStatus']}))  # 将线程添加进线程池
                # get_person_message(id,positionLinkId,phone)         #备用：调用函数


            #启动线程池中的线程
            for t in threadNum_list:
                t.start()

            #等待线程执行完毕，再继续向下执行代码
            for t in threadNum_list:
                t.join()
        return account_number_list
        # except Exception as e:
        #     return print(e.args,'获取审批账号信息失败！！！')




    def ishave_jurisdiction(self):
        pass

    def is_admin(self):
        pass





if __name__ == '__main__':
    stime = time.time()
    a=account_number(head_url='http://ldjfgj.vicp.io',login_number='18888025556',password='FDY2020',assignType='POSITION',account_name='风控主管',assignEntityId='8f0f5227-3078-4fd3-a4af-051777645b27')
    # t=myThread(a.queryPersonLink,args=())
    # t.start()
    # t.join()
    # print(t.get_result())
    print(a.queryPersonLink())
    etime =time.time()
    print('处理时间：',etime-stime,'s')

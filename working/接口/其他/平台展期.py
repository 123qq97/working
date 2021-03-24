import requests
from 接口.公共.登录 import login
import json
from 接口.其他.时间转换 import local_to_utc,local_to_time_stamp
import datetime
import time
from 接口.其他.流程审批 import task_approval
from 接口.公共.线程与进程案例 import myThread
from 接口.流程.平台流程 import process


url_dict = {
    '展期详情':'/web-surety/security/platformOverdue/queryCreateDetail'
}

class Platform_extension(process):
    # def __init__(self, odd_num, handing_username='17666121214',handing_password='123456',head_url='http://192.168.0.58:82'):
    #     global null, true, false
    #     null = None
    #     true = True
    #     false = False
    #     self.odd_num = odd_num
    #     self.handing_username = handing_username
    #     self.handing_password = handing_password
    #     self.head_url = head_url
    #     self.html ,self.response= login(head_url=self.head_url,username=handing_username,password=handing_password)

    def Application_for_extension(self):
        pass




if __name__ == '__main__':
    p = Platform_extension(odd_num='X2101140007')
    # p.Application_for_extension()





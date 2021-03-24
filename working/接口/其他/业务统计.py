from 接口.公共.登录 import login
import time

class Capital():
    def __init__(self,handing_username='17666121214',handing_password='123456',head_url='http://192.168.0.58:82',keyword=''):
        global null, true, false
        null = None
        true = True
        false = False

        self.head_url = head_url
        self.handing_username = handing_username  # 推荐使用平台商户管理员账号
        self.handing_password = handing_password  # 推荐使用平台商户管理员密码
        self.keyword = keyword
        self.html, response = login(username=self.handing_username, password=self.handing_password,
                                         head_url=self.head_url)
        time.sleep(0.1)         #session未请求完成，等待0.1秒

    #在保列表
    def queryUnderGuaranteePage(self):
        queryUnderGuarantee_url = self.head_url + '/web-surety/security/fnBusinessStatistics/queryUnderGuaranteePage' + '?pageSize=20&currentPage=1&keyword='+self.keyword
        queryUnderGuarantee_result = self.html.get(queryUnderGuarantee_url).text
        queryUnderGuarantee_result = eval(queryUnderGuarantee_result)
        pageCount = queryUnderGuarantee_result['result']['pageCount']

        #循环每页取值
        appleMoneySum = 0
        for i in range(pageCount):
            queryUnderGuarantee_url = self.head_url + '/web-surety/security/fnBusinessStatistics/queryUnderGuaranteePage' + '?pageSize=20&currentPage=' + str(i+1) + '&keyword=' + self.keyword
            queryUnderGuarantee_result = self.html.get(queryUnderGuarantee_url).text
            queryUnderGuarantee_result = eval(queryUnderGuarantee_result)

            result_list = queryUnderGuarantee_result['result']['items']
            appleMoneySubtotal = 0                                       #小计
            for i in result_list:
                fundOrgModelList = i['fundOrgModelList']
                guaranteeNum = i['guaranteeNum']
                for j in fundOrgModelList:
                    arrivalMoney = j['arrivalMoney']
                    appleMoneySubtotal = appleMoneySubtotal + (float(arrivalMoney)/10000)
                    print(guaranteeNum,'到账金额：',arrivalMoney)

            print('在保小计：',appleMoneySubtotal)
            appleMoneySum = appleMoneySum +appleMoneySubtotal
        print('在保总计:',appleMoneySum)

    # 解保列表
    def queryOverGuaranteePage(self):
        queryUnderGuarantee_url = self.head_url + '/web-surety/security/fnBusinessStatistics/queryOverGuaranteePage' + '?pageSize=20&currentPage=1&keyword=' + self.keyword
        queryUnderGuarantee_result = self.html.get(queryUnderGuarantee_url).text
        queryUnderGuarantee_result = eval(queryUnderGuarantee_result)
        pageCount = queryUnderGuarantee_result['result']['pageCount']

        # 循环每页取值
        appleMoneySum = 0
        for i in range(pageCount):
            queryUnderGuarantee_url = self.head_url + '/web-surety/security/fnBusinessStatistics/queryOverGuaranteePage' + '?pageSize=20&currentPage=' + str(
                i+1) + '&keyword=' + self.keyword
            queryUnderGuarantee_result = self.html.get(queryUnderGuarantee_url).text
            queryUnderGuarantee_result = eval(queryUnderGuarantee_result)

            result_list = queryUnderGuarantee_result['result']['items']
            appleMoneySubtotal = 0  # 小计
            for i in result_list:
                fundOrgModelList = i['fundOrgModelList']
                guaranteeNum = i['guaranteeNum']
                for j in fundOrgModelList:
                    arrivalMoney = j['arrivalMoney']
                    appleMoneySubtotal = appleMoneySubtotal + (float(arrivalMoney)/10000)
                    print(guaranteeNum,'到账金额：',arrivalMoney)

            print('解保小计：', appleMoneySubtotal)
            appleMoneySum = appleMoneySum + appleMoneySubtotal
        print('解保总计:', appleMoneySum)

if __name__ == '__main__':
    c = Capital(head_url='http://192.168.0.58:82/',handing_username='17666121214',handing_password='123456',keyword='')# ,handing_username='18888888888',handing_password='FDY2020'
    c.queryUnderGuaranteePage()
    c.queryOverGuaranteePage()
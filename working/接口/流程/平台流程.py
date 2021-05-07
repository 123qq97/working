import requests
from 接口.公共.登录 import login
from 接口.公共.筛选替换文字 import screen
from 接口.公共.递归字典数据 import recursive_filtering
import json
from 接口.其他.时间转换 import local_to_utc,local_to_time_stamp,time_stamp_to_local
import datetime
import time
from 接口.其他.增加额度 import add_quota
from 接口.其他.流程审批 import task_approval
from 接口.公共.线程与进程案例 import myThread
from 接口.其他.初始化方法 import *
from 接口.其他.json格式化输出 import format_ouput

# 链接
url_dict = {
    '初始化参数': {'报单列表': ['/web-surety/security/business/guarantee/guaranteePage?keyWord=',
                       '/web-surety/security/open/guarantee/pickGuaranteeMessage?id=',
                       '/web-surety/security/riskAssetsCreditCity/querySubmitAndCoopState'],
              '登录人参数': ['/web-surety/security/open/personalInfo/pickPersonInfo'],
              '公司账户': ['/web-surety/security/open/fundAccount/queryFnAccountBox'],
              '分行、支行': ['/web-surety/security/open/fundProvider/pageQuery',
                           '/web-surety/security/open/fundProvider/queryAllChildByParent']},
    '面签': [
        '/web-surety/security/interviewVisa/queryInterviewVisaRiskPage?keyword=',
        '/web-surety/security/interviewVisa/submitInterviewVisa'],
    '核行': [
        '/web-surety/security/checkBank/queryCheckBankRiskPage?keyword=',
        '/web-surety/security/checkBank/selectSellerLoanByOrderId',
        '/web-surety/security/checkBank/selectBuyerLoanByOrderId',
        '/web-surety/security/checkBank/commitCheckBank'],
    '运营初审': [
        '/web-surety/security/risk/riskOperateApproval/queryRiskOperateToBeApprovalPage',
        '/web-surety/security/risk/riskOperateApproval/selectById',
        '/web-surety/security/risk/riskOperateApproval/receive',
        '/web-surety/security/risk/riskOperateApproval/approvalPass',
        '/web-surety/security/risk/riskOperateApproval/approvalReject'],
    '风控初审': [
        '/web-surety/security/risk/riskFirstApproval/queryRiskFirstToBeApprovalPage',
        '/web-surety/security/risk/riskFirstApproval/selectApprovalInfoById',
        '/web-surety/security/risk/riskApprovalSub/selectFundInfo',
        '/web-surety/security/risk/riskFirstApproval/receive',
        '/web-surety/security/risk/riskFirstApproval/approvalPass',
        '/web-surety/security/risk/riskApproval/selectTaskNoteInfo',
        '/web-surety/security/risk/riskFirstApproval/approvalReject'],
    '风控复审': [
        '/web-surety/security/workflow/workflowapprove/queryTaskOfCurrentPerson',
        '/web-surety/security/open/task/getHisAndRunTaskListByProcInstId',
        '/web-surety/security/workflow/task/passTask'],
    '收费': [
        '/web-surety/security/fee/queryFundFeePage',
        '/web-surety/security/fee/insertBeforeLoanFee',
        '/web-surety/security/fee/insertDelayFee',
        '/web-surety/security/fee/insertOverdueFee'],
    '用款确认': [
        '/web-surety/security/platform/platformFundApply/queryPlatformFundApplyPage',
        '/web-surety/security/platform/platformFundApply/pickFundApplyInfo',
        '/web-surety/security/platform/platformFundApply/submit'],
    '收要件': [
        '/web-surety/security/fnEssentialsTake/queryFnEssentialsTakePage',
        '/web-surety/security/fnEssentialsTake/saveFnEssentialsTake',
        '/web-surety/security/fnEssentialsTake/takeCompleteConfirm'],
    '执行岗备注': [
        '/web-surety/security/risk/riskExecutionRemarks/queryToBeRiskExecutionRemarksPage',
        '/web-surety/security/risk/riskExecutionRemarks/insertRiskExecutionRemarks'],
    '保函寄送': [
        '/web-surety/security/risk/riskGuaranteeMain/queryRiskGuaranteeMainPage',
        '/web-surety/security/risk/riskGuaranteeSend/insertRiskGuaranteeSend'],
    '资金到账': {'资金安排': ['/web-surety/security/fundApply/queryFundApplyPage',
                      '/web-surety/security/fundApply/pickFundApplyInfo',
                      '/web-surety/security/fundApply/queryFundApplyLoanDetails',
                      '/web-surety/security/fundApply/submitFundApply'
                      ], '资料推送': [
        '/web-surety/security/fundApply/queryNoPushFundApplyPage',
        '/web-surety/security/fundApply/getPayeeAccountByOrderId',
        '/web-surety/security/fundApply/pushFundOrg'], '到账管理': [
        '/web-surety/security/fundApply/queryIsArrivalAccountFundApplyPage',
        '/web-surety/security/fundApply/updateArrivalAccountStatus']},
    '查档查诉讼': [
        '/web-surety/security/risk/riskCheckDocLawsuit/queryUncheckOrders',
        '/web-surety/security/risk/riskCheckDocLawsuit/checkDocAndLawsuitDetail',
        '/web-surety/security/riskCheckDoc/updateRiskCheckDoc',
        '/web-surety/security/risk/riskCheckDocLawsuit/updateCheckDocAndLawsuit'],
    '收取保证金': [
        '/web-surety/security/billing/queryBillingPage',
        '/web-surety/security/fnBusinessAssure/saveFnBusinessAssure'],
    '出款申请': [
        '/web-surety/security/fnRedeem/queryFnRedeemPage',
        '/web-surety/security/billing/queryLoanDetails',
        '/web-surety/security/business/guarantee/pickLoanSellerByGuaranteeId',
        '/web-surety/security/billing/applyBilling'],
    '出款审批': [
        '/web-surety/security/billing/queryBillingPage',
        '/web-surety/security/billing/findBillingAccountByBillingDetailsId',
        '/web-surety/security/billing/auditBilling'],
    '流程审批': [
        '/web-surety/security/workflow/workflowapprove/queryTaskOfCurrentPerson',
        '/web-surety/security/open/task/getHisAndRunTaskListByProcInstId',
        '/web-surety/security/workflow/task/passTask'],
    '出款': [
        '/web-surety/security/billing/queryBillingPage',
        '/web-surety/security/billing/queryArrivalAccountFundListToBilling',
        '/web-surety/security/billing/confirmBilling',
        '/web-surety/security/billing/billingCheckOtp'],
    '赎楼': [
        '/web-surety/security/fnRedeem/queryFnRedeemPage',
        '/web-surety/security/fnRedeem/saveFnRedeem',
        '/web-surety/security/fnRedeem/saveFnSupplement'],
    '核对赎楼凭证': ['/web-surety/security/fnRedeemCheck/queryFnRedeemCheckPage','/web-surety/security/fnRedeemCheck/queryFnRedeemCheckRecord','/web-surety/security/fnRedeemCheck/editFnRedeemCheckRecord'],
    '二次还款' : {'发起二次还款':['/web-surety/security/billingTwoApply/queryBusinessBillingTwoApplyIndexPage',
                                  '/web-surety/security/billingTwoApply/suretyApplyTwoBilling'],
                  '二次到账' : ['/web-surety/security/billingTwoApply/queryBillingTwoApplyIndexPage',
                                '/web-surety/security/billingTwoApply/updateTwoArrivalAccountStatus'],
                  '二次出款申请' : ['/web-surety/security/billingTwoApply/applyTwoBilling'],
                  '二次出款审批' : ['/web-surety/security/billing/findBillingAccountByBillingDetailsId',
                                    '/web-surety/security/billingTwoApply/auditTwoBilling'],
                  '二次出款' : ['/web-surety/security/billingTwoApply/confirmTwoBilling'],
                  '二次还款' : ['/web-surety/security/billingTwoApply/saveTwoBillingRedeem']},
    '取原证': [
        '/web-surety/security/fnCertTake/queryFnCertTakePage',
        '/web-surety/security/fnCertTake/insertFnCertTake'],
    '权证管理': ['/web-surety/security/platformProductEvid/list',
             '/web-surety/security/platformProductEvid/sendOrerRecord',
             '/web-surety/security/risk/handleAfterForeclosure/queryCertLogout',
             '/web-surety/security/risk/handleAfterForeclosure/redeemCertLLogoutSave',
             '/web-surety/security/risk/handleAfterForeclosure/queryTransfer',
             '/web-surety/security/risk/handleAfterForeclosure/redeemTransferSave',
             '/web-surety/security/risk/handleAfterForeclosure/queryTakeNewCert',
             '/web-surety/security/risk/handleAfterForeclosure/redeemTakeNewCertSave',
             '/web-surety/security/risk/handleAfterForeclosure/queryTakeNewCert',
             '/web-surety/security/risk/handleAfterForeclosure/redeemMortgageSave',
             '/web-surety/security/platformProductEvid/handleAfterSave'],
    '回款': ['/web-surety/security/repayment/queryRepaymentPage',
           '/web-surety/security/billing/queryLoanDetails',
           '/web-surety/security/repayment/queryArrivalAccountFundListToRepayment',
           '/web-surety/security/repayment/insertRepaymentDetails'],

}




# 流程开始
class process:

    def __init__(self, odd_num=None, handing_username='17666121214',handing_password='123456',head_url='http://192.168.0.58:82'):
        stime = time.time()
        global null, true, false
        null = None
        true = True
        false = False

        # 转换为本地链接
        self.url = recursive_filtering(url_dict, head_url=head_url)

        self.head_url = head_url
        self.handing_username=handing_username      #推荐使用平台商户管理员账号
        self.handing_password=handing_password      #推荐使用平台商户管理员密码
        self.html, self.response = login(username=self.handing_username, password=self.handing_password,head_url=self.head_url)
        self.response = eval(self.response.text)
        self.orgId = self.response['result']['orgId']
        self.odd_num = odd_num
        self.takeDate = str(datetime.date.today())  #当前日期
        self.chargeDate = local_to_utc()            #当前地区时间
        self.stampDate = local_to_time_stamp()      #当前日期时间戳

        if odd_num == None:
            pass
        else:
            # 查询担保单列表,获取单号对应id
            def guaratee_message(url, html, odd_num):
                guarateeID_url = url['初始化参数']['报单列表'][0] + odd_num
                response = html.get(guarateeID_url).text
                response = eval(response)
                id = response['result']['items'][0]['id']

                guarateetype_url = url['初始化参数']['报单列表'][1] + id
                response1 = html.get(guarateetype_url).text
                response1 = eval(response1)
                return response1, response

            #使用多线程调用函数
            guarateeMessage_thread = myThread(guaratee_message,kwargs={'url':self.url,'html':self.html,'odd_num':self.odd_num})
            pickPersonInfoMessage_thread = myThread(pickPersonInfo_message,kwargs={'url':self.url,'html':self.html})
            companyAccountMessage_thread = myThread(company_account_message,kwargs={'url':self.url,'orgId':self.orgId,'html':self.html})
            fundProvider_thread = myThread(fundProvider_message,kwargs={'url':self.url,'html':self.html})

            guarateeMessage_thread.start()
            pickPersonInfoMessage_thread.start()
            companyAccountMessage_thread.start()
            fundProvider_thread.start()

            guarateeMessage_thread.join()
            pickPersonInfoMessage_thread.join()
            companyAccountMessage_thread.join()
            fundProvider_thread.join()

            guarateeMessage_result = guarateeMessage_thread.get_result()[0]
            guarateeMessage_result_to = guarateeMessage_thread.get_result()[1]
            pickPersonInfoMessage_result = pickPersonInfoMessage_thread.get_result()
            companyAccountMessage_result = companyAccountMessage_thread.get_result()
            fundProvider_result = fundProvider_thread.get_result()

            # 查询担保单列表,取值字段
            self.fundType = guarateeMessage_result['result']['bizTypeModel']['fundType']
            self.guaranteeBizType = guarateeMessage_result['result']['guarantee']['guaranteeBizType']    #区分拍卖房，值：PMF或null
            self.isRedeemselfBiz = guarateeMessage_result['result']['bizTypeModel']['isRedeemselfBiz']   #是否自赎业务
            self.transactionType = guarateeMessage_result['result']['bizTypeModel']['transactionType']
            if self.guaranteeBizType !='PMF':
                self.loanType = guarateeMessage_result['result']['loanSellerList'][0]['loanType']
            self.riskAssetsCreditCityId = guarateeMessage_result['result']['guarantee']['riskAssetsCreditCityId']
            self.manager_phone = guarateeMessage_result['result']['guaranteePartnerList'][0]['phone']    #经办人电话
            self.isTwiceRepay = guarateeMessage_result_to['result']['items'][0]['isTwiceRepay']

            # 使用多线程调用函数
            isFaceBankCheck_thread = myThread(isFaceBankCheck_message,kwargs={'url': self.url,'riskAssetsCreditCityId': self.riskAssetsCreditCityId ,'html': self.html})
            managerOrgId_thread = myThread(manager_orgId_message,kwargs={'head_url': self.head_url,'manager_phone': self.handing_username,'manager_password':self.handing_password})

            isFaceBankCheck_thread.start()
            managerOrgId_thread.start()

            isFaceBankCheck_thread.join()
            managerOrgId_thread.join()

            isFaceBankCheck_result = isFaceBankCheck_thread.get_result()
            managerOrgId_result = managerOrgId_thread.get_result()[0]

            #查询是否需要面签、核行
            self.isFaceBankCheck = isFaceBankCheck_result['result']['isFaceBankCheck']                       #是否需要平台面签、核行

            # 获取经办人的orgId、cityOrgId
            self.html1 =  managerOrgId_thread.get_result()[1]
            self.orgId1 = managerOrgId_result['result']['orgId']
            self.cityOrgId1 = managerOrgId_result['result']['cityOrgId']

            #登录人参数,取值字段
            self.companyId = pickPersonInfoMessage_result['result']['companyId']
            self.positionLinkId = pickPersonInfoMessage_result['result']['positionLinkId']
            self.id = pickPersonInfoMessage_result['result']['id']
            self.name = pickPersonInfoMessage_result['result']['name']

            # 公司账户,取值字段
            self.companyAccountBank = companyAccountMessage_result['result']['itemList'][1]['fundProviderName']
            self.companyAccountId = companyAccountMessage_result['result']['itemList'][1]['id']
            self.companyAccountName = companyAccountMessage_result['result']['itemList'][1]['accountName']
            self.companyAccountNumber = companyAccountMessage_result['result']['itemList'][1]['accountNumber']
            self.companyAccountAll = self.companyAccountBank + '-' + self.companyAccountName + '(' + self.companyAccountNumber + ')'

            #分行、支行,取值字段
            # self.accountBank = fundProvider_result['result']['itemList'][0]['name']
        etime = time.time()
        print('处理时间：', etime-stime, 's')

    # 平台面签
    def face_signature(self):
        # 判断不需要平台面签、核行，就不办理面签
        if self.isFaceBankCheck == 'NO':
            return

        try:
            # 查询面签列表,获取单号对应id
            face_url = self.url['面签'][0] + self.odd_num
            response = self.html.get(face_url).text
            response = eval(response)

            # 取值字段
            id = response['result']['items'][0]['id']

            # 办理面签,需要获取列表单号对应id
            data = {
                "associatesFileInfoList": [], "handlePersonType": "MECHANISM_HANDLE", "interviewAddress": "面签地址1",
                "interviewTime": self.chargeDate, "remark": "备注1", "source": "PC",
                "transactorOperatorName": "张admin", "id": id, "systemKey": "RISK_SYS"
            }
            data = json.dumps(data)
            response1 = self.html.post(self.url['面签'][1], data, headers={'Content-Type': 'application/json'})
            print(response1.text, '-------------平台面签')
            # self.nuclear_row()
        except:

            return print('平台面签失败')

    # 平台核行  (原贷款：LOAN_SELLER|新贷款：LOAN_BUYER)
    def nuclear_row(self, loanType=['LOAN_SELLER', 'LOAN_BUYER']):
        #判断不需要平台面签、核行，就不办理核行
        if self.isFaceBankCheck == 'NO':
            return

        for i, j in enumerate(loanType):
            try:
                # 查询核行列表
                face_url = self.url['核行'][0] + self.odd_num
                null = ''
                true = ''
                message_response1 = self.html.get(face_url).text
                message_response1 = eval(message_response1)
                # 取值字段
                checkBankGeneralId = message_response1['result']['items'][0]['id']
                orderId = message_response1['result']['items'][0]['orderId']

                if j == 'LOAN_SELLER':
                    face_url1 = self.url['核行'][1] + '?orderId=' +orderId
                elif j == 'LOAN_BUYER':
                    face_url1 = self.url['核行'][2] + '?orderId=' +orderId

                message_response2 = self.html.get(face_url1).text
                message_response2 = eval(message_response2)
                loanBackName = message_response2['result'][0]['bankName']
                loanBackId = message_response2['result'][0]['bankId']

                # 办理核行,需要获取列表单号对应id
                data = {"associatesFileIdList": [],
                        "checkBankDetail": {"address": "核行地址1", "backContactPerson": "梁涛",
                                            "backContactPhone": "15592245136",
                                            "checkBankGeneralId": checkBankGeneralId,
                                            "checkTime": self.chargeDate,
                                            "checkType": "SITE_CHECKED_BANK", "handlePersonName": "张admin",
                                            "handlePersonType": "MECHANISM_HANDLE", "loanBackName": loanBackName,
                                            "loanBackId": loanBackId, "loanType": j,
                                            "remark": "备注1", "source": "PC"
                                            }, "orderId": orderId, "systemKey": "RISK_SYS"}
                data = json.dumps(data)
                response1 = self.html.post(self.url['核行'][3], data, headers={'Content-Type': 'application/json'})
                if j == 'LOAN_SELLER':
                    print(response1.text,'-------------平台原贷款核行')
                elif j == 'LOAN_BUYER':
                    print(response1.text,'-------------平台新贷款核行')
            except:
                if j == 'LOAN_SELLER':
                    return print('平台原贷款核行不通过')
                elif j == 'LOAN_BUYER':
                    return print('平台新贷款核行不通过')

    #运营初审
    def preliminary_operation_review(self,is_reject=False,is_pass=True):
        '''
        :param is_reject: 是否驳回,True办理驳回，False不办理，默认为False
        :param is_pass: 是否运营初审审查,True办理，False不办理，默认为True
        1、先判断是否接收，未接收就办理，接收了就跳过
        2、再判断是否需要运营初审审查，True就办理，False就不办理
        3、再判断是否需要驳回，True就办理，False则不办理
        70780886-3848-455f-a041-0b01f263d737
        '''
        try:
            stime = time.time()
            # 查询运营初审列表
            face_url = self.url['运营初审'][0] + '?keyword=' + self.odd_num + '&companyId=' + self.companyId
            message_response1 = self.html.get(face_url).text
            message_response1 = eval(message_response1)

            # 取值字段
            orderId = message_response1['result']['items'][0]['orderId']
            riskApprovalId = message_response1['result']['items'][0]['riskApprovalId']
            isReceive = message_response1['result']['items'][0]['isReceive']

            # 办理运营初审接收,需要获取列表单号对应orderId、riskApprovalId
            data1 = {"orderId": orderId, "riskApprovalId": riskApprovalId, "companyId": self.companyId}
            data1 = json.dumps(data1)

            #未接收，就办理运营初审接收
            if isReceive == 'NO':
                response1 = self.html.post(self.url['运营初审'][2], data1, headers={'Content-Type': 'application/json'})
                print(response1.text, '-------------运营初审接收')

            #是否办理运营初审审查
            if is_pass ==False:
                return

            # 办理运营初审审查,需要获取列表单号对应id、riskApprovalId、riskApprovalId
            message_response2 = self.html.get(face_url).text
            message_response2 = eval(message_response2)
            # 取值字段
            id = message_response2['result']['items'][0]['id']

            face_url1 = self.url['运营初审'][1] + '?id=' + id
            message_response3 = self.html.get(face_url1).text
            message_response3 = eval(message_response3)

            createOperatorId = message_response3['result']['createOperatorId']
            createTime = message_response3['result']['createTime']
            examinerId = message_response3['result']['examinerId']
            id = message_response3['result']['id']
            isNeedFaceBankCheck = message_response3['result']['isNeedFaceBankCheck']
            orderId = message_response3['result']['orderId']
            orgId = message_response3['result']['orgId']
            receiveTime = message_response3['result']['receiveTime']
            isBankCheck = message_response3['result']['isBankCheck']
            isFaceCheck = message_response3['result']['isFaceCheck']
            riskApprovalId = message_response3['result']['riskApprovalId']
            riskFundInfoModelList = message_response3['result']['riskFundInfoModelList']
            status = message_response3['result']['status']
            updateOperatorId = message_response3['result']['updateOperatorId']
            updateTime = message_response3['result']['updateTime']
            correctFundIds = []
            for i in riskFundInfoModelList:
                correctFundIds.append(i['id'])

            # 办理运营初审审查
            data2 = {"approvalState":"PASS","normalType":"NORMAL","rejectType":"","addFileExtendIds":"",
                     "addFileIds":"","addFileNames":"","acceptCondition":"","addFileRemark":"",
                     "createOperatorId":createOperatorId,"createTime":createTime,
                     "examineTime":null,"examinerId":examinerId,
                     "examinerName":"","id":id,"isAddFile":"NO",
                     "isBankCheck":isBankCheck,"isFaceCheck":isFaceCheck,"isNeedFaceBankCheck":isNeedFaceBankCheck,"isUsePlatform":null,
                     "operateCorrectFundIds":"","operateIncorrectFundIds":"",
                     "orderId":orderId,"orgId":orgId,
                     "receiveTime":receiveTime,"refType":"","rejectReason":"",
                     "riskApprovalId":riskApprovalId,
                     "riskFundInfoModelList":riskFundInfoModelList,"status":status,"unusualExplain":"","unusualReason":"",
                     "updateOperatorId":updateOperatorId,"updateTime":updateTime,
                     "approvalType":"NORMAL","addFileExtendNameList":[""],"fundIds":"",
                     "correctFundIds":correctFundIds,"incorrectFundIds":[]}

            # 驳回：将状态、url改为驳回
            if is_reject == True:
                data2['approvalState'] = 'REJECT'
                data2['rejectType'] = 'INCORRECT'
                run_url = self.url['运营初审'][4]
            #通过：调用通过的url；
            else:
                run_url = self.url['运营初审'][3]

            data2 = json.dumps(data2,ensure_ascii=False)
            response2 = self.html.post(run_url, data2.encode(), headers={'Content-Type': 'application/json'})
            etime = time.time()
            print(response2.text, '-------------运营初审审查,处理时间:',etime-stime,'s')
        except Exception as e:
            return print(e.args,"运营初审不通过")

    # 风控初审
    def risk_review(self,is_reject=False,is_pass=True,reject_node='报单'):
        '''
        :param is_reject: 是否驳回,True办理驳回，False不办理，不填默认为False
        :param is_pass: 是否风控初审审查,True办理，False不办理，不填默认为True
        :param reject_node: 驳回至xx节点,可填“报单”、“运营初审”，不填默认为“报单”
        1、先判断是否接收，未接收就办理，接收了就跳过
        2、再判断是否需要风控初审审查，True就办理，False就不办理
        3、再判断是否需要驳回，True就办理，False则不办理
        '''
        # try:
        stime = time.time()
        # 查询风控初审列表
        face_url = self.url['风控初审'][0] + '?companyId=' + self.companyId + '&orgId=' + self.orgId + '&keyword=' + self.odd_num
        message_response1 = self.html.get(face_url).text
        message_response1 = eval(message_response1)
        # 取值字段
        orderId = message_response1['result']['items'][0]['orderId']
        riskApprovalId = message_response1['result']['items'][0]['riskApprovalId']
        isReceive = message_response1['result']['items'][0]['isReceive']
        processId = message_response1['result']['items'][0]['processId']
        nodeId = message_response1['result']['items'][0]['nodeId']

        # 办理风控初审接收,需要获取列表单号对应orderId、riskApprovalId
        data1 = {"orderId": orderId, "riskApprovalId": riskApprovalId, "companyId": self.companyId}
        data1 = json.dumps(data1)

        # 未接收，就办理风控初审接收
        if isReceive == 'NO':
            response1 = self.html.post(self.url['风控初审'][3], data1, headers={'Content-Type': 'application/json'})
            print(response1.text, '-------------风控初审接收')

        # 是否办理风控初审审查
        if is_pass == False:
            return

        # 办理风控初审审查,需要获取列表单号对应id、riskApprovalId、riskApprovalId
        message_response2 = self.html.get(face_url).text
        message_response2 = eval(message_response2)
        id = message_response2['result']['items'][0]['id']

        face_url1 = self.url['风控初审'][1] + '?id=' + id
        face_url2 = self.url['风控初审'][2] + '?riskApprovalId=' + riskApprovalId + '&orderId=' + orderId + '&id=' + id
        message_response3 = self.html.get(face_url1).text
        message_response3 = eval(message_response3)
        message_response4 = self.html.get(face_url2).text
        message_response4 = eval(message_response4)
        takeOutDebtRatio = message_response3['result']['takeOutDebtRatio']
        approvalJobTitle = message_response3['result']['approvalJobTitle']
        approvalName = message_response3['result']['approvalName']
        buyer = message_response3['result']['buyer']
        channelMargin = message_response3['result']['channelMargin']
        companyId = message_response3['result']['companyId']
        createOperatorId = message_response3['result']['createOperatorId']
        createTime = message_response3['result']['createTime']
        debtRatio = message_response3['result']['debtRatio']
        depositMargin = message_response3['result']['depositMargin']
        downPayments = message_response3['result']['downPayments']
        estName = message_response3['result']['estName']
        estateValue = message_response3['result']['estateValue']
        examinerId = message_response3['result']['examinerId']
        isAddFile = message_response3['result']['isAddFile']
        isAllocation = message_response3['result']['isAllocation']
        isSelfSupport = message_response3['result']['isSelfSupport']
        isUseChannel = message_response3['result']['isUseChannel']
        loanTotalAmount = message_response3['result']['loanTotalAmount']
        managerName = message_response3['result']['managerName']
        margin = message_response3['result']['margin']
        need = message_response3['result']['need']
        oldLoanSituation = message_response3['result']['oldLoanSituation']
        orderNo = message_response3['result']['orderNo']
        orgId = message_response3['result']['orgId']
        productName = message_response3['result']['productName']
        receiveTime = message_response3['result']['receiveTime']
        redeemHouseAmount = message_response3['result']['redeemHouseAmount']
        redemptionRatio = message_response3['result']['redemptionRatio']
        refType = message_response3['result']['refType']
        remark = message_response3['result']['remark']
        returnSource = message_response3['result']['returnSource']
        seller = message_response3['result']['seller']
        status = message_response3['result']['status']
        subCompanyName = message_response3['result']['subCompanyName']
        totalAmount = message_response3['result']['totalAmount']
        transactionPrice = message_response3['result']['transactionPrice']
        updateOperatorId = message_response3['result']['updateOperatorId']
        updateTime = message_response3['result']['updateTime']
        correctFundIds = []

        for i in message_response4['result']['riskFundInfoModelList']:
            correctFundIds.append(i['id'])

        data2 = {"approvalType":"NORMAL","fundIds":"","allocationAssureMoney":"","takeOutDebtRatio":takeOutDebtRatio,"isNecessary":"NO","addFileRemark":"",
                 "allChannel":"","approvalJobTitle":approvalJobTitle,"approvalName":approvalName,"approvalOpinions":"通过","approveState":"PASS","assetsCapitalMaxLimit":0,
                 "assetsCapitalMinLimit":0,"buyAllowRemark":"","buyer":buyer,"channelAssureMoney":channelMargin,
                 "channelMargin":channelMargin,"companyId":companyId,"createOperatorId":createOperatorId,
                 "createTime":createTime,"creditSituation":"","creditSituationRemark":"","dealPriceCheckExplain":"",
                 "dealPriceCheckState":"","debtRatio":debtRatio,"depositMargin":depositMargin,"downPayments":downPayments,
                 "estName":estName,"estateValue":estateValue,"examineTime":null,"examinerId":examinerId,
                 "examinerName":"","guaranteeAmount":0,"guarantorSituationRemark":"","id":id,"isAddFile":isAddFile,
                 "isAllocation":isAllocation,"isBuyAllow":"","isGuarantorSituation":"","isOwnerCivilDisputes":"",
                 "isOwnerLawsuit":"","isSuspend":"","isSelfSupport": isSelfSupport,"isUseChannel":isUseChannel,"loanTotalAmount":loanTotalAmount,
                 "managerName":managerName,"margin":margin,"need":need,"normalType":"NORMAL","oldLoanSituation":oldLoanSituation,
                 "orderId":orderId,"orderNo":orderNo,"orgId":orgId,
                 "ownerCivilDisputesRemark":"","productName":productName,"ownerLawsuitRemark":"","productType":"SL","receivableAmount":"",
                 "receiveTime":receiveTime,"redeemHouseAmount":redeemHouseAmount,"redemptionRatio":redemptionRatio,"refType":refType,
                 "refuseReason":"","remark":remark,"returnSource":returnSource,
                 "riskApprovalId":riskApprovalId,"seller":seller,"status":status,
                 "subCompanyName":subCompanyName,"suspendDate":null,"suspendRelieveDate":null,"totalAmount":totalAmount,
                 "transactionPrice":transactionPrice,"transactionType":self.transactionType,"updateOperatorId":updateOperatorId,
                 "updateTime":updateTime,"addFileExtendNameList":[""],"isRejectToStartNode":"NO",
                 "correctFundIds":correctFundIds,"incorrectFundIds":[]}

        #驳回：判断驳回至报单/运营初审节点，获取对应id传参，将状态、url改为驳回,
        if is_reject == True:
            face_url3 = self.url['风控初审'][5] + '?processId=' + processId + '&nodeId=' + nodeId + '&id=' + riskApprovalId
            run_url = self.url['风控初审'][6]
            message_response5 = self.html.get(face_url3).text
            message_response5 = eval(message_response5)
            data2['approvalOpinions'] = '驳回'
            data2['approveState'] = 'REJECT'

            if reject_node == '报单':
                nodeId = message_response5['result'][0]['id']              #报单节点id
                data2['nodeId'] = nodeId
            elif reject_node == '运营初审':
                nodeId = message_response5['result'][1]['id']              #运营初审节点id
                data2['nodeId'] = nodeId
        #通过：调用通过的url；
        else:
            run_url=self.url['风控初审'][4]

        data2 = json.dumps(data2, ensure_ascii=False)
        response2 = self.html.post(run_url, data2.encode(), headers={'Content-Type': 'application/json'})
        etime = time.time()
        print(response2.text, '-------------风控初审审查,处理时间:',etime-stime,'s')
        # except:
        #     return print("风控初审不通过")

    # 风控复审
    def risk_recheck(self):
        # try:
        # 风控复审办理
        t = task_approval(odd_num=self.odd_num,head_url=self.head_url,handing_username=self.handing_username,handing_password=self.handing_password,configCode='RISK_WIND_CONTROL')#
        t.platform_task()
        time.sleep(1)

        # except Exception as e:
        #     return print(e.args, '风控复审审查失败')

    # 收费
    def charge(self,currentCollectFeeMoney = None):
        try:
            stime = time.time()
            # 查询财务收费列表
            face_url = self.url['收费'][0] + '?keyword=' + self.odd_num
            response = self.html.get(face_url).text
            response = eval(response)
            planTotalFee = response['result']['items'][0]['planTotalFee']
            realtotalFee = response['result']['items'][0]['realtotalFee']
            feeGeneralId = response['result']['items'][0]['feeGeneralId']
            delayApplyId = response['result']['items'][0]['delayApplyId']
            feeStage = response['result']['items'][0]['feeStage']
            beforeLoanStatus = response['result']['items'][0]['beforeLoanStatus']
            delayStatus = response['result']['items'][0]['delayStatus']
            overdueStatus = response['result']['items'][0]['overdueStatus']

            #判断收费阶段 BEFORE_LOAN_STAGE=贷前收费，DELAY_FEE_STAGE=展期收费阶段,OVERDUE_FEE_STAGE=逾期收费阶段
            if feeStage == 'BEFORE_LOAN_STAGE':
                fee = '贷前收费'
                charge_url = self.url['收费'][1]
                #判断贷前收费状态!=已收费
                if beforeLoanStatus !='YES_CONFIRM':
                    #判断收取金额不为空
                    if currentCollectFeeMoney != None:
                        currentCollectFeeMoney = int(currentCollectFeeMoney)
                    else:
                        if planTotalFee < realtotalFee:
                            return
                        #收取费用=应收-已收
                        currentCollectFeeMoney = planTotalFee - realtotalFee

                    # 收费办理
                    data1 = {"currentCollectFeeMoney": currentCollectFeeMoney, "chargeDate": self.chargeDate,
                             "companyAccountBank": self.companyAccountBank,"companyAccountId": self.companyAccountId,
                             "companyAccountName": self.companyAccountName,"companyAccountNumber": self.companyAccountNumber,
                             "fundFnFeeGeneralId": feeGeneralId}
                else:
                    return
            elif feeStage == 'DELAY_FEE_STAGE':
                fee = '展期收费'
                charge_url = self.url['收费'][2]
                #展期收费
                if delayStatus != 'YES_CONFIRM':
                    # 判断收取金额不为空
                    if currentCollectFeeMoney != None:
                        currentCollectFeeMoney = int(currentCollectFeeMoney)
                    else:
                        if planTotalFee < realtotalFee:
                            return
                        # 收取费用=应收-已收
                        currentCollectFeeMoney = planTotalFee - realtotalFee

                    data1 = {"delayFee":currentCollectFeeMoney,"chargeDate":self.chargeDate,"companyAccountBank":self.companyAccountBank,
                             "companyAccountId":self.companyAccountId,"companyAccountName":self.companyAccountName,
                             "companyAccountNumber":self.companyAccountNumber,"fundFnFeeGeneralId":feeGeneralId,
                             "delayApplyId":delayApplyId,"bankSerialNumber":"","fileIdList":[],"remark":""}
                else:
                    return
            elif feeStage == 'OVERDUE_FEE_STAGE':
                fee = '逾期收费'
                charge_url = self.url['收费'][3]
                if overdueStatus != 'YES_CONFIRM':
                    # 判断收取金额不为空
                    if currentCollectFeeMoney != None:
                        currentCollectFeeMoney = int(currentCollectFeeMoney)
                    else:
                        if planTotalFee < realtotalFee:
                            return
                        # 收取费用=应收-已收
                        currentCollectFeeMoney = planTotalFee - realtotalFee

                    data1 = {"chargeDate":self.chargeDate,"companyAccountBank":self.companyAccountBank,"companyAccountId":self.companyAccountId,
                             "companyAccountName":self.companyAccountName,"companyAccountNumber":self.companyAccountNumber,
                             "fundFnFeeGeneralId":feeGeneralId,"bankSerialNumber":"","fileIdList":[],"remark":"","overdueFee":currentCollectFeeMoney}
                else:
                    return

            data1 = json.dumps(data1)
            response1 = self.html.post(charge_url, data1, headers={'Content-Type': 'application/json'})
            etime = time.time()
            print(response1.text, '-------------',fee,',处理时间：',etime-stime,'s')
        except:
            return print('收费失败')

    #用款确认
    def Payment_confirmation(self):
        if self.fundType == 'AMOUNT':
            return
        stime =time.time()
        #用款确认列表
        face_url = self.url['用款确认'][0] + '?&keyword=' + self.odd_num
        response = self.html.get(face_url).text
        response = eval(response)
        id = response['result']['items'][0]['id']
        guaranteeId = response['result']['items'][0]['guaranteeId']
        status = response['result']['items'][0]['status']

        face_url2 = self.url['用款确认'][1] + '?id=' + guaranteeId
        response1 = self.html.get(face_url2).text
        response1 = eval(response1)
        radioData = response1['result'][0]['id']

        #判断已提交
        if status == 'COMMITTED':
            return print("该单据已提交用款申请，无需重复操作！")

        #用款确认办理
        data1 = {"radioData":radioData,"usePlanTime": self.stampDate,"remark":"","funderList":[{"id":radioData}],"id": id}
        data1 = json.dumps(data1)
        response1 =self.html.post(self.url['用款确认'][2], data1, headers={'Content-Type': 'application/json'})
        etime = time.time()
        print(response1.text, '-------------用款确认,处理时间：', etime - stime, 's')

    # 收要件
    def collection_requirements(self):
        try:
            #判断是否为拍卖房
            if self.guaranteeBizType=='PMF':
                return

            stime = time.time()
            # 查询收要件列表
            face_url = self.url['收要件'][0] + '?keyword=' + self.odd_num
            response = self.html.get(face_url).text
            response = eval(response)
            # 取值字段
            id = response['result']['items'][0]['id']
            isNeed = response['result']['items'][0]['isNeed']
            takeStatus = response['result']['items'][0]['takeStatus']

            #判断为不需要收取要件 or 已确认收齐状态
            if isNeed != 'YES' or takeStatus == 'COMPLETE':
                return

            # 收取要件
            data1 = {"id":id,"isNeed":"YES","fileIds":[],"remark":"",
            "fnEssentialsTakeRecordList":[{"essentialsAssort":"PERSON","essentialsContentList":["ID_CARD",
            "EBANK"],"AndEssentialsType":[],"essentialsId":id,
            "essentialsTakeAccountList":[{"accountBank":"中国银行通海支行","accountName":"要件1",
            "accountNumber":"432414234234321","id":null,"isEbank":"NO","bankId":"A7525607F855AB2EE0533A00A8C0CD66",
            "accountContentList":[],"accountContentType":[{"label":"网银","value":"EBANK"},{"label":" 单位结算卡",
            "value":"SETTLE"}],"EditFeild":"","accountContent":[{"essentialsCode":"EBANK",
            "essentialsTakeDetail":"网银","isCheck":false,"id":null},{"essentialsCode":"SETTLE",
            "essentialsTakeDetail":" 单位结算卡","isCheck":false,"id":null}]}],"essentialsType":"REDEEM","id":null,
            "remark":null,"takeDate":self.takeDate,"collectType":[{"label":"身份证","value":"ID_CARD"},{"label":"银行卡",
            "value":"BANK_CARD"},{"label":"网银","value":"EBANK"},{"label":"委托书","value":"BAILMENT"},{"label":"其他",
            "value":"OTHER"}],"essentialsContent":[{"essentialsTakeDetail":"身份证","isCheck":true,
            "essentialsCode":"ID_CARD","isSendBack":""},{"essentialsTakeDetail":"银行卡","isCheck":false,
            "essentialsCode":"BANK_CARD","isSendBack":""},{"essentialsTakeDetail":"网银","isCheck":true,
            "essentialsCode":"EBANK","isSendBack":""},{"essentialsTakeDetail":"委托书","isCheck":false,
            "essentialsCode":"BAILMENT","isSendBack":""},{"essentialsTakeDetail":"其他","isCheck":false,
            "essentialsCode":"OTHER","isSendBack":""}],"essentialsTypeSame":"[]"},{"essentialsAssort":"PERSON",
            "essentialsContentList":["BANK_CARD","BAILMENT"],"AndEssentialsType":[],
            "essentialsId":id,"essentialsTakeAccountList":[{"accountBank":"中国银行怒江州分行",
            "accountName":"要件2","accountNumber":"4423432423","id":null,"isEbank":"NO",
            "bankId":"A7525607F7C0AB2EE0533A00A8C0CD66","accountContentList":[],"accountContentType":[{"label":"网银",
            "value":"EBANK"},{"label":" 单位结算卡","value":"SETTLE"}],"EditFeild":"","accountContent":[{"essentialsCode":"EBANK",
            "essentialsTakeDetail":"网银","isCheck":false,"id":null},{"essentialsCode":"SETTLE","essentialsTakeDetail":" 单位结算卡",
            "isCheck":false,"id":null}]}],"essentialsType":"REPAYMENT","id":null,"remark":null,"takeDate":"2020-11-04",
            "collectType":[{"label":"身份证","value":"ID_CARD"},{"label":"银行卡","value":"BANK_CARD"},{"label":"网银","value":"EBANK"},
            {"label":"委托书","value":"BAILMENT"},{"label":"其他","value":"OTHER"}],"essentialsContent":[{"essentialsTakeDetail":"身份证",
            "isCheck":false,"essentialsCode":"ID_CARD","isSendBack":""},{"essentialsTakeDetail":"银行卡","isCheck":true,
            "essentialsCode":"BANK_CARD","isSendBack":""},{"essentialsTakeDetail":"网银","isCheck":false,"essentialsCode":"EBANK",
            "isSendBack":""},{"essentialsTakeDetail":"委托书","isCheck":true,"essentialsCode":"BAILMENT","isSendBack":""},
            {"essentialsTakeDetail":"其他","isCheck":false,"essentialsCode":"OTHER","isSendBack":""}],"essentialsTypeSame":"[]"}],
            "essentialsType":["REDEEM","REPAYMENT"]}

            data1 = json.dumps(data1,ensure_ascii=False)
            response1 = self.html.post(self.url['收要件'][1], data1.encode(), headers={'Content-Type': 'application/json'})
            print(response1.text, '-------------收取要件')

            # 确认收齐
            data2 = {"id": id}
            data2 = json.dumps(data2)
            response2 = self.html.post(self.url['收要件'][2], data2, headers={'Content-Type': 'application/json'})
            etime = time.time()
            print(response2.text, '-------------已确认收齐,处理时间:',etime-stime,'s')
        except:
            return print('收取要件失败')

    # 执行岗备注
    def insertRiskExecutionRemarks(self):
        try:
            # 判断是否为拍卖房
            if self.guaranteeBizType=='PMF':
                return

            stime = time.time()
            # 查询执行岗备注列表
            face_url = self.url['执行岗备注'][0] + '?keyword=' + self.odd_num + '&orgId=' + self.orgId + '&companyId=' + self.companyId
            response = self.html.get(face_url).text
            response = eval(response)
            # 取值字段
            id = response['result']['items'][0]['id']
            orderId = response['result']['items'][0]['orderId']
            riskApprovalId = response['result']['items'][0]['riskApprovalId']

            # 执行岗备注办理
            data1 = {"companyId": self.companyId, "id": id, "informationSituation": "COMPLETE"
                , "orderId": orderId, "riskApprovalId": riskApprovalId,
                     "riskExecutionRemarksFileFormList": [], "approvalOpinions": "执行岗备注通过"}

            data1 = json.dumps(data1)
            response1 = self.html.post(self.url['执行岗备注'][1], data1, headers={'Content-Type': 'application/json'})
            etime = time.time()
            print(response1.text,'-------------执行岗备注,处理时间：',etime-stime,'s')
        except Exception as e:
            return print(e.args,'执行岗备注失败')

    # 保函寄送
    def queryRiskGuaranteeMainPage(self):
        try:
            stime = time.time()
            # 查询保函寄送列表
            face_url = self.url['保函寄送'][0] + '?keyword=' + self.odd_num
            response = self.html.get(face_url).text
            response = eval(response)
            # 取值字段
            guaranteeMainId = response['result']['items'][0]['id']
            orderId = response['result']['items'][0]['orderId']
            sendState = response['result']['items'][0]['sendState']
            fundIds = response['result']['items'][0]['fundIds'].split(',')[-1]

            if sendState == 'SEND':
                return print('该单据已寄送保函，无需重复操作！')

            # 保函寄送办理
            data1 = {"guaranteeMainId": guaranteeMainId, "sendTime": self.takeDate, "addressee": "",
                     "addresseeType": "BANK"
                , "fundId": fundIds, "sendType": "EXPRESS", "remark": "备注1"}
            data1 = json.dumps(data1, ensure_ascii=False)
            response1 = self.html.post(self.url['保函寄送'][1], data1.encode(), headers={'Content-Type': 'application/json'})
            etime = time.time()
            print(response1.text, '-------------保函寄送,处理时间：',etime-stime,'s')
        except Exception as e:
            return print(e.args, '保函寄送失败')

    # 资金安排
    def financial_arrangement(self):
        def financial_arrangement_handle(fundorglist=[]):
            '''资金安排办理'''
            face_url1 = self.url['资金到账']['资金安排'][1] + '?id=' + id
            face_url2 = self.url['资金到账']['资金安排'][2] + '?orderId=' + orderId
            message_response1 = self.html.get(face_url1).text
            message_response1 = eval(message_response1)
            message_response2 = self.html.get(face_url2).text
            message_response2 = eval(message_response2)
            fundApplyRecordId = message_response1['result']['fundOrgList'][0]['fundApplyRecordId']
            fundOrgId = message_response1['result']['fundOrgList'][0]['fundOrgId']
            loanDetailsId = ''
            for i in message_response2['result']:
                loanDetailsId = loanDetailsId + ',' + i['id']
            loanDetailsId = loanDetailsId[1:]  # 去除第一个逗号，

            if fundorglist == []:
                fundOrgList = [{"applyDate": self.takeDate, "applyDays": 1, "applyMoney": str(loanMoney),
                                "fundApplyRecordId": fundApplyRecordId, "fundOrgId": fundOrgId,
                                "loanDetailsId": loanDetailsId}]
            else:
                fundOrgList = fundorglist

            data = {"id": id, "remark": "无", "fundOrgList": fundOrgList}

            data = json.dumps(data, ensure_ascii=False)
            response1 = self.html.post(self.url['资金到账']['资金安排'][3], data.encode(),
                                       headers={'Content-Type': 'application/json'})
            return response1, fundOrgId

        def financial_arrangement_audit():
            '''资金选择工行需审批'''
            response = self.html.get(face_url).text
            response = eval(response)
            processInstanceId = response['result']['items'][0]['processInstanceId']
            if processInstanceId == '':
                pass
            else:
                # 办理审批
                t = task_approval(odd_num=self.odd_num, head_url=self.head_url,
                                  handing_username=self.handing_username, handing_password=self.handing_password,
                                  configCode='FUND_ACCOUNT_OUT')
                t.platform_task()

        if self.fundType == 'CASH':
            stime = time.time()
            time.sleep(1)
            face_url = self.url['资金到账']['资金安排'][0] + '?keyword=' + self.odd_num
            message_response = self.html.get(face_url).text
            message_response = eval(message_response)
            id = message_response['result']['items'][0]['id']
            orderId = message_response['result']['items'][0]['orderId']
            loanMoney = message_response['result']['items'][0]['loanMoney']
            auditStatus = message_response['result']['items'][0]['auditStatus']
            fundOrgList = message_response['result']['items'][0]['fundOrgList']

            if auditStatus != 'PASS':
                if fundOrgList != []:
                    '''判断资金安排历史有值，循环获取资金安排历史获取安排状态'''
                    fundorglist = []
                    applyMoney_Sum = 0
                    need_start = 0
                    need_Approval = 0
                    for i in fundOrgList:
                        auditStatus = i['auditStatus']
                        applyMoney = i['applyMoney']
                        fundOrgId = i['fundOrgId']
                        fundApplyRecordId = i['id']
                        loanDetailsId = i['loanDetailsId']
                        applyDate = time_stamp_to_local(i['applyDate'],'%Y-%m-%d')
                        applyMoney_Sum += applyMoney

                        #判断状态为驳回、撤销
                        if auditStatus in ['NO_AUDIT']:
                            need_start += 1
                            fundorglist.append({"applyDate": applyDate,"applyDays": 1, "applyMoney": str(applyMoney), "fundApplyRecordId": fundApplyRecordId,"fundOrgId": fundOrgId, "loanDetailsId": loanDetailsId})

                        #判断状态为审批中
                        elif auditStatus == 'IN_AUDIT':
                            need_Approval += 1

                    #判断资金安排列表驳回、撤销状态的数据是否大于0，大于0则办理资金安排，并自动办理审批
                    if need_start > 0:
                        response1,fundOrgId = financial_arrangement_handle(fundorglist)

                        if '实时可用额度不足' in eval(response1.text)['message']:
                            a = add_quota(head_url=self.head_url, fundOrgId=fundOrgId, username=self.handing_username,
                                          password=self.handing_password)
                            a.add_insertFundPackage()
                            self.financial_arrangement()
                        financial_arrangement_audit()
                        etime = time.time()
                        print(response1.text, '-------------资金安排,处理时间：', etime - stime, 's')
                    #判断资金安排列表审批中状态的数据大于0
                    elif need_Approval > 0:
                        financial_arrangement_audit()

                    #对撤销审批，进行自动重新发起
                    elif loanMoney > applyMoney_Sum:
                        print(applyMoney_Sum)

                else:
                    '''判断为资金安排历史无值，第一次发起资金安排，只存在一条数据'''
                    # 判断状态为未安排
                    if auditStatus in ['NO_AUDIT', 'WORK_FLOW_REJECT']:
                        response1,fundOrgId = financial_arrangement_handle()
                        if '实时可用额度不足' in eval(response1.text)['message']:
                            a = add_quota(head_url=self.head_url, fundOrgId=fundOrgId, username=self.handing_username,
                                          password=self.handing_password)
                            a.add_insertFundPackage()
                            self.financial_arrangement()
                        financial_arrangement_audit()
                        etime = time.time()
                        print(response1.text, '-------------资金安排,处理时间：', etime - stime, 's')


    # 资料推送
    def fund_arrange(self):
        if self.fundType == 'CASH':
            stime = time.time()
            face_url2 = self.url['资金到账']['资料推送'][0] + '?keyword=' + self.odd_num
            response2 = self.html.get(face_url2).text
            response2 = eval(response2)
            fundOrgList = response2['result']['items'][0]['fundOrgList']
            orderId = response2['result']['items'][0]['orderId']

            face_url3 = self.url['资金到账']['资料推送'][1] + '?id=' + orderId
            response3 = self.html.get(face_url3).text
            response3 = eval(response3)
            if response3['result'] == []:
                payeeAccountName = 1
                payeeAccountBank = 1
                payeeAccountNumber = 1
            else:
                payeeAccountBank = response3['result'][0]['accountBank']
                payeeAccountName = response3['result'][0]['accountName']
                payeeAccountNumber = response3['result'][0]['accountNumber']

            #多次推送
            for i in fundOrgList:
                id = i['id']
                pushStatus = i['pushStatus']

                #推送“未推送”状态数据
                if pushStatus =='NO_PUSH':
                    data2 = {"id": id, "payeeAccountBank": payeeAccountBank, "payeeAccountName": payeeAccountName,
                             "payeeAccountNumber": payeeAccountNumber, "pushType": "OFF_LINE", "remark": ""}

                    data2 = json.dumps(data2, ensure_ascii=False)
                    response2 = self.html.post(self.url['资金到账']['资料推送'][2], data2.encode(),
                                               headers={'Content-Type': 'application/json'})
                    etime = time.time()
                    print(response2.text, '-------------资金推送,处理时间：', etime - stime, 's')

    # 资金到账(billingStatus:赎楼状态)
    def updateArrivalAccountStatus(self):
        try:
            stime = time.time()
            # 查询资金到账列表
            face_url = self.url['资金到账']['到账管理'][0] + '?keyword=' + self.odd_num
            response = self.html.get(face_url).text
            response = eval(response)
            # 取值字段
            fundOrgList = response['result']['items'][0]['fundOrgList']
            orderId = response['result']['items'][0]['orderId']
            loanMoney = response['result']['items'][0]['loanMoney']

            #多次到账
            for i in fundOrgList:
                id = i['id']
                arrivalAccountStatus = i['arrivalAccountStatus']

                #办理“未到账”状态的数据
                if arrivalAccountStatus == 'NO':
                    # 到账办理
                    data1 = {"sourceAccountName": "丽丽", "sourceAccountNumber": "130000000000", "sourceAccountBank": "高新园分行",
                             "payeeAccountName": self.companyAccountName,
                             "payeeAccountNumber": self.companyAccountNumber, "payeeAccountBank": self.companyAccountBank,
                             "arrivalAccountMoney": loanMoney,
                             "isBankEnterpriseAccount": "NO", "payeeAccountId": self.companyAccountId,
                             "orderId": orderId,
                             "id": id, "arrivalAccountDate": self.takeDate, "arrivalRemark": "","operatorName": "","updateTime": ""}

                    data1 = json.dumps(data1)
                    response1 = self.html.post(self.url['资金到账']['到账管理'][1], data1, headers={'Content-Type': 'application/json'})
                    etime =time.time()
                    print(response1.text, '-------------资金到账,处理时间：',etime-stime,'s')

        except Exception as e:
            return print(e.args, '资金到账失败')

    # 查档查诉讼
    def updateCheckDocAndLawsuit(self):
        try:
            # 判断是否为拍卖房
            if self.guaranteeBizType == 'PMF':
                return

            stime = time.time()
            # 查询查档查诉讼列表
            face_url = self.url['查档查诉讼'][0] + '?keyWord=' + self.odd_num
            response = self.html.get(face_url).text
            response = eval(response)
            # 取值字段
            checkDocLawsuitId = response['result']['items'][0]['checkDocLawsuitId']
            orderId = response['result']['items'][0]['orderId']

            face_url1 = self.url['查档查诉讼'][1] + '?checkDocLawsuitId=' + checkDocLawsuitId
            response1 = self.html.get(face_url1).text
            response1 = eval(response1)
            riskCheckDocId = response1['result']['docModelList'][0]['riskCheckDocId']
            id = response1['result']['id']
            lawsuitFormList = []
            for i in response1['result']['lawsuitModelList']:
                lawsuitFormList.append({"cardId":i['cardId'],"cardType":i['cardType'],"checkDocLawsuitId":i['checkDocLawsuitId'],
                "checkLawsuitTime":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"cltName":i['cltName'],"createOperatorId":i['createOperatorId'],
                "createTime":i['createTime'],"id":i['id'],"identityType":i['identityType'],"lawsuitState":"DISABLE",
                "name":i['name'],"orderId":i['orderId'],"remark":i['remark'],"riskApprovalId":i['riskApprovalId'],
                "riskCheckLawSuitId":i['riskCheckLawSuitId'],"updateOperatorId":i['updateOperatorId'],"updateTime":i['updateTime']})

            # 查档办理
            data1 = {"checkDocState":"ENABLE","checkDocTime":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"id":riskCheckDocId,
                     "riskCheckDocId":riskCheckDocId}

            data1 = json.dumps(data1, ensure_ascii=False)
            response1 = self.html.post(self.url['查档查诉讼'][2], data1.encode(), headers={'Content-Type': 'application/json'})
            print(response1.text,'-------------查档成功')

            # 查诉讼办理
            data1 = {"approvalOpinions": "通过", "approvalState": "PASS", "checkDocLawsuitId": checkDocLawsuitId,
                     "fileList":[],"id": checkDocLawsuitId, "lawsuitFormList": lawsuitFormList,"orderId": orderId}

            data1 = json.dumps(data1,ensure_ascii=False)
            response1 = self.html.post(self.url['查档查诉讼'][3], data1.encode(), headers={'Content-Type': 'application/json'})
            etime =time.time()
            print(response1.text, '-------------查诉讼成功,处理时间：',etime-stime,'s')
        except Exception as e:
            return print(e.args,'查档查诉讼失败')

    # 收取保证金
    def deposit_collection(self):
        try:
            stime = time.time()
            # 查询出款列表
            face_url = self.url['收取保证金'][0] + '?keyword=' + self.odd_num
            response = self.html.get(face_url).text
            response = eval(response)
            # 取值字段
            totalPlanAssureMoney = response['result']['items'][0]['totalPlanAssureMoney']
            orderId = response['result']['items'][0]['orderId']

            #可收保证金为0，结束方法
            if totalPlanAssureMoney == 0:
                return

            # 收取保证金办理
            data1 = {"takeMoney": totalPlanAssureMoney, "takeDate": self.chargeDate, "accountBank": self.companyAccountBank,
                     "accountId": self.companyAccountId,
                     "accountName": self.companyAccountName, "accountNumber": self.companyAccountNumber, "orderId": orderId, "remark": "备注1"}

            data1 = json.dumps(data1,ensure_ascii=False)
            response1 = self.html.post(self.url['收取保证金'][1], data1.encode(), headers={'Content-Type': 'application/json'})
            etime = time.time()
            print(response1.text, '-------------收取保证金，处理时间：',etime-stime,'s')
        except:
            return print('收取保证金失败')

    # 出款申请
    def disbursement_application(self):
        try:
            # 查询赎楼列表
            face_url = self.url['出款申请'][0] + '?keyword=' + self.odd_num
            response = self.html.get(face_url).text
            response = eval(response)
            # 取值字段
            billingDetailsId = response['result']['items'][0]['billingDetailsId']
            arrivalAccountMoney = response['result']['items'][0]['arrivalAccountMoney']
            orderId = response['result']['items'][0]['orderId']

            face_url1 = self.url['出款申请'][1] + '?orderId=' + orderId
            response1 = self.html.get(face_url1).text
            response1 = eval(response1)

            face_url2 = self.url['出款申请'][2] + '?id=' + orderId
            response2 = self.html.get(face_url2).text
            response2 = eval(response2)
            #获取原贷款银行
            loanLenderModel = response2['result'][0]['loanLenderModel']
            if loanLenderModel == None:
                '''当原贷款机构、个人值返回为空，取银行'''
                oldLoanBankId = response2['result'][0]['loanMbId']
                oldLoanBankName = response2['result'][0]['loanMbName']
            else:
                oldLoanBankId = loanLenderModel['id']
                oldLoanBankName = loanLenderModel['lenderName']

            # 循环发起申请
            for i in range(len(response1['result'])):
                response1 = self.html.get(face_url1).text
                response1 = eval(response1)

                # 根据金额判断能否发起申请
                if response1['result'][i]['notBillingOutMoney'] == 0:
                    continue
                else:
                    loanDetailsId = response1['result'][i]['id']
                    notBillingOutMoney = response1['result'][i]['notBillingOutMoney']

                    # 出款申请办理
                    data1 = {"billingDetailsId": billingDetailsId,
                             "billingAccountList": [{"billingMoney": notBillingOutMoney,
                                                     "payeeAccountBank": "收款开户行1", "payeeAccountName": "收款账户1",
                                                     "payeeAccountNumber": "13135435435",
                                                     "payeeAccountType": "ELSE"}],"oldLoanBankName": oldLoanBankName,"oldLoanBankId": oldLoanBankId,
                             "billingTotalMoney": notBillingOutMoney, "loanDetailsId": loanDetailsId,
                             "orderId": orderId, "orgId": "2dbb1bc7-8f87-431b-b64b-7fb9850233aa", "remark": "备注1"}

                    data1 = json.dumps(data1, ensure_ascii=False, indent=4)
                    print(data1)
                    # response1 = self.html.post(self.url['出款申请'][3], data1.encode(),
                    #                            headers={'Content-Type': 'application/json'})
                    # print(response1.text, '-------------出款申请')

        except Exception as e:
            return print(e.args, '出款申请失败')

    # 出款审批
    def auditBilling(self):
        try:
            # 判断是否为自赎业务
            # if self.isRedeemselfBiz == 'NO' or (self.isRedeemselfBiz == 'YES' and collectState == 'HAVE_COLLECT'):
            # 查询出款审批列表
            face_url = self.url['出款审批'][0] + '?keyword=' + self.odd_num
            response = self.html.get(face_url).text
            response = eval(response)
            # 取值字段
            billingDetailsId = response['result']['items'][0]['billingDetailsId']
            face_url1 = self.url['出款审批'][1] + '?id=' + billingDetailsId
            response1 = self.html.get(face_url1).text
            response1 = eval(response1)

            sourceAccountBank = response1['result']['bankList'][0]['accountBank']
            sourceAccountName = response1['result']['bankList'][0]['accountName']
            sourceAccountNumber = response1['result']['bankList'][0]['accountNumber']
            isBankEnterpriseAccount = response1['result']['bankList'][0]['isBankEnterpriseAccount']
            totalBillingMoney = response1['result']['totalBillingMoney']
            orderId = response1['result']['orderId']

            # 循环获取对应出款的所需字段
            billingAccountList = []
            for i in range(len(response1['result']['billingAccountList'])):
                id = response1['result']['billingAccountList'][i]['id']
                billingMoney = response1['result']['billingAccountList'][i]['billingMoney']
                billingRecordId = response1['result']['billingAccountList'][i]['billingRecordId']
                payeeAccountBank = response1['result']['billingAccountList'][i]['payeeAccountBank']
                payeeAccountName = response1['result']['billingAccountList'][i]['payeeAccountName']
                payeeAccountNumber = response1['result']['billingAccountList'][i]['payeeAccountNumber']

                billingAccountList_add = {"id": id, "billingMoney": billingMoney,
                                          "billingRecordId": billingRecordId,
                                          "showBank": payeeAccountBank, "payeeAccountBank": payeeAccountBank,
                                          "payeeAccountBankNum": "", "payeeAccountName": payeeAccountName,
                                          "payeeAccountNumber": payeeAccountNumber,
                                          "payeeAccountType": "ELSE", "payeeType": 1,
                                          "sourceAccountBank": sourceAccountBank,
                                          "sourceAccountName": sourceAccountName,
                                          "sourceAccountNumber": sourceAccountNumber,
                                          "isBankEnterpriseAccount": isBankEnterpriseAccount}
                billingAccountList.append(billingAccountList_add)

            # 出款审批办理
            data1 = {"billingAccountList": billingAccountList, "billingDetailsId": billingDetailsId,
                     "billingTotalMoney": totalBillingMoney, "orderId": orderId,
                     "orgId": "2dbb1bc7-8f87-431b-b64b-7fb9850233aa", "remark": ""}

            data1 = json.dumps(data1, ensure_ascii=False)
            response1 = self.html.post(self.url['出款审批'][2], data1.encode(), headers={'Content-Type': 'application/json'})
            print(response1.text, '-------------出款审批')
        except Exception as e:
            return print(e.args, '出款审批失败')

    # 流程审批
    def process_approval(self):
        try:
            t = task_approval(odd_num=self.odd_num, head_url=self.head_url,handing_username=self.handing_username,handing_password=self.handing_password,configCode='FUND_BILLING_OUT')
            t.platform_task()
        except:
            return print('流程审批失败')

    # 出款、复核
    def payment(self):
        try:
            # 查询出款列表
            face_url = self.url['出款'][0] + '?keyword=' + self.odd_num
            message_response = self.html.get(face_url).text
            message_response = eval(message_response)
            # 取值字段
            billingDetailsId = message_response['result']['items'][0]['billingDetailsId']
            billingTotalMoney = message_response['result']['items'][0]['loanMoney']
            allotMoney = message_response['result']['items'][0]['allotMoney']
            arrivalAccountMoney = message_response['result']['items'][0]['arrivalAccountMoney']
            billingMoney = message_response['result']['items'][0]['billingRecordList'][0]['billingMoney']
            fundOrgName = message_response['result']['items'][0]['fundOrgName']
            orderId = message_response['result']['items'][0]['orderId']
            finBillingRecordId = message_response['result']['items'][0]['billingRecordList'][0]['id']

            face_url1 = self.url['出款'][1] + '?orderId=' + orderId
            message_response1 = self.html.get(face_url1).text
            message_response1 = eval(message_response1)
            fundApplyRecordId = message_response1['result'][0]['fundApplyRecordId']
            fundOrgId = message_response1['result'][0]['fundOrgId']
            notBillingOutMoney = message_response1['result'][0]['notBillingOutMoney']

            face_url2 = self.url['出款审批'][1] + '?id=' + billingDetailsId
            message_response2 = self.html.get(face_url2).text
            message_response2 = eval(message_response2)
            id = message_response2['result']['billingAccountList'][0]['id']
            billingMoney = message_response2['result']['billingAccountList'][0]['billingMoney']
            billingRecordId = message_response2['result']['billingAccountList'][0]['billingRecordId']
            payeeAccountBank = message_response2['result']['billingAccountList'][0]['payeeAccountBank']
            payeeAccountBankNum = message_response2['result']['billingAccountList'][0]['payeeAccountBankNum']
            payeeAccountName = message_response2['result']['billingAccountList'][0]['payeeAccountName']
            payeeAccountNumber = message_response2['result']['billingAccountList'][0]['payeeAccountNumber']
            payeeAccountType = message_response2['result']['billingAccountList'][0]['payeeAccountType']
            payeeType = message_response2['result']['billingAccountList'][0]['payeeType']
            sourceAccountBank = message_response2['result']['billingAccountList'][0]['sourceAccountBank']
            sourceAccountName = message_response2['result']['billingAccountList'][0]['sourceAccountName']
            sourceAccountNumber = message_response2['result']['billingAccountList'][0]['sourceAccountNumber']
            isBankEnterpriseAccount = message_response2['result']['billingAccountList'][0]['isBankEnterpriseAccount']

            # 出款、复核办理
            data1 = {"billingAccountList":[{"id":id,"billingMoney":billingMoney,"billingRecordId":billingRecordId,
                    "showBank":payeeAccountBank,"payeeAccountBank":payeeAccountBank,"payeeAccountBankNum":payeeAccountBankNum,
                    "payeeAccountName":payeeAccountName,"payeeAccountNumber":payeeAccountNumber,"payeeAccountType":payeeAccountType,
                    "payeeType":payeeType,"sourceAccountBank":sourceAccountBank,"sourceAccountName":sourceAccountName,
                    "sourceAccountNumber":sourceAccountNumber,"isBankEnterpriseAccount":isBankEnterpriseAccount}],"billingDetailsId": billingDetailsId,
                     "billingDate": self.takeDate,"billingTotalMoney": billingTotalMoney,"fundBillingRecordFormList":[{"allotMoney":allotMoney,
                     "arrivalAccountMoney":arrivalAccountMoney,"billingMoney":billingMoney,
                     "fundApplyRecordId":fundApplyRecordId,"fundOrgId":fundOrgId,"fundOrgName":fundOrgName,
                     "notBillingOutMoney":notBillingOutMoney,"selected":false,"orderId":orderId,"finBillingRecordId":finBillingRecordId,
                     "AccountType":"COMPANY","SubtotalNotBillingOutMoney":billingMoney,"withdrawal":id,
                     "accountName":sourceAccountName,"accountBank":sourceAccountBank,"accountNumber":sourceAccountNumber}]}
            data1 = json.dumps(data1, ensure_ascii=False)
            response1 = self.html.post(self.url['出款'][2], data1.encode(), headers={'Content-Type': 'application/json'})
            print(response1.text, '-------------出款')

            # 复核操作
            # data2 = {"billingDetailsId": billingDetailsId, "billingDate": self.takeDate,
            #          "billingTotalMoney": billingTotalMoney}
            # data2 = json.dumps(data2, ensure_ascii=False)
            # response2 = self.html.post(url['出款'][3], data2.encode(), headers={'Content-Type': 'application/json'})
            # print(response2.text, '-------------复核')
            # self.foreclosure_building()
        except:
            return print('出款、复核失败')

    #核对赎楼凭证
    def check_voucher(self):
        # 查询核对赎楼凭证列表
        face_url = self.url['核对赎楼凭证'][0] + '?checkStatus=UNCHECKED&keyword='+self.odd_num
        response = self.html.get(face_url).text
        response = eval(response)

        id = response['result']['items'][0]['billingRecordCheckList'][0]['redeemId']
        face_url1 = self.url['核对赎楼凭证'][1] + '?id=' + id
        response1 = self.html.get(face_url1).text
        response1 = eval(response1)

        # 取值字段
        orderId = response1['result']['orderId']
        redeemType = response1['result']['redeemType']
        redeemRecordId = response1['result']['id']

        #办理核对赎楼凭证
        data = {"checkStatus":"CHECKED","orderId":orderId,
                "redeemCheckRecordSaveForm":{"redeemType":redeemType,
                "redeemRecordId":redeemRecordId}}

        data=json.dumps(data,ensure_ascii=False)
        response2 = self.html.post(self.url['核对赎楼凭证'][2],data.encode(),headers={'Content-Type': 'application/json'})
        print(response2.text,'-------------核对赎楼凭证')

    #二次还款(二次到账、二次出款等)
    def second_repayment(self,collectState=''):
        #发起二次还款
        def second_repayment_apply():
            # 查询二次还款申请列表
            face_url = self.url['二次还款']['发起二次还款'][0] + '?keyword=' + self.odd_num + '&orgId=' + self.orgId1 + '&cityOrgId=' + self.cityOrgId1 + '&isCityChange=true'
            response = self.html1.get(face_url).text
            response = eval(response)
            # 取值字段
            twoBillingApplyId = response['result']['items'][0]['billingTwoApplyId']
            applyBillingMoney = response['result']['items'][0]['redeemHouseAmount']

            # 发起二次还款
            data1 = {"twoBillingApplyId" : twoBillingApplyId , "applyBillingDate" : self.takeDate,
                    "applyBillingMoney" : applyBillingMoney}

            data1 = json.dumps(data1, ensure_ascii=False)
            response1 = self.html1.post(self.url['二次还款']['发起二次还款'][1], data1.encode(),
                                       headers={'Content-Type': 'application/json'})
            print(response1.text, '-------------发起二次还款')

        #二次到账
        def second_arrival():
            # 查询二次还款列表
            face_url = self.url['二次还款']['二次到账'][0] + '?keyword=' + self.odd_num
            response = self.html.get(face_url).text
            response = eval(response)
            # 取值字段
            arrivalAccountMoney = response['result']['items'][0]['billingTwoApplyMoney']
            orderId = response['result']['items'][0]['orderId']
            twoAccountId = response['result']['items'][0]['twoAccountId']
            id = response['result']['items'][0]['twoAccountId']

            # 二次到账办理
            data1 = { "sourceAccountName":"1","sourceAccountNumber":"1","sourceAccountBank":"1",
                    "payeeAccountName": self.companyAccountName,"payeeAccountNumber": self.companyAccountNumber,
                    "payeeAccountBank": self.companyAccountBank,"arrivalAccountMoney":arrivalAccountMoney,
                    "payeeAccountId": self.companyAccountId,"id": id,"arrivalAccountDate": self.takeDate,
                    "arrivalRemark":"","orderId":orderId,"twoAccountId":twoAccountId}

            data1 = json.dumps(data1, ensure_ascii=False)
            response1 = self.html.post(self.url['二次还款']['二次到账'][1], data1.encode(),
                                        headers={'Content-Type': 'application/json'})
            print(response1.text, '-------------二次到账')

        #二次出款申请
        def second_application():
            # 查询二次还款列表
            face_url = self.url['二次还款']['二次到账'][0] + '?keyword=' + self.odd_num
            response = self.html.get(face_url).text
            response = eval(response)
            # 取值字段
            arrivalAccountMoney = response['result']['items'][0]['billingTwoApplyMoney']
            orderId = response['result']['items'][0]['orderId']
            billingDetailsId = response['result']['items'][0]['billingDetailsId']

            # 二次出款申请办理
            data1 = {"billingDetailsId":billingDetailsId,
                    "billingAccountList":[{"billingMoney":arrivalAccountMoney,"payeeAccountBank":"1",
                    "payeeAccountName":"1","payeeAccountNumber":"1","payeeAccountType":"ELSE"}],
                    "billingTotalMoney":arrivalAccountMoney,"orderId":orderId,"orgId":self.orgId,"remark":""}

            data1 = json.dumps(data1, ensure_ascii=False)
            response1 = self.html.post(self.url['二次还款']['二次出款申请'][0], data1.encode(),
                                       headers={'Content-Type': 'application/json'})
            print(response1.text, '-------------二次出款申请')

        #二次出款审批
        def Approval_of_secondary_payment():
            # 查询二次还款列表
            face_url = self.url['二次还款']['二次到账'][0] + '?keyword=' + self.odd_num
            response = self.html.get(face_url).text
            response = eval(response)
            # 取值字段
            arrivalAccountMoney = response['result']['items'][0]['billingTwoApplyMoney']
            orderId = response['result']['items'][0]['orderId']
            billingDetailsId = response['result']['items'][0]['billingDetailsId']

            # 查询二次还款审批弹窗
            face_url = self.url['二次还款']['二次出款审批'][0] + '?id=' + billingDetailsId
            response = self.html1.get(face_url).text
            response = eval(response)
            # 取值字段
            id = response['result']['billingAccountList'][0]['id']
            billingMoney = response['result']['billingAccountList'][0]['billingMoney']
            billingRecordId = response['result']['billingAccountList'][0]['billingRecordId']
            isBankEnterpriseAccount = response['result']['billingAccountList'][0]['isBankEnterpriseAccount']
            payeeAccountBank = response['result']['billingAccountList'][0]['payeeAccountBank']
            payeeAccountBankNum = response['result']['billingAccountList'][0]['payeeAccountBankNum']
            payeeAccountName = response['result']['billingAccountList'][0]['payeeAccountName']
            payeeAccountNumber = response['result']['billingAccountList'][0]['payeeAccountNumber']
            payeeAccountType = response['result']['billingAccountList'][0]['payeeAccountType']
            sourceAccountBank = response['result']['bankList'][0]['accountBank']
            sourceAccountName = response['result']['bankList'][0]['accountName']
            sourceAccountNumber = response['result']['bankList'][0]['accountNumber']

            # 二次出款审批办理
            data1 = {"billingAccountList":[{"id":id,"billingMoney":billingMoney,"billingRecordId":billingRecordId,
                    "showBank":"1","payeeAccountBank":payeeAccountBank,"payeeAccountBankNum":payeeAccountBankNum,
                    "payeeAccountName":payeeAccountName,"payeeAccountNumber":payeeAccountNumber,
                    "payeeAccountType":payeeAccountType,"payeeType":1,"sourceAccountBank":sourceAccountBank,
                    "sourceAccountName":sourceAccountName,"sourceAccountNumber":sourceAccountNumber,
                    "isBankEnterpriseAccount":isBankEnterpriseAccount}],
                    "billingDetailsId":billingDetailsId,"billingTotalMoney":arrivalAccountMoney,
                    "orderId":orderId,"orgId":self.orgId,"remark":""
}

            data1 = json.dumps(data1, ensure_ascii=False)
            response1 = self.html.post(self.url['二次还款']['二次出款审批'][1], data1.encode(),
                                        headers={'Content-Type': 'application/json'})
            print(response1.text, '-------------二次出款审批')

        #二次出款流程审批
        def second_process_approval():
            try:
                # 判断不为自赎业务 或 为自赎业务且已赎楼补录
                if self.isRedeemselfBiz == 'NO' or (self.isRedeemselfBiz == 'YES' and collectState == 'HAVE_COLLECT'):
                    t = task_approval(odd_num=self.odd_num, head_url=self.head_url,configCode='FUND_TWO_BILLING_OUT')
                    t.platform_task()
            except:
                return print('流程审批失败')

        #二次出款
        def second_payment():
            # 查询二次还款列表
            face_url = self.url['二次还款']['二次到账'][0] + '?keyword=' + self.odd_num
            response = self.html.get(face_url).text
            response = eval(response)
            # 取值字段
            billingDetailsId = response['result']['items'][0]['billingDetailsId']

            # 二次出款办理
            data={"billingDetailsId":billingDetailsId,"billingDate":self.takeDate}

            data1 = json.dumps(data, ensure_ascii=False)
            response1 = self.html.post(self.url['二次还款']['二次出款'][0], data1.encode(),
                                       headers={'Content-Type': 'application/json'})
            print(response1.text, '-------------二次出款')

        #二次还款办理
        def second_repayment_handle():
            # 查询二次还款列表
            face_url = self.url['二次还款']['二次到账'][0] + '?keyword=' + self.odd_num
            response = self.html.get(face_url).text
            response = eval(response)
            # 取值字段
            billingMoney = response['result']['items'][0]['billingRecordList'][0]['billingMoney']
            billingRecordId = response['result']['items'][0]['billingRecordList'][0]['id']
            billingTwoApplyId = response['result']['items'][0]['billingTwoApplyId']
            redeemTotalAmount = response['result']['items'][0]['redeemTotalAmount']
            arrivalAccountMoney = response['result']['items'][0]['billingTwoApplyMoney']
            orderId = response['result']['items'][0]['orderId']

            # 二次还款办理
            data = {"redeemBalanceHandle":"NOT_BACK_COMPANY_ACCOUNT","billingMoney":billingMoney,
                    "billingRecordId":billingRecordId,"billingTwoApplyId":billingTwoApplyId,"orderId":orderId,
                    "fileIdList":[],"interest":0,"penaltyInterest":0,"personReplenishment":0,
                    "realRepayAmount":arrivalAccountMoney,"redeemBalance":0,"redeemDate":self.takeDate,
                    "redeemTotalAmount":redeemTotalAmount,"remark":""}

            data1 = json.dumps(data, ensure_ascii=False)
            response1 = self.html.post(self.url['二次还款']['二次还款'][0], data1.encode(),
                                       headers={'Content-Type': 'application/json'})
            print(response1.text, '-------------二次还款办理')

        second_repayment_apply()  #二次还款发起
        second_arrival()            #二次到账
        second_application()        #二次出款申请
        Approval_of_secondary_payment()#二次出款审批
        second_process_approval()      #二次出款流程审批
        second_payment()               #二次出款
        second_repayment_handle()      #二次还款办理


    # 赎楼
    def foreclosure_building(self,collectState=''):
        try:
            # 查询赎楼列表
            face_url = self.url['赎楼'][0] + '?keyword=' + self.odd_num
            response = self.html.get(face_url).text
            response = eval(response)
            # 取值字段
            orderId = response['result']['items'][0]['orderId']
            billingDetailsId = response['result']['items'][0]['billingDetailsId']

            # 循环赎楼
            for i in range(len(response['result']['items'][0]['billingRecordList'])):
                # 判断是否已赎楼
                if response['result']['items'][0]['billingRecordList'][i]['isRedeem'] == 'YES':
                    continue
                else:
                    #判断是否为自赎业务
                    if self.isRedeemselfBiz == 'NO':
                        billingMoney = response['result']['items'][0]['billingRecordList'][i]['billingMoney']
                        billingRecordId = response['result']['items'][0]['billingRecordList'][i]['id']

                        # 赎楼办理
                        data1 = {"redeemBalanceHandle": "NOT_BACK_COMPANY_ACCOUNT", "billingMoney": billingMoney,
                                 "billingRecordId": billingRecordId, "billingDetailsId":billingDetailsId,"id":"",
                                 "orderId": orderId,"fileIdList": [], "deleteFileIdList":[],"interest": 0,
                                 "penaltyInterest": 0, "personReplenishment": 0,"realRepayAmount": billingMoney,
                                 "redeemBalance": 0, "redeemDate": self.takeDate,"redeemTotalAmount": billingMoney,
                                 "remark": ""}

                        data1 = json.dumps(data1, ensure_ascii=False)
                        response1 = self.html.post(self.url['赎楼'][1], data1.encode(),
                                                   headers={'Content-Type': 'application/json'})
                        print(response1.text, '-------------赎楼')
                        #判断是否为二次还款业务
                        if self.isTwiceRepay == 'YES':
                            self.check_voucher()    #办理核对赎楼凭证
                            self.second_repayment() #办理二次还款

                    #判断是否为自赎且已赎楼补录
                    elif self.isRedeemselfBiz == 'YES' and collectState == 'HAVE_COLLECT':
                        billingMoney = response['result']['items'][1]['billingRecordList'][i]['billingMoney']
                        billingRecordId = response['result']['items'][1]['billingRecordList'][i]['id']

                        # 赎楼办理
                        data1 = {"redeemBalanceHandle": "NOT_BACK_COMPANY_ACCOUNT", "billingMoney": billingMoney,
                                 "billingRecordId": billingRecordId, "orderId": orderId,
                                 "fileIdList": [], "interest": 0, "penaltyInterest": 0, "personReplenishment": 0,
                                 "realRepayAmount": billingMoney, "redeemBalance": 0, "redeemDate": self.takeDate,
                                 "redeemTotalAmount": billingMoney, "remark": ""}

                        data1 = json.dumps(data1, ensure_ascii=False)
                        response1 = self.html.post(self.url['赎楼'][1], data1.encode(),
                                                   headers={'Content-Type': 'application/json'})
                        print(response1.text, '-------------赎楼')

                    else:
                        id = response['result']['items'][0]['billingDetailsId']
                        riskAssetsCreditCityId = response['result']['items'][0]['businessSourceId']
                        suppleOperatorId = self.response['result']['id']
                        cityName = response['result']['items'][0]['cityName']
                        redeemBalance = response['result']['items'][0]['loanMoney']

                        #赎楼补录办理
                        data1 = {
                            "id": id,"riskAssetsCreditCityId": riskAssetsCreditCityId,"orderId": orderId,
                            "suppleOperatorId": suppleOperatorId,"cityName": cityName,"fileIdList": [],
                            "personReplenishment": 0,"redeemAmount": "0","redeemBalance": redeemBalance,
                            "redeemDate": self.chargeDate,"remark": ""}

                        data1 = json.dumps(data1, ensure_ascii=False)
                        response1 = self.html.post(self.url['赎楼'][2], data1.encode(),
                                                   headers={'Content-Type': 'application/json'})
                        print(response1.text, '-------------赎楼补录')

                        #判断原贷款形式是否为组合贷
                        if self.loanType == 'COMBINATION_LOAN':
                            response1 = eval(response1.text)
                            collectState = response1['result']['collectState']
                            self.updateArrivalAccountStatus()
                            self.deposit_collection()
                            self.disbursement_application()
                            self.auditBilling()
                            self.process_approval()
                            self.payment()
                            self.foreclosure_building(collectState=collectState)
                            # 判断是否为二次还款业务
                            if self.isTwiceRepay == 'YES':
                                self.check_voucher()    #办理核对赎楼凭证
                                self.second_repayment(collectState=collectState) #办理二次还款

                        # 判断是否为二次还款业务
                        elif self.isTwiceRepay == 'YES':
                            response1 = eval(response1.text)
                            collectState = response1['result']['collectState']
                            self.check_voucher()        #办理核对赎楼凭证
                            self.second_repayment(collectState=collectState)     #办理二次还款
        except:
            return print('赎楼失败')

    # 取原证
    def insertFnCertTake(self):
        # try:
        # 查询取原证列表
        face_url = self.url['取原证'][0] + '?keyword=' + self.odd_num
        response = self.html.get(face_url).text
        response = eval(response)
        # 取值字段
        orderId = response['result']['items'][0]['orderId']

        # 取原证办理
        data1 = {"actualOperatorPostId":self.positionLinkId,"actualOperatorId":self.id,"actualOperatorName":self.name,
                 "actualHandleType":"PLATFORM","expectDate":self.takeDate,"efcertNumber":"123456","guaranteeId":"",
                 "orderId":orderId,"fileIdList":[],"takeCertDate":self.takeDate}

        data1 = json.dumps(data1, ensure_ascii=False)
        response1 = self.html.post(self.url['取原证'][1], data1.encode(), headers={'Content-Type': 'application/json'})
        print(response1.text, '-------------取原证')
        # except Exception as e:
        #     return print(e.args,'取原证失败')

    # 风控权证办理   CERT_LOGOUT=注销、TRANSFER=过户、TAKE_NEW_CERT=取新证、MORTGAGE=抵押登记
    def cancellation(self, itemCode):
        # 注销
        if itemCode == 'CERT_LOGOUT':
            # 查询原证注销列表
            face_url = self.url['权证管理'][2] + '?keyWord=' + self.odd_num + '&positionType=' + itemCode
            response = self.html.get(face_url).text
            response = eval(response)
            orderId = response['result']['items'][0]['id']
            riskHandleId = response['result']['items'][0]['riskHandleId']

            # 办理原证注销
            data1 = {"actualOperatorPostId":self.positionLinkId,"actualOperatorId":self.id,"actualOperatorName":self.name,
                     "actualHandleType":"PLATFORM","expectDate":self.takeDate,"bizFinishTime":self.takeDate,"orderId":orderId,
                     "riskHandleId":riskHandleId,"id":"","itemCode":itemCode,"fileList":[]}
            data1 = json.dumps(data1, ensure_ascii=False)
            response1 = self.html.post(self.url['权证管理'][3], data1.encode(),
                                       headers={'Content-Type': 'application/json'})
            print(response1.text, '--------办理原证注销')
        # 过户
        elif itemCode == 'TRANSFER':
            # 查询过户列表
            face_url = self.url['权证管理'][4] + '?keyWord=' + self.odd_num + '&positionType=' + itemCode
            response = self.html.get(face_url).text
            response = eval(response)
            orderId = response['result']['items'][0]['id']
            riskHandleId = response['result']['items'][0]['riskHandleId']

            # 办理过户
            data1 = {"actualOperatorPostId":self.positionLinkId,"actualOperatorId":self.id,"actualOperatorName":self.name,
                     "actualHandleType":"PLATFORM","expectDate":self.takeDate,"applyDate":self.takeDate,"replyTime":self.chargeDate,
                     "bizCode":"4321","orderId":orderId,"riskHandleId":riskHandleId,"id":"","itemCode":"TRANSFER","fileList":[]}
            data1 = json.dumps(data1, ensure_ascii=False)
            response1 = self.html.post(self.url['权证管理'][5], data1.encode(),
                                       headers={'Content-Type': 'application/json'})
            print(response1.text, '--------办理过户')
        # 取新证
        elif itemCode == 'TAKE_NEW_CERT':
            # 查询取新证列表
            face_url = self.url['权证管理'][6] + '?keyWord=' + self.odd_num + '&positionType=' + itemCode
            response = self.html.get(face_url).text
            response = eval(response)
            orderId = response['result']['items'][0]['id']
            riskHandleId = response['result']['items'][0]['riskHandleId']

            # 办理过户
            data1 = {"actualOperatorPostId":self.positionLinkId,"actualOperatorId":self.id,"actualOperatorName":self.name,
                     "actualHandleType":"PLATFORM","expectDate":self.takeDate,"bizFinishTime":self.chargeDate,"bizCode":"4321",
                     "orderId":orderId,"riskHandleId":riskHandleId,"id":"","itemCode":"TAKE_NEW_CERT","fileList":[]}
            data1 = json.dumps(data1, ensure_ascii=False)
            response1 = self.html.post(self.url['权证管理'][7], data1.encode(),
                                       headers={'Content-Type': 'application/json'})
            print(response1.text, '--------办理取新证')
        # 抵押登记
        elif itemCode == 'MORTGAGE':
            # 查询取新证列表
            face_url = self.url['权证管理'][8] + '?keyWord=' + self.odd_num + '&positionType=' + itemCode
            response = self.html.get(face_url).text
            response = eval(response)
            orderId = response['result']['items'][0]['id']
            riskHandleId = response['result']['items'][0]['riskHandleId']

            # 办理过户
            data1 = {"actualOperatorPostId":self.positionLinkId,"actualOperatorId":self.id,"actualOperatorName":self.name,
                     "actualHandleType":"PLATFORM","applyDate":self.takeDate,"replyTime":self.takeDate,"bizCode":"4321",
                     "remark":"","orderId":orderId,"riskHandleId":riskHandleId,"id":"","itemCode":"MORTGAGE","fileList":[]}
            data1 = json.dumps(data1, ensure_ascii=False)
            response1 = self.html.post(self.url['权证管理'][9], data1.encode(),
                                       headers={'Content-Type': 'application/json'})
            print(response1.text, '--------办理抵押登记')

    # 资产权证办理
    def give_orders(self):
        # 查询权证管理列表
        face_url = self.url['权证管理'][0] + '?keyword=' + self.odd_num
        time.sleep(0.5)
        response = self.html1.get(face_url).text
        response = eval(response)
        cancelStatus = response['result']['items'][0]['cancelStatus']
        transferNamesStatus = response['result']['items'][0]['transferNamesStatus']
        getNewLicnseStatus = response['result']['items'][0]['getNewLicnseStatus']
        mortgageRegistrationStatus = response['result']['items'][0]['mortgageRegistrationStatus']
        guaranteeId = response['result']['items'][0]['guaranteeId']
        isSuretyTransfer = response['result']['items'][0]['isSuretyTransfer']
        isSuretyRegistration = response['result']['items'][0]['isSuretyRegistration']
        isSuretyCancel = response['result']['items'][0]['isSuretyCancel']
        isSuretyGetnewlicnse = response['result']['items'][0]['isSuretyGetnewlicnse']
        id = response['result']['items'][0]['id']

        # 原证注销
        if cancelStatus == 'WAIT_PLATFORM_CANCEL':
            self.cancellation('CERT_LOGOUT')
        # 资产原证注销办理
        elif cancelStatus == 'NO_CANCEL' and isSuretyCancel == 'YES':
            data = {"actualOperatorPostId":self.positionLinkId,"actualOperatorId":self.id,"actualOperatorName":self.name,
                    "actualHandleType":"PLATFORM","expectDate":self.takeDate,"applyDate":self.takeDate,"fileList":[],
                    "guaranteeId":guaranteeId,"id":id,"itemCode":"CERT_LOGOUT","remark":"","productEvidNo":"","receiptDate":self.takeDate}
            data = json.dumps(data, ensure_ascii=False)
            response1 = self.html.post(self.url['权证管理'][10], data.encode(),
                                       headers={'Content-Type': 'application/json'})
            print(response1.text, '--------原证注销')
        # 过户发指令
        elif transferNamesStatus == 'WAIT_PLATFORM_TRANSFERNAMES':
            self.cancellation('TRANSFER')
        # 资产过户办理
        elif transferNamesStatus == 'WAIT_TRANSFERNAMES' and isSuretyTransfer == 'YES':
            data = {"actualOperatorPostId":self.positionLinkId,"actualOperatorId":self.id,"actualOperatorName":self.name,
                    "actualHandleType":"PLATFORM","expectDate":self.takeDate,"applyDate":self.takeDate,"fileList":[],
                    "guaranteeId":guaranteeId,"id":id,"itemCode":"TRANSFER","remark":"","productEvidNo":"123456",
                    "receiptDate":self.takeDate,"replyTime":self.takeDate}
            data = json.dumps(data, ensure_ascii=False)
            response1 = self.html.post(self.url['权证管理'][10], data.encode(),
                                       headers={'Content-Type': 'application/json'})
            print(response1.text, '--------过户')
        # 取新证发指令
        elif getNewLicnseStatus == 'WAIT_PLATFORM_NEWEVIDENCE':
            self.cancellation('TAKE_NEW_CERT')
        # 资产取新证办理
        elif getNewLicnseStatus == 'WAIT_NEWEVIDENCE' and isSuretyGetnewlicnse == 'YES':
            data = {"actualOperatorPostId":self.positionLinkId,"actualOperatorId":self.id,"actualOperatorName":self.name,
                    "actualHandleType":"PLATFORM","expectDate":self.takeDate,"applyDate":self.takeDate,"fileList":[],
                    "guaranteeId":guaranteeId,"id":id,"itemCode":"TAKE_NEW_CERT","remark":"","productEvidNo":"231232321","receiptDate":self.takeDate}
            data = json.dumps(data, ensure_ascii=False)
            response1 = self.html.post(self.url['权证管理'][10], data.encode(),
                                       headers={'Content-Type': 'application/json'})
            print(response1.text, '--------取新证')
        # 抵押登记发指令
        elif mortgageRegistrationStatus == 'WAIT_PLATFORM_MORTGAGEREGISTRATION':
            self.cancellation('MORTGAGE')
        # 资产抵押登记办理
        elif mortgageRegistrationStatus == 'WAIT_MORTGAGEREGISTRATION' and isSuretyRegistration == 'YES':
            data = {"actualOperatorPostId":self.positionLinkId,"actualOperatorId":self.id,"actualOperatorName":self.name,
                    "actualHandleType":"PLATFORM","applyDate":self.takeDate,"fileList":[],"guaranteeId":guaranteeId,"id":id,
                    "itemCode":"MORTGAGE","remark":"","productEvidNo":"4321","receiptDate":self.takeDate,"replyTime":self.takeDate}
            data = json.dumps(data, ensure_ascii=False)
            response1 = self.html.post(self.url['权证管理'][10], data.encode(),
                                       headers={'Content-Type': 'application/json'})
            print(response1.text, '--------抵押登记')

    # 原证注销
    def cancellation_of_original_certificate(self):
        self.give_orders()

    # 过户
    def transfer(self):
        self.give_orders()

    # 取新证
    def take_new_evidence(self):
        self.give_orders()

    # 抵押登记
    def mortgage_registration(self):
        self.give_orders()

    # 回款
    def payment_collection(self,paymentAmount=None,loanDetail_index=None,repaymentDate=None):
        # 判断是否为现金业务
        if self.fundType == 'CASH':
            # 查询回款列表
            face_url = self.url['回款'][0] + '?keyword=' + self.odd_num
            response = self.html.get(face_url).text
            response = eval(response)
            orderId = response['result']['items'][0]['orderId']
            repaymentGeneralId = response['result']['items'][0]['repaymentGeneralId']

            # 回款弹窗
            face_url1 = self.url['回款'][1] + '?orderId=' + orderId
            response1 = self.html.get(face_url1).text
            response1 = eval(response1)


            #循环借款明细
            for index,i in enumerate(response1['result']):
                #判断是否为手动设置到账资方，不是则跳过
                if loanDetail_index != None:
                    if index != loanDetail_index:
                        continue
                repaymentBranchId = i['repaymentBranchId']
                notRepaymentMoney = i['notRepaymentMoney']
                orderId = i['orderId']
                repaymentMoney = i['repaymentMoney']
                loanDetailId = i['id']

                #判断回款金额是否为空，为空取未回款金额
                if paymentAmount == None:
                    paymentMoney = notRepaymentMoney
                elif paymentAmount > notRepaymentMoney:
                    return print('本次回款金额大于该笔剩余借款的金额!!!')
                else:
                    paymentMoney = paymentAmount

                #判断回款日期是否为空，为空取当前日期
                if repaymentDate ==None:
                    repaymentDate = self.takeDate

                #获取对应的到账资金方
                face_url2 = self.url['回款'][2] + '?loanDetailId=' + loanDetailId
                response2 = self.html.get(face_url2).text
                response2 = eval(response2)
                arrivalAccountMoney = response2['result'][0]['arrivalAccountMoney']
                fundApplyRecordId = response2['result'][0]['fundApplyRecordId']
                fundOrgId = response2['result'][0]['fundOrgId']
                fundOrgName = response2['result'][0]['fundOrgName']

                fundRepaymentRecordFormList = [{"arrivalAccountMoney":arrivalAccountMoney,"fundApplyRecordId":fundApplyRecordId,
                "fundOrgId":fundOrgId,"fundOrgName":fundOrgName,"notRepaymentMoney":notRepaymentMoney,"selected":true,
                "orderId":orderId,"repaymentMoney":paymentMoney,"TotalrepaymentMoney":paymentMoney}]

                # 判断剩余借款是否大于0
                if notRepaymentMoney > 0:
                    data = {
                        "companyAccountBank": self.companyAccountBank, "companyAccountId": self.companyAccountId,
                        "companyAccountName": self.companyAccountName, "companyAccountNumber": self.companyAccountNumber,
                        "companyAccountAll": self.companyAccountAll, "fundRepaymentRecordFormList":fundRepaymentRecordFormList,"fileIdList": [], "remark": "",
                        "repaymentBranchId": repaymentBranchId, "repaymentDate": repaymentDate,
                        "repaymentGeneralId": repaymentGeneralId, "repaymentMoney": paymentMoney,
                        "repaymentSource": "NEW_LOAN", "repaymentOutMoney": 0
                    }
                    data = json.dumps(data, ensure_ascii=False)
                    response3 = self.html.post(self.url['回款'][3], data.encode(),
                                               headers={'Content-Type': 'application/json'})
                    print(response3.text, '--------回款')
                else:
                    print('回款金额超出剩余借款金额！！！')


#主代码12
if __name__ == '__main__':
    head_url='http://192.168.0.58:82'   # http://192.168.0.58:82  or  http://189i0341c8.iok.la:27031

    p = process(odd_num='X2105070012',head_url=head_url,handing_username='17666121214')
    # p.face_signature()             # 平台面签
    # p.nuclear_row()                # 平台核行
    # p.preliminary_operation_review() # 运营初审
    # p.risk_review()                  # 风控初审
    # p.risk_recheck()                 # 风控复审
    # time.sleep(1)
    # p.charge()                      # 收费
    # p.Payment_confirmation()        #用款确认
    # p.collection_requirements()     # 收要件
    # p.insertRiskExecutionRemarks()  # 执行岗备注
    # p.queryRiskGuaranteeMainPage()  # 保函寄送
    #
    # p.financial_arrangement()       #资金安排
    # p.fund_arrange()                #资料推送
    # p.updateArrivalAccountStatus()  # 资金到账
    # p.updateCheckDocAndLawsuit()    # 查档查诉讼
    # p.deposit_collection()          # 收取保证金
    # p.disbursement_application()    # 出款申请
    # p.auditBilling()                # 出款审批
    # p.process_approval()            # 流程审批
    # p.payment()                     # 出款、复核
    # p.foreclosure_building()        # 赎楼
    # p.payment_collection(paymentAmount=100000)          # 回款
    # p.insertFnCertTake()            # 取原证
    # p.cancellation_of_original_certificate()  # 原证注销
    # p.transfer()                    # 过户
    # p.take_new_evidence()           # 取新证
    # p.mortgage_registration()       # 抵押登记
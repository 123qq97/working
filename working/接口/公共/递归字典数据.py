url = {
    '报单列表': ['/web-surety/security/business/guarantee/guaranteePage?keyWord=',
             '/web-surety/security/open/guarantee/pickGuaranteeMessage?id='],
    '面签': [
        '/web-surety/security/interviewVisa/queryInterviewVisaRiskPage?keyword=',
        '/web-surety/security/interviewVisa/submitInterviewVisa'],
    '核行': [
        '/web-surety/security/checkBank/queryCheckBankRiskPage?keyword=',
        '/web-surety/security/checkBank/commitCheckBank'],
    '运营初审': [
        '/web-surety/security/risk/riskOperateApproval/queryRiskOperateToBeApprovalPage',
        '/web-surety/security/risk/riskOperateApproval/receive',
        '/web-surety/security/risk/riskOperateApproval/approvalPass'],
    '风控初审': [
        '/web-surety/security/risk/riskFirstApproval/queryRiskFirstToBeApprovalPage?companyId=f0cfce2d-765d-4a11-99fb-7a572628c883&pageSize=20&currentPage=1&orgId=2dbb1bc7-8f87-431b-b64b-7fb9850233aa&productId=&isReceive=&examinerId=&businessSourceId=&normalType=',
        '/web-surety/security/risk/riskFirstApproval/receive',
        '/web-surety/security/risk/riskFirstApproval/approvalPass'],
    '风控复审': [
        '/web-surety/security/workflow/workflowapprove/queryTaskOfCurrentPerson?processName=E2005110012&startDate=&endDate=&systemKey=RISK_SYS&finishPerson=0f15e23f-e317-414a-a990-c7cd31d073c9&currentPage=1&pageSize=20&positionId=2820f1ef-6a9e-42d6-af6b-f7705beebfef',
        '/web-surety/security/open/task/getHisAndRunTaskListByProcInstId?id=',
        '/web-surety/security/workflow/task/passTask'],
    '收费': [
        '/web-surety/security/fee/queryFundFeePage?limitStartDate=&limitEndDate=&companyId=&feeStage=&pageSize=20&currentPage=1&keyword=E2005110012',
        '/web-surety/security/fee/insertBeforeLoanFee'],
    '收要件': [
        '/web-surety/security/fnEssentialsTake/queryFnEssentialsTakePage?essentialsTakeStatus=&pageSize=20&currentPage=1&companyId=&keyword=E2005110012',
        '/web-surety/security/fnEssentialsTake/saveFnEssentialsTake',
        '/web-surety/security/fnEssentialsTake/takeCompleteConfirm'],
    '执行岗备注': [
        '/web-surety/security/risk/riskExecutionRemarks/queryToBeRiskExecutionRemarksPage?pageSize=20&currentPage=1&keyword=E2005110012&orgId=2dbb1bc7-8f87-431b-b64b-7fb9850233aa&companyId=f0cfce2d-765d-4a11-99fb-7a572628c883',
        '/web-surety/security/risk/riskExecutionRemarks/insertRiskExecutionRemarks'],
    '保函寄送': [
        '/web-surety/security/risk/riskGuaranteeMain/queryRiskGuaranteeMainPage?pageSize=20&currentPage=1&keyword=E2005110012&productId=&businessSourceId=&sendState=',
        '/web-surety/security/risk/riskGuaranteeSend/insertRiskGuaranteeSend'],
    '资金到账': {'资金安排': ['/web-surety/security/fundApply/queryFundApplyPage?keyword=E2005110012',
                      '/web-surety/security/fundApply/pickFundApplyInfo?id=',
                      '/web-surety/security/fundApply/submitFundApply',
                      '/web-surety/security/workflow/workflowapprove/queryTaskOfCurrentPerson?startDate=&endDate=&systemKey=FUND_SYS&finishPerson=0f15e23f-e317-414a-a990-c7cd31d073c9&currentPage=1&pageSize=20&positionId=2820f1ef-6a9e-42d6-af6b-f7705beebfef&processName=',
                      '/web-surety/security/open/task/getHisAndRunTaskListByProcInstId?id=',
                      '/web-surety/security/workflow/task/passTask'], '资料推送': [
        '/web-surety/security/fundApply/queryNoPushFundApplyPage?keyword=E2005110012',
        '/web-surety/security/fundApply/getPayeeAccountByOrderId?id=',
        '/web-surety/security/fundApply/pushFundOrg'], '到账管理': [
        '/web-surety/security/fundApply/queryIsArrivalAccountFundApplyPage?planBillingStartDate=&planBillingEndDate=&fundOrgId=&cityCode=&companyId=&keyword=E2005110012&pageSize=20&currentPage=1',
        '/web-surety/security/fundApply/updateArrivalAccountStatus']},
    '查档查诉讼': [
        '/web-surety/security/risk/riskCheckDocLawsuit/queryUncheckOrders?pageSize=20&currentPage=1&companyId=&productId=&keyWord=E2005110012&planUseTime=&planEndTime=',
        '/web-surety/security/risk/riskCheckDocLawsuit/checkDocAndLawsuitDetail?checkDocLawsuitId=',
        '/web-surety/security/risk/riskCheckDocLawsuit/updateCheckDocAndLawsuit'],
    '收取保证金': [
        '/web-surety/security/billing/queryBillingPage?realBillingStartDate=&realBillingEndDate=&keyword=E2005110012&companyId=&billingStatus=&currentPage=1&pageSize=20',
        '/web-surety/security/fnBusinessAssure/saveFnBusinessAssure'],
    '出款申请': [
        '/web-surety/security/fnRedeem/queryFnRedeemPage?redeemStartDate=&redeemEndDate=&redeemStatus=&companyId=&keyword=E2005110012&currentPage=1&pageSize=20',
        '/web-surety/security/billing/queryLoanDetails?orderId=',
        '/web-surety/security/billing/applyBilling'],
    '出款审批': [
        '/web-surety/security/billing/queryBillingPage?realBillingStartDate=&realBillingEndDate=&keyword=E2005110012&companyId=&billingStatus=&currentPage=1&pageSize=20',
        '/web-surety/security/billing/findBillingAccountByBillingDetailsId?id=',
        '/web-surety/security/billing/auditBilling'],
    '流程审批': [
        '/web-surety/security/workflow/workflowapprove/queryTaskOfCurrentPerson?processName=E2005110012&startDate=&endDate=&systemKey=FUND_SYS&finishPerson=0f15e23f-e317-414a-a990-c7cd31d073c9&currentPage=1&pageSize=20&positionId=2820f1ef-6a9e-42d6-af6b-f7705beebfef',
        '/web-surety/security/open/task/getHisAndRunTaskListByProcInstId?id=',
        '/web-surety/security/workflow/task/passTask'],
    '出款': [
        '/web-surety/security/billing/queryBillingPage?realBillingStartDate=&realBillingEndDate=&keyword=E2005110012&companyId=&billingStatus=&currentPage=1&pageSize=20',
        '/web-surety/security/billing/confirmBilling',
        '/web-surety/security/billing/billingCheckOtp'],
    '赎楼': [
        '/web-surety/security/fnRedeem/queryFnRedeemPage?redeemStartDate=&redeemEndDate=&redeemStatus=&companyId=&keyword=E2005110012&currentPage=1&pageSize=20',
        '/web-surety/security/fnRedeem/saveFnRedeem'],
    '取原证': [
        '/web-surety/security/fnCertTake/queryFnCertTakePage?companyId=&pageSize=20&takeCertStatus=&takeCertDateStart=&takeCertDateEnd=&currentPage=1&keyword=E2005110012',
        '/web-surety/security/fnCertTake/insertFnCertTake'],
    '权证管理': ['/web-surety/security/platformProductEvid/list?keyword=E2005110012',
             '/web-surety/security/platformProductEvid/sendOrerRecord',
             '/web-surety/security/risk/handleAfterForeclosure/queryCertLogout?keyWord=E2005110012&positionType=CERT_LOGOUT',
             '/web-surety/security/risk/handleAfterForeclosure/redeemCertLLogoutSave',
             '/web-surety/security/risk/handleAfterForeclosure/queryTransfer?keyWord=E2005110012&positionType=TRANSFER',
             '/web-surety/security/risk/handleAfterForeclosure/redeemTransferSave',
             '/web-surety/security/risk/handleAfterForeclosure/queryTakeNewCert?keyWord=E2005110012&positionType=TAKE_NEW_CERT',
             '/web-surety/security/risk/handleAfterForeclosure/redeemTakeNewCertSave',
             '/web-surety/security/risk/handleAfterForeclosure/queryTakeNewCert?keyWord=E2005110012&positionType=MORTGAGE',
             '/web-surety/security/risk/handleAfterForeclosure/redeemMortgageSave',
             '/web-surety/security/platformProductEvid/handleAfterSave']
}

#递归获取字典最后的值
def recursive_filtering(data_dict,head_url):
    in_head_url=head_url
    for i in data_dict:
        if type(data_dict[i]) == dict:
            recursive_filtering(data_dict[i],in_head_url)

        else:               #对获取的值处理
            for x,y in enumerate(data_dict[i]):
                y=in_head_url + y
                data_dict[i][x]=y

    return data_dict

# print(recursive_filtering(url,head_url='http://192.168.0.58:82'))


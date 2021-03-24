from 接口.流程.平台流程 import process
from 接口.公共.递归字典数据 import recursive_filtering
import time


if __name__ == '__main__':
    head_url = 'http://192.168.0.65:82'  # http://192.168.0.58:82  or  http://189i0341c8.iok.la:27031

    p = process(odd_num='X2103190015', head_url=head_url,handing_username='18888888888',handing_password='888888')
    # p.face_signature()             # 平台面签
    # p.nuclear_row()                # 平台核行
    # p.preliminary_operation_review() # 运营初审
    # p.risk_review()                  # 风控初审
    # p.risk_recheck()  # 风控复审
    # time.sleep(2)
    # p.charge()                      # 收费
    # p.Payment_confirmation()        #用款确认
    # p.collection_requirements()     # 收要件
    # p.insertRiskExecutionRemarks()  # 执行岗备注
    # p.queryRiskGuaranteeMainPage()  # 保函寄送
    #
    # p.financial_arrangement()  # 资金安排
    # p.fund_arrange()  # 资料推送
    # p.updateArrivalAccountStatus()  # 资金到账
    # p.updateCheckDocAndLawsuit()    # 查档查诉讼
    # p.deposit_collection()          # 收取保证金
    # p.disbursement_application()    # 出款申请
    # p.auditBilling()                # 出款审批
    # p.process_approval()            # 流程审批
    # p.payment()                     # 出款、复核
    # p.foreclosure_building()        # 赎楼
    p.payment_collection(paymentAmount=900000)          # 回款
    # p.insertFnCertTake()            # 取原证
    # p.cancellation_of_original_certificate()  # 原证注销
    # p.transfer()                    # 过户
    # p.take_new_evidence()           # 取新证
    # p.mortgage_registration()       # 抵押登记
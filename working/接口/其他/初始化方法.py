from 接口.公共.登录 import login

global null, true, false
null = None
true = True
false = False



# 登录人参数
def pickPersonInfo_message(url,html):
    pickPersonInfo_url = url['初始化参数']['登录人参数'][0]
    pickPersonInfo_text = html.get(pickPersonInfo_url).text
    pickPersonInfo_dict = eval(pickPersonInfo_text)
    return pickPersonInfo_dict

# 公司账户
def company_account_message(url,orgId,html):
    company_account_url = url['初始化参数']['公司账户'][0] + '?&cityOrgId=' + orgId + '&status=ENABLED'
    response2 = html.get(company_account_url).text
    response2 = eval(response2)
    return response2

# 分行、支行
def fundProvider_message(url,html):
    fundProvider_url = url['初始化参数']['分行、支行'][0] + '?fundProviderType=HEAD&status=ENABLED'
    response4 = html.get(fundProvider_url).text
    response4 = eval(response4)
    parentId = response4['result']['itemList'][0]['id']
    branch_url = url['初始化参数']['分行、支行'][1] + '?parentId=' + parentId + '&fundProviderType=BRANCH&status=ENABLED'
    response5 = html.get(branch_url).text
    response5 = eval(response5)
    return response5

#查询是否需要面签、核行
def isFaceBankCheck_message(url,riskAssetsCreditCityId,html):
    guarateetype_url1 = url['初始化参数']['报单列表'][2] + '?riskAssetsCreditCityId=' + riskAssetsCreditCityId
    response3 = html.get(guarateetype_url1).text
    response3 = eval(response3)
    return response3

# 获取经办人的orgId、cityOrgId
def manager_orgId_message(manager_phone,head_url,manager_password):
    html1,response1 = login(username=manager_phone, head_url=head_url,password=manager_password)
    response1 = eval(response1.text)
    return response1,html1
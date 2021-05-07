import requests
import json
from 接口.公共.登录 import login


head_url = 'http://192.168.0.58:82'
queryBizWarnRemindPage_url = head_url + '/web-surety/security/risk/bizWarn/queryBizWarnRemindPage?positionId=c142988c-e320-4239-9570-7129b1157daa8&positionLinkId=2820f1ef-6a9e-42d6-af6b-f7705beebfef'
html, response = login(username='15865589888', password='123456',head_url=head_url)
null = None
true = 'true'

queryBizWarnRemindPage_result = html.get(queryBizWarnRemindPage_url).text
queryBizWarnRemindPage_result = eval(queryBizWarnRemindPage_result)
for i in queryBizWarnRemindPage_result['result']['items']:
    orderId = i['orderId']
    remindId = i['remindId']
    warnId = i['id']


    data = {"followRemark":"1","handleStatus":"NOT","handleTime":"2021-04-28",
            "warnId":warnId,"orderId":orderId,"remindId":remindId,"followPositionId":"c142988c-e320-4239-9570-7129b1157daa",
            "followPositionName":"admin"}

    data1 = json.dumps(data, ensure_ascii=False)
    response1 = html.post('http://192.168.0.58:82/web-surety/security/risk/bizWarnFollow/insertBizWarnFollow', data1.encode(), headers={'Content-Type': 'application/json'})
    print(response1.text)

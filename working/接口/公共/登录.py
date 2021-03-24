import requests
import json
from 接口.公共.md5加密 import md5_encryption
# from .md5加密 import md5_encryption
'''
environment:切换测试、预发布环境
if else判断是否为传入的链接
'''


def login(head_url='http://192.168.0.58:82',username='13714028085',password='123456',wxOpenId='',loading='false'):
    '''
    
    :param head_url: 
    :param username: 
    :param password: 
    :param wxOpenId: 
    :param loading: 
    :return: 使用md5_encryption加密password
    '''
    #将python无法识别的参数转换为str类型
    global null, true, false
    null = ''
    true = ''
    false = ''

    url=head_url+'/web-surety/login/login'
    params = 'userName=' + username + '&password=' + md5_encryption(password) + '&wxOpenId=' + wxOpenId + '&loading=' + loading
    html = requests.session()
    response = html.get(url, params=params)
    if eval(response.text)['message'] == '处理成功':
        return html,response

    #如果初始、填入密码登录不成功，改用后账号后6为登录
    else:
        params = 'userName=' + username + '&password=' + md5_encryption(username[-6:]) + '&wxOpenId=' + wxOpenId + '&loading=' + loading
        response = html.get(url, params=params)
        return html,response




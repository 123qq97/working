from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

#打开url网址
# url ='https://www.baidu.com/'
# driver.get(url)

#元素定位
#通过id定位
# id = driver.find_element_by_id('kw')
# #通过name定位
# name = driver.find_element_by_name('wd')
# #通过class name定位
# class_name = driver.find_element_by_class_name('s_ipt')
#通过tag name定位
# tag_name = f.find_element_by_tag_name('input')
# #通过完整超链接的文本定位
# link_text = driver.find_element_by_link_text('新闻')
# #通过部分超链接的文本定位
# partial_link_text = driver.find_element_by_partial_link_text('新')
# print(partial_link_text.get_attribute('outerHTML'))

#xpath定位
'''
<input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">

<input type="submit" id="su" value="百度一下" class="bg s_btn">

<a href="http://news.baidu.com" target="_blank" class="mnav c-font-normal c-color-t">新闻</a>
'''
# #属性定位
# id_xpath = driver.find_element_by_xpath('//input[@id="kw"]')
# class_xpath = driver.find_element_by_xpath('//input[@class="s_ipt"]')
# id_class_xpath = driver.find_element_by_xpath('.//input[@id="kw" and @class="s_ipt"]')
# #路径定位-绝对路径
# dir_xath = driver.find_element_by_xpath('/html/body/div[2]/..')
# print(dir_xath.get_attribute('outerHTML'))
# #路径定位-返回上层路径
# back_dir_xath = driver.find_element_by_xpath('/html/body/div/div/div[5]/div/div/form/span[2]/input/..')
# #路径+属性定位
# all_dir_xpath= driver.find_element_by_xpath('//*[@id="form"]/span[1]')
# #模糊定位-属性值
# like_xpath = driver.find_element_by_xpath('//input[contains(@value,"百度")]')
# print(like_xpath.get_attribute('outerHTML'))
# #text定位
# text_xpath = driver.find_element_by_xpath('//a[text()="新闻"]')



#css定位
'''
<input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">

<input type="submit" id="su" value="百度一下" class="bg s_btn">
'''
# #属性定位
# id_css = driver.find_element_by_css_selector('#kw')
# class_css = driver.find_element_by_css_selector('.s_ipt')
# name_css = driver.find_element_by_css_selector('input[name="wd"]')
# #路径定位-索引
# test>span:nth-child(2):表示test目录下第2个元素,并且限制为div元素;
# # test>span:nth-of-type(2):表示test目录下第2个span元素,类似xpath的test/span[2];
# dir_css = driver.find_element_by_css_selector('html>body>div>div>div:nth-child(5)>div>div>form>span:nth-of-type(2)>input')
# first_dir_css =driver.find_element_by_css_selector('html>body>div>div>div:nth-child(5)>div>div>form>span:first-of-type')
# last_dir_css =driver.find_element_by_css_selector('html>body>div>div>div:nth-child(5)>div>div>form>span:last-of-type')
# #路径+属性定位
# all_dir_css = driver.find_element_by_css_selector('ul.s-hotsearch-content>li')

#常用操作方法

# driver.set_window_size(1000,500)   #设置浏览器窗口宽高分别为1920,1080

driver.maximize_window()              #设置浏览器窗口最大化
# driver.minimize_window()              #设置浏览器窗口最小化

# import time
# driver.get('https://www.baidu.com/')
# time.sleep(2)
# driver.refresh()                      #刷新浏览器当前页面

# driver.get('https://www.baidu.com/')
# driver.back()                         #控制浏览器后退

# driver.get('https://www.baidu.com/')
# driver.back()
# driver.forward()                      #控制浏览器前进

# driver.get('https://www.baidu.com/')
# driver.find_element_by_xpath('//*[@id="s-hotsearch-wrapper"]/div/a[1]/div').click()
# driver.close()                        #关闭一个标签页

# driver.get('https://www.baidu.com/')
# driver.find_element_by_xpath('//*[@id="s-hotsearch-wrapper"]/div/a[1]/div').click()
# driver.quit()                           #关闭浏览器

# driver.get('https://www.baidu.com/')
# text_input = driver.find_element_by_xpath('//*[@id="kw"]')
# text_input.send_keys('python教程')       #输入框输入'python教程'

# driver.get('https://www.baidu.com/')
# text_input = driver.find_element_by_xpath('//*[@id="kw"]')
# text_input.send_keys('python教程')
# import time
# time.sleep(3)
# text_input.clear()                         #清除输入框的文本

# driver.get('https://www.baidu.com/')
# driver.find_element_by_xpath('//*[@id="s-hotsearch-wrapper"]/div/a[1]/div').click()     #点击百度热榜按钮

# driver.get('https://www.baidu.com/')
# text_input = driver.find_element_by_xpath('//*[@id="kw"]')
# text_input.send_keys('selenium')
# text_input.submit()                       #提交form表单

# driver.get('https://www.baidu.com/')
# text_input = driver.find_element_by_xpath('//*[@id="kw"]')
# print(text_input.size)                     #打印元素宽高

# driver.get('https://www.baidu.com/')
# get_text = driver.find_element_by_xpath('//*[@id="s-top-left"]/a[1]')
# print(get_text.text)                        #获取元素的文本

# driver.get('https://www.baidu.com/')
# ele = driver.find_element_by_xpath('//*[@id="hotsearch-content-wrapper"]/li[1]/a/span[2]')
# print(ele.is_displayed())                   #判断元素是否可见,true可见，false不可见

# 鼠标操作
from selenium.webdriver.common.action_chains import ActionChains

#单击
# driver.get('http://sahitest.com/demo/clicks.htm')
# click_btn = driver.find_element_by_xpath('//input[@value="click me"]')
# ActionChains(driver).click(click_btn).perform()

#双击
# double_click_btn = driver.find_element_by_xpath('//input[@value="dbl click me"]')
# ActionChains(driver).double_click(double_click_btn).perform()

#右击
# right_click_btn = driver.find_element_by_xpath('//input[@value="right click me"]')
# ActionChains(driver).context_click(right_click_btn).perform()

#移动鼠标到某个元素
# driver.get('http://sahitest.com/demo/mouseover.htm')
# move_in_btn = driver.find_element_by_xpath('//input[@value="Write on hover"]')
# import time
# time.sleep(3)
# ActionChains(driver).move_to_element(move_in_btn).perform()

#移动鼠标到距当前位置(8,29)的点
# driver.get('http://sahitest.com/demo/mouseover.htm')
# move_in_btn = driver.find_element_by_xpath('//input[@value="Write on hover"]')

# #获取元素的x、y坐标
# x = move_in_btn.location.get('x')
# y = move_in_btn.location.get('y')
# ActionChains(driver).move_by_offset(8,29).perform()
# 移动鼠标到距move_in_btn元素(0,-21)的点
# move_in_btn = driver.find_element_by_xpath('//input[@value="Write on hover"]')
# ActionChains(driver).move_to_element_with_offset(move_in_btn,0,-21).perform()
#拖拽drag_to元素到drag_to元素
# driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
# drag_to = driver.find_element_by_xpath('//div[@class="drag"]')
# to_drop = driver.find_element_by_xpath('//div[text()="Item 1"]')
# ActionChains(driver).drag_and_drop(drag_to,to_drop)
#按住鼠标左键拖动drag_to元素，到to_drop元素放开
# drag_to = driver.find_element_by_xpath('//div[@class="drag"]')
# to_drop = driver.find_element_by_xpath('//div[text()="Item 1"]')
# ActionChains(driver).click_and_hold(drag_to).release(to_drop).perform()
#按住鼠标左键拖动drag_to元素，到to_drop元素放开
# drag_to = driver.find_element_by_xpath('//div[@class="drag"]')
# to_drop = driver.find_element_by_xpath('//div[text()="Item 1"]')
# ActionChains(driver).click_and_hold(drag_to).move_to_element(to_drop).release().perform()
#将drag_to元素移动到(13,150)指定坐标
# driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
# drag_to = driver.find_element_by_xpath('//div[@class="drag"]')
# to_drop = driver.find_element_by_xpath('//div[text()="Item 1"]')
# ActionChains(driver).drag_and_drop_by_offset(drag_to,13,150).perform()

#按键、松开
# from selenium.webdriver.common.keys import Keys
# driver.get('http://sahitest.com/demo/keypress.htm')
# key_up_radio = driver.find_element_by_id('r1') # 监测按键升起
# key_down_radio = driver.find_element_by_id('r2') # 监测按键按下
# key_press_radio = driver.find_element_by_id('r3') # 监测按键按下升起
# input = driver.find_elements_by_xpath('//form[@name="f1"]/input')[1] # 输入框
# key_down_radio.click()
# ActionChains(driver).key_down(Keys.CONTROL, input).key_up(Keys.CONTROL).perform()

#键盘事件
# from selenium.webdriver.common.keys import Keys
# import time
# driver.get('https://www.baidu.com/')
# input = driver.find_element_by_xpath('//input[@class="s_ipt"]')
# input.send_keys('selenium')
# time.sleep(1)
# input.send_keys(Keys.BACK_SPACE)    #回退
# time.sleep(1)
# input.send_keys(Keys.CONTROL,'a')   #全选

#获取断言信息
import time
driver.get('https://www.baidu.com/')
driver.find_element_by_xpath('//input[@class="s_ipt"]').send_keys('selenium')
#打印当前页面title
print(driver.title)
#打印当前页面url
print(driver.current_url)
driver.find_element_by_xpath('//input[@value="百度一下"]').click()
#再次打印当前页面title
print(driver.title)
#再次打印当前页面url
print(driver.current_url)
#获取当前元素文本内容
time.sleep(1)
text = driver.find_element_by_xpath('//span[@class="nums_text"]').text
print(text)

#多表单切换
'''
<div id="loginDiv" class="loginUrs" style="width: 400px; height: 302px;">
<iframe name="" frameborder="0" id="x-URS-iframe1614656158852.1558" scrolling="no" style="width: 100%; height: 100%; border: none; background: none;" src="https://passport.126.com/webzj/v1.0.1/pub/index_dl2_new.html?cd=%2F%2Fmimg.127.net%2Fp%2Ffreemail%2Findex%2Funified%2Fstatic%2F2020%2F%2Fcss%2F&amp;cf=urs.126.5be7af1b.css&amp;MGID=1614656158852.1558&amp;wdaId=&amp;pkid=QdQXWEQ&amp;product=mail126"></iframe>
</div>
'''
# driver.get('http://www.126.com')
# iframe_in = driver.find_element_by_xpath('//div[@id="loginDiv"]/iframe')
# driver.switch_to.frame(iframe_in)   #进入iframe标签内
# print(driver.page_source)
# driver.switch_to.default_content()  #跳出iframe标签外
# print(driver.page_source)

#多窗口切换
# driver.get('https://www.baidu.com/')
# print(driver.current_window_handle)     #打印当前窗口句柄
# print(driver.window_handles)            #打印所有窗口句柄
# driver.find_element_by_xpath('//div[@id="s-top-left"]/a[1]').click()
# print(driver.current_window_handle)     #打印当前窗口句柄
# print(driver.window_handles)            #打印所有窗口句柄
# print(driver.page_source)
# driver.switch_to.window(driver.window_handles[1])   #填入第二个窗口句柄切换为第二个窗口
# print(driver.current_window_handle)
# print(driver.page_source)

#警告框处理
# driver.get('D:/git/project_file/testgit/working/接口/公共/案例/test.html')
# driver.find_element_by_xpath('//input[@onclick="showPro()"]').click()
# alert = driver.switch_to.alert         #定位到alert警告框
# print(alert.text)                      #打印警告框内容
# alert.dismiss()                        #点击警告框取消按钮，等于关闭效果
# driver.find_element_by_xpath('//input[@onclick="showPro()"]').click()
# alert.send_keys('2')                   #在警告框中的输入框输入2
# alert.accept()                         #点击警告框确定按钮

#下拉框选择操作
# from selenium.webdriver.support.select import Select
# import time
# driver.get('D:/git/project_file/testgit/working/接口/公共/案例/test.html')
# select_btn = driver.find_element_by_xpath('//select[@id="select_btn"]')
# time.sleep(0.5)
# Select(select_btn).select_by_value('saab')          #通过value值选中
# time.sleep(0.5)
# Select(select_btn).select_by_index(1)                #通过下标来选中
# time.sleep(0.5)
# Select(select_btn).select_by_visible_text('Audi')   #通过文本来选中

#文件上传
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# test_dict = {
#     '账号' : ['文本','//*[@id="app"]/div/section/aside/div[1]/div[2]/form/div[2]/div/div/input','17666121214'],
#     '密码' : ['文本','//*[@id="app"]/div/section/aside/div[1]/div[2]/form/div[4]/div/div/input','123456'],
#     '登录按钮' : ['按钮','//*[@id="app"]/div/section/aside/div[1]/div[2]/div/span'],
#     '业务管理' : ['按钮','//*[@id="app"]/section/section/aside/div/div/div[1]/div/ul//li/div/span[text()="业务管理"]'],
#     '担保导航' : ['按钮','//*[@id="app"]/section/section/aside/div/div/div[1]/div/ul//li/ul//li[text()="担保导航"]'],
#     '资料上传' : ['按钮','//*[@id="mainBox"]/div[2]/div[1]/div/div[4]/div[2]/table/tbody/tr[1]/td[15]/div/span[1]/span'],
#     '上传按钮' : ['按钮','//*[@id="pane-de1f0829-fb18-4728-a05c-69700aff946c"]/div/div[4]/div[2]/table/tbody/tr/td[7]/div/a/span'],
#
# }
# driver.get('http://192.168.0.58:82/login')
#
# for i in test_dict:
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located(
#             (By.XPATH, test_dict[i][1]))
#     )
#     # 文本操作
#     if test_dict[i][0] == '文本':
#         # 执行输入文本
#         element = driver.find_element_by_xpath(test_dict[i][1])
#         element.send_keys(test_dict[i][2])
#     # 按钮操作
#     else:
#         # 执行点击
#         element = driver.find_element_by_xpath(test_dict[i][1])
#         driver.execute_script("arguments[0].click();", element)  # 使用js点击
#
# driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div[1]/div/div/input').send_keys('C:\\Users\JF\Desktop\文件存放\证件资料上传\合同.png')  #上传文件

#cookie操作
# driver.get('http://www.baidu.com')
# print('原始cookie：',driver.get_cookies())                                           #打印所有cookie
# driver.add_cookie({'name':'userName','value':'youname'})         #添加cookie
# driver.add_cookie({'name':'password','value':'youpassword'})    #添加cookie
# driver.get('http://www.baidu.com')
# print('添加两条cookie',driver.get_cookies())
# driver.delete_cookie(name='password')                               #删除name='password'的那条cookie
# print('删除name=‘password’的cookie：',driver.get_cookies())
# driver.delete_all_cookies()                                           #删除所有cookie
# print('删除所有cookie后：',driver.get_cookies())

#调用JavaScript代码
# import time
# driver.get('http://www.baidu.com')
# input_path = driver.find_element_by_xpath('//input[@id="kw"]')
# input_path.send_keys('selenium')
# input_path.submit()
# time.sleep(1)
# page_path= driver.find_element_by_xpath('//*[@id="page"]/div/strong/span[2]') #定位到底部页码
# driver.execute_script("arguments[0].scrollIntoView();", page_path)             #执行js代码，根据元素位置拖动滚动条

#窗口截图
# import time
# driver.get('http://www.baidu.com')
# driver.find_element_by_xpath('//input[@id="kw"]').send_keys('selenium')
# driver.find_element_by_xpath('//input[@id="su"]').click()
# time.sleep(2)
# driver.get_screenshot_as_file(r'C:\Users\JF\Desktop\文件存放\img\baidu_img.jpg')    #截图，并存放在C:\Users\JF\Desktop\文件存放\img路径下
#从selenium库导入webdriver方法
from selenium import webdriver


#调用Chromedriver插件，对Chrome浏览器进行控制
driver = webdriver.Chrome()


#打开网址
driver.get('https://www.baidu.com/')


#元素定位

#通过id值定位
inp = driver.find_element_by_id('kw')

#通过class name值定位
inp1 = driver.find_element_by_class_name('s_ipt')

#通过name值定位
inp2 = driver.find_element_by_name('wd')

#通过链接文本定位
link_text = driver.find_element_by_link_text('百度热榜')

#通过部分链接文本定位
link_text1 = driver.find_element_by_partial_link_text('百度')

#通过tag name值定位
test = driver.find_element_by_class_name('s_btn_wr')
tag_name = test.find_element_by_tag_name('input')

#通过css定位
css_id = driver.find_element_by_css_selector('#kw')                                 #用css方法，根据id值定位
css_class = driver.find_element_by_css_selector('.s_ipt')                           #用css方法，根据class name值定位
css_name = driver.find_element_by_css_selector('[name=wd]')                         #用css方法，根据name值定位
css_path = driver.find_element_by_css_selector('form#form > span > input.s_ipt')  #用css方法，组合定位
css_child = driver.find_element_by_css_selector('form#form :nth-child(2)')         #用css方法，子元素定位

#通过xpath定位
xpath_path = driver.find_element_by_xpath('/html/body/div/div/div[5]/div/div/form/span/input')  #用xpath方法，绝对路径定位
xpath_class = driver.find_element_by_xpath('.//input[@class="s_ipt"]')                              #用xpath方法，根据标签名+节点属性定位
xpath_text = driver.find_element_by_xpath('.//div[text()="百度热榜"]')                               #用xpath方法，根据文本定位


print(xpath_text.get_attribute('outerHTML'))
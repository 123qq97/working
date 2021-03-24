from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class chandao():
    def __init__(self):
        self.key_value = {
            '登录' : {'useraccount' : ('//input[@id="account"]','xurui',),
                    'userpassword' : ('//*[@id="loginPanel"]/div/div[2]/form/table/tbody/tr[2]/td/input','123456'),
                    'click' : '//*[@id="submit"]'},
            'bug页' : {'click' : ('//*[@id="navbar"]/ul/li[4]/a','//*[@id="block4752"]/div[2]/div/div/ul//a[text()="房贷云"]','//*[@id="block4752"]/div[2]/div/div/ul//a[text()="房贷云"]/../a[2]')}
        }

    def login(self):
        for i in self.key_value['登录']:
            if i == 'click':
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, self.key_value['登录'][i]))
                )
                driver.find_element_by_xpath(self.key_value['登录'][i]).click()
            else:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, self.key_value['登录'][i][0]))
                )
                driver.find_element_by_xpath(self.key_value['登录'][i][0]).send_keys(self.key_value['登录'][i][1])

    def bug_page(self):
        for i in self.key_value['bug页']['click']:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, i))
            )
            driver.find_element_by_xpath(i).click()

        title = driver.find_element_by_xpath('//*[@id="bugList"]/tbody/')
        print(title.get_attribute('outerHTML'))

if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    driver.maximize_window()
    driver.get('http://192.168.0.42:8088/index.php?m=user&f=login')
    c = chandao()
    c.login()
    # c.bug_page()

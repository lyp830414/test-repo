#coding=utf-8
import time, os
from splinter.browser import Browser
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


def start_firefox_with_firebug_plug():
    """启动Firefox，并自动加载插件Firebug"""
    firefoxBin = os.path.abspath(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
    os.environ["webdriver.firefox.bin"] = firefoxBin

    firefoxProfile = webdriver.FirefoxProfile()
    tempDir = os.getcwd()
    tempDir = os.path.split(tempDir)[0]
    firebugPlugFile = os.path.join(r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\82bh7hqw.default\extensions", "cehomepage@mozillaonline.com")
    firefoxProfile.add_extension(firebugPlugFile)
    firefoxProfile.set_preference("extensions.firebug.currentVersion", "2.0.7")

    driver = webdriver.Firefox(firefox_profile=firefoxProfile)
    driver.get("https://api.weibo.com/oauth2/authorize?client_id=3054804248&redirect_uri=http%3A%2F%2Fwww.huajiao.com&response_type=code&state=eyJzb3VyY2UiOiJzaW5hIiwicmVkaXJlY3QiOiJodHRwOlwvXC93d3cuaHVhamlhby5jb21cLz9ocmQ0Nzk1IiwidXNlcl9yYW5kIjoiNDY5YWM3NDUzNWY2MjkwMDdhOTZiYjcyNDExMGM2MjciLCJiYW5qdW1wIjoiIn0%3D")

def splinter2(browser):
        browser.find_element_by_id("userId").clear()
        browser.find_element_by_id("userId").send_keys("xiangyuzhenniao")
        browser.find_element_by_id("passwd").clear()
        browser.find_element_by_id('passwd').send_keys('XyznSsz1983@')

        contents = browser.find_element_by_class_name("WB_btn_login")
        if contents:
            contents.click()

def splinterWeibo(url):

    firefoxProfile = FirefoxProfile()
    firefoxProfile.set_preference('plugin.state.flash', '2')

    browser = webdriver.Firefox(firefoxProfile)

    time.sleep(1)

    browser.get(url)

    time.sleep(3)

    contents = browser.find_element_by_class_name("btn-login")
    if contents:
        contents.click()
        contents2 = browser.find_element_by_class_name("sina")
        if contents2:
            contents2.click()

            websize3 = 'https://api.weibo.com/oauth2/authorize?client_id=3054804248&redirect_uri=http%3A%2F%2Fwww.huajiao.com&response_type=code&state=eyJzb3VyY2UiOiJzaW5hIiwicmVkaXJlY3QiOiJodHRwOlwvXC93d3cuaHVhamlhby5jb21cLz9ocmQ0Nzk1IiwidXNlcl9yYW5kIjoiNDY5YWM3NDUzNWY2MjkwMDdhOTZiYjcyNDExMGM2MjciLCJiYW5qdW1wIjoiIn0%3D'
            splinter2(browser)

    firefoxProfile = webdriver.FirefoxProfile()
    tempDir = os.getcwd()
    tempDir = os.path.split(tempDir)[0]
    firebugPlugFile = os.path.join(r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\82bh7hqw.default\extensions", "cehomepage@mozillaonline.com")
    firefoxProfile.add_extension(firebugPlugFile)
    firefoxProfile.set_preference("extensions.firebug.currentVersion", "2.0.7")

    driver = webdriver.Firefox(firefox_profile=firefoxProfile)
    driver.get("https://api.weibo.com/oauth2/authorize?client_id=3054804248&redirect_uri=http%3A%2F%2Fwww.huajiao.com&response_type=code&state=eyJzb3VyY2UiOiJzaW5hIiwicmVkaXJlY3QiOiJodHRwOlwvXC93d3cuaHVhamlhby5jb21cLz9ocmQ0Nzk1IiwidXNlcl9yYW5kIjoiNDY5YWM3NDUzNWY2MjkwMDdhOTZiYjcyNDExMGM2MjciLCJiYW5qdW1wIjoiIn0%3D")

def splinterQQ(url):
    firefoxProfile = FirefoxProfile()
    firefoxProfile.set_preference('plugin.state.flash', '2')

    browser = webdriver.Firefox(firefoxProfile)

    time.sleep(1)

    browser.get(url)

    time.sleep(3)

    contents = browser.find_element_by_class_name("btn-login")
    if contents:
        contents.click()
        while True:
            try:
                contents2 = browser.find_element_by_class_name("qq")
                if contents2:
                    contents2.click()
                    break
            except Exception as err:
                time.sleep(3)
                break

        browser.get(
            'https://graph.qq.com/oauth/show?which=Login&display=pc&response_type=code&client_id=101289788&redirect_uri=http%3A%2F%2Fwww.huajiao.com%2Fapi%2Factive&state=eyJzb3VyY2UiOiJxcSIsInJlZGlyZWN0IjoiaHR0cDpcL1wvd3d3Lmh1YWppYW8uY29tXC8/aHJkMzY3NCIsInVzZXJfcmFuZCI6ImYzN2U0N2EzMjIxMDJhY2RiYTM1MTk2YjY0ODhlYjA4IiwiYmFuanVtcCI6IiJ9')
        time.sleep(3)

        while True:
            try:
                print 'try new 1'
                contents3 = browser.find_element_by_id("switcher_plogin")
                print 'try new 2'
                if contents3:
                    print 'try new 3'
                    contents3.click()
                    break
            except Exception as err:
                print '!!!not found'
            time.sleep(1)


            #websize3 = 'https://api.weibo.com/oauth2/authorize?client_id=3054804248&redirect_uri=http%3A%2F%2Fwww.huajiao.com&response_type=code&state=eyJzb3VyY2UiOiJzaW5hIiwicmVkaXJlY3QiOiJodHRwOlwvXC93d3cuaHVhamlhby5jb21cLz9ocmQ0Nzk1IiwidXNlcl9yYW5kIjoiNDY5YWM3NDUzNWY2MjkwMDdhOTZiYjcyNDExMGM2MjciLCJiYW5qdW1wIjoiIn0%3D'
            #splinter2(browser)

def splinterOld(url):
    #start_firefox_with_firebug_plug()
    #while True:
    #    time.sleep(1000)

    #profileDir = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\82bh7hqw.default\extensions'
    #profile = webdriver.FirefoxProfile(profileDir)

    firefoxProfile = FirefoxProfile()
    #firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'true')
    firefoxProfile.set_preference('plugin.state.flash', '2')

    browser = webdriver.Firefox(firefoxProfile)

    #time.sleep(1)

    browser.get("https://api.weibo.com/oauth2/authorize?client_id=3054804248&redirect_uri=http%3A%2F%2Fwww.huajiao.com&response_type=code&state=eyJzb3VyY2UiOiJzaW5hIiwicmVkaXJlY3QiOiJodHRwOlwvXC93d3cuaHVhamlhby5jb21cLz9ocmQ0Nzk1IiwidXNlcl9yYW5kIjoiNDY5YWM3NDUzNWY2MjkwMDdhOTZiYjcyNDExMGM2MjciLCJiYW5qdW1wIjoiIn0%3D")

    #time.sleep(3)

    browser.find_element_by_id("userId").clear()
    browser.find_element_by_id("userId").send_keys("xiangyuzhenniao")
    browser.find_element_by_id("passwd").clear()
    browser.find_element_by_id('passwd').send_keys('ilovekorea')

    #browser.find_by_xpath('//*[@class="WB_btn_login formbtn_01"]/a').first.click()

    for i in range(0, 5):
        contents = browser.find_element_by_class_name("WB_btn_login")
        if contents:
            contents.click()

if __name__ == '__main__':
    websize3 = 'http://www.huajiao.com/'
    #splinterWeibo(websize3)
    splinterQQ(websize3)
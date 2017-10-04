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


def splinter(url):
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
    websize3 = 'https://api.weibo.com/oauth2/authorize?client_id=3054804248&redirect_uri=http%3A%2F%2Fwww.huajiao.com&response_type=code&state=eyJzb3VyY2UiOiJzaW5hIiwicmVkaXJlY3QiOiJodHRwOlwvXC93d3cuaHVhamlhby5jb21cLz9ocmQ0Nzk1IiwidXNlcl9yYW5kIjoiNDY5YWM3NDUzNWY2MjkwMDdhOTZiYjcyNDExMGM2MjciLCJiYW5qdW1wIjoiIn0%3D'
    splinter(websize3)
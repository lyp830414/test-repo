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
    browser.find_element_by_id("userId").send_keys("your name")
    browser.find_element_by_id("passwd").clear()
    browser.find_element_by_id('passwd').send_keys('your password')

    contents = browser.find_element_by_class_name("WB_btn_login")
    if contents:
        contents.click()

def splinter(url):

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

if __name__ == '__main__':
    websize3 = 'http://www.huajiao.com/'
    splinter(websize3)
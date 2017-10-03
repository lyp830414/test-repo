#coding=utf-8
import time
from splinter.browser import Browser


def splinter(url):
    browser = Browser()
    #login 126 email websize
    browser.visit(url)
    #wait web element loading
    time.sleep(3)
    #fill in account and password
    browser.find_by_id('userId').fill('your name')
    browser.find_by_id('passwd').fill('your pwd')
    #browser.find_by_xpath('//*[@class="WB_btn_login formbtn_01"]/a').first.click()

    contents = browser.find_by_xpath('//*[@class="WB_btn_login formbtn_01"]')
    print len(contents)

    for content in contents:
        print content.value

    ll = len(browser.find_by_xpath('//*[@class="WB_btn_login formbtn_01"]'))
    print 'len for ll is %d' %ll



    for j in range(ll+5):
        print j
        obj = browser.find_by_xpath('//*[@class="WB_btn_login formbtn_01"]')
        print obj

        if obj:
            obj.click()
        else:
            obj = browser.find_by_xpath('//*[@class="WB_btn_oauth formbtn_01"]')
            if obj:
                obj.click()

        time.sleep(3)

        if (len(browser.windows) > 1):
            print 'ok!'
            while(True):
                time.sleep(1000)
            browser.windows[1].close()

    time.sleep(10)
    #close the window of brower
    browser.quit()

if __name__ == '__main__':
    websize3 = 'https://api.weibo.com/oauth2/authorize?client_id=3054804248&redirect_uri=http%3A%2F%2Fwww.huajiao.com&response_type=code&state=eyJzb3VyY2UiOiJzaW5hIiwicmVkaXJlY3QiOiJodHRwOlwvXC93d3cuaHVhamlhby5jb21cLz9ocmQ0Nzk1IiwidXNlcl9yYW5kIjoiNDY5YWM3NDUzNWY2MjkwMDdhOTZiYjcyNDExMGM2MjciLCJiYW5qdW1wIjoiIn0%3D'
    splinter(websize3)
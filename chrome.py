# coding:utf-8

import time
from splinter import Browser

def splinter(url):
    browser = Browser()
    browser.visit(url)
    time.sleep(5)

    #browser.find_by_id('idInput').fill('******')
    #browser.find_by_id('pwdInput').fill('******')
    #browser.find_by_id('loginBtn').click()
    #time.sleep(8)
    browser.quit()

if __name__ == '__main__':
    websize3 = 'https://drive.google.com/get_video_info?docid=0B0VS8-zQCcJmNVU1QWdjam02RWs'
    splinter(websize3)
# coding:utf-8

import time
from splinter import Browser
import os

from splinter.request_handler.status_code import HttpResponseError


def splinter(url):
    browser = Browser('chrome')
    try:
        browser.visit(url)
        if browser.status_code.is_success():
            print 'success', browser.status_code.code
    except Exception, e:
        print e
    #print browser.html
    browser.quit()

if __name__ == '__main__':
    url = 'https://drive.google.com/get_video_info?docid=0B0VS8-zQCcJmSEtFU201VTFZQU0'
    #url = 'http://baidu.com'
    splinter(url)

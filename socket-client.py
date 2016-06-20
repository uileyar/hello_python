#!/usr/bin/env python
# coding:utf-8

import socket  # socket模块
import time
from util import *

HOST = '0.0.0.0'
PORT = 8888


def main1():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型，网络通信，TCP
    s.connect((HOST, PORT))  # 要连接的IP与端口
    while True:
        cmd = raw_input("Please input cmd:")  # 与人交互，输入命令
        s.sendall(cmd)  # 把命令发送给对端
        data = s.recv(1024)  # 把接收的数据定义为变量
        print data  # 输出变量
    s.close()  # 关闭连接

def main():
    try:
        connFd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        connFd.connect((HOST, PORT))
        logging.info("connect to network server success")
    except socket.error, msg:
        logging.error(msg)

    for i in range(1, 11):
        data = "The Number is %d" % i
        if connFd.send(data) != len(data):
            logging.error("send data to network server failed")
            break
        readData = connFd.recv(1024)
        print readData
        time.sleep(1)

    connFd.close()
if __name__ == '__main__':
    main()

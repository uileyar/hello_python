#!/usr/bin/env python
# coding:utf-8

import socket  # socket模块
from util import *

HOST = '0.0.0.0'
PORT = 8888


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型，网络通信，TCP
    s.connect((HOST, PORT))  # 要连接的IP与端口
    while True:
        cmd = raw_input("Please input cmd:")  # 与人交互，输入命令
        s.sendall(cmd)  # 把命令发送给对端
        data = s.recv(1024)  # 把接收的数据定义为变量
        print data  # 输出变量
    s.close()  # 关闭连接


if __name__ == '__main__':
    main()

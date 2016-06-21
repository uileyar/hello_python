#!/usr/bin/env python
# coding:utf-8

import socket  # socket模块
import select, errno
import commands  # 执行系统命令模块
from util import *

HOST = '0.0.0.0'
PORT = 8888


def main1():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型，网络通信，TCP
    s.bind((HOST, PORT))  # 套接字绑定的IP与端口
    s.listen(1)  # 开始TCP监听
    while True:
        conn, addr = s.accept()  # 接受TCP连接，并返回新的套接字与IP地址
        print'Connected by', addr  # 输出客户端的IP地址
        while True:
            data = conn.recv(1024)  # 把接收的数据实例化
            cmd_status, cmd_result = commands.getstatusoutput(data)  # commands.getstatusoutput执行系统命令（即shell命令），返回两个结果，第一个是状态，成功则为0，第二个是执行成功或失败的输出信息
            if len(cmd_result.strip()) == 0:  # 如果输出结果长度为0，则告诉客户端完成。此用法针对于创建文件或目录，创建成功不会有输出信息
                conn.sendall('Done.')
            else:
                conn.sendall(cmd_result)  # 否则就把结果发给对端（即客户端）
        conn.close()  # 关闭连接


def main():
    try:
        listen_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        listen_fd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_fd.bind((HOST, PORT))
        listen_fd.listen(10)
        epoll_fd = select.epoll()
        epoll_fd.register(listen_fd.fileno(), select.EPOLLIN)
    except socket.error, msg:
        logging.error("msg=%s", msg)
        return

    connections = {}
    addresses = {}
    datalist = {}
    while True:
        epoll_list = epoll_fd.poll()
        for fd, events in epoll_list:
            if fd == listen_fd.fileno():
                conn, addr = listen_fd.accept()
                logging.info("accept connection from %s, %d, fd = %d" % (addr[0], addr[1], conn.fileno()))
                conn.setblocking(0)
                epoll_fd.register(conn.fileno(), select.EPOLLIN | select.EPOLLET)
                connections[conn.fileno()] = conn
                addresses[conn.fileno()] = addr
            elif select.EPOLLIN & events:
                datas = ''
                while True:
                    try:
                        data = connections[fd].recv(1024)
                        if not data and not datas:
                            epoll_fd.unregister(fd)
                            connections[fd].close()
                            logging.info("%s, %d closed" % (addresses[fd][0], addresses[fd][1]))
                            break
                        else:
                            datas += data
                    except socket.error, msg:
                        if msg.errno == errno.EAGAIN:
                            logging.info("%s receive %s" % (fd, datas))
                            datalist[fd] = datas
                            epoll_fd.modify(fd, select.EPOLLET | select.EPOLLOUT)
                            break
                        else:
                            epoll_fd.unregister(fd)
                            connections[fd].close()
                            logging.error(msg)
                            break
            elif select.EPOLLHUP & events:
                epoll_fd.unregister(fd)
                connections[fd].close()
                logging.info("%s, %d closed" % (addresses[fd][0], addresses[fd][1]))
            elif select.EPOLLOUT & events:
                sendLen = 0
                logging.info("cmd: %s" % datalist[fd])
                cmd_status, cmd_result = commands.getstatusoutput(datalist[fd])  # commands.getstatusoutput执行系统命令（即shell命令），返回两个结果，第一个是状态，成功则为0，第二个是执行成功或失败的输出信息
                if len(cmd_result.strip()) == 0:  # 如果输出结果长度为0，则告诉客户端完成。此用法针对于创建文件或目录，创建成功不会有输出信息
                    connections[fd].sendall('Done.')
                else:
                    #connections[fd].sendall(cmd_result)  # 否则就把结果发给对端（即客户端）
                    while True:
                        sendLen += connections[fd].send(cmd_result[sendLen:])
                        if sendLen == len(cmd_result):
                            break
                epoll_fd.modify(fd, select.EPOLLIN | select.EPOLLET)
            else:
                continue


if __name__ == '__main__':
    logging.config.fileConfig(os.path.join(os.path.dirname(__file__), './config/logging.ini'))
    main()

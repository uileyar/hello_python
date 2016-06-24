
#!/usr/bin/env python
# coding:utf-8

import pcap
import dpkt

def main():
    pc = pcap.pcap()                # 注，参数可为网卡名，如eth0
    pc.setfilter('tcp port 80')     # 设置监听过滤器
    for ptime, pdata in pc:         # ptime为收到时间，pdata为收到数据
        print ptime, pdata          # ...
        #对抓到的以太网V2数据包(raw packet)进行解包
        p = dpkt.ethernet.Ethernet(pdata)
        if p.data.__class__.__name__ == 'IP':
            ip = '%d.%d.%d.%d' % tuple(map(ord, list(p.data.dst)))
            if p.data.data.__class__.__name__ == 'TCP':
                if data.dport == 80:
                    print p.data.data.data  # by gashero

    #一些显示参数
    nrecv, ndrop, nifdrop = pc.stats()  #返回的元组中，第一个参数为接收到的数据包，(by gashero)第二个参数为被核心丢弃的数据包。

if __name__ == "__main__":
  main()

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import paramiko
import ConfigParser
from socket import *
import socket
class SSH(object):        
    def SSH2Test(self):
        ip = "10.95.41.15"
        cmd = ['pwd','echo hello!']#你要执行的命令列表
        username = "root"  #用户名
        passwd = "www.360.cn"    #密码
        ret = True
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip,22,username,passwd,timeout=120)
            ssh.exec_command("pwd")
            ssh.close()
            print 'SSH connect %s\tOK\n'%(ip)
            return ret
        except :
            print '%s\tError\n'%(ip)
            return False
        return
    def SendMessageForFeiq(self):
        def run(ip):
            s = socket.socket(AF_INET,SOCK_DGRAM)
            add = (ip,2425)
            a = u"1:525:杨曙光:杨曙光:32:我是王宝强，我无敌!"
            s.sendto(a.encode("gbk"),add)
            s.close()
            print u'(未知协议) socket OK'
            return True

        cf = ConfigParser.ConfigParser()
        cf.read("conf/endpoint.ini")
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
        opts_feiq = cf.options("feiq")
        kvs_feiq = cf.items("feiq")

        for opts in opts_feiq:
            value = cf.get("feiq", opts)
            run(value)
        return True
    def SendMessageForFeiqTCP(self):
        def run(ip):
            s = socket.socket(AF_INET,SOCK_STREAM)
            s.connect((ip, 2425))
            a = u"1:525:杨曙光:杨曙光:32:我是王宝强，我无敌!"
            s.send(a.encode("gbk"))
            s.close()
            print u'(未知协议) socket OK'
            return True

        cf = ConfigParser.ConfigParser()
        cf.read("conf/endpoint.ini")
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
        opts_feiq = cf.options("feiq")
        kvs_feiq = cf.items("feiq")

        for opts in opts_feiq:
            value = cf.get("feiq", opts)
            run(value)
        return True

if __name__=='__main__':
    t = SSH()
    t.SendMessageForFeiqTCP()
# -*- coding: utf-8 -*- 

import telnetlib
import ConfigParser
from socket import *
from edlp import control
import socket
import os
import ConfigParser
import time



class Telnet:

    def TelnetTest(self):
        # 配置选项
        Host = '10.95.41.18' # Telnet服务器IP
        username = 'administrator'   # 登录用户名
        password = 'www.360.cn'  # 登录密码
        finish = ':~$ '      # 命令提示符（标识着上一条命令已执行完毕）
 
        # 连接Telnet服务器
        tn = telnetlib.Telnet(Host)
 
        # 输入登录用户名
        tn.read_until('login: ')
        tn.write(username + '\n')
 
        # 输入登录密码
        tn.read_until('Password: ')
        tn.write(password + '\n')
 
        # 登录完毕后，执行ls命令
        tn.read_until(finish)
        tn.write('ls\n')
        #tn.write('王宝强\n')
        #tn.write('王宝强\n')
        #tn.write('王宝强\n')
 
        # ls命令执行完毕后，终止Telnet连接（或输入exit退出）
        tn.read_until(finish)
        tn.close() # tn.write('exit\n')
    def TelnetTestFile(self):
        def run(ip):

            #print tn.read_until("n")
            #fp = r"file\SN.txt"
            files = FromDirGetFile()
            for fp in files:
                time.sleep(3)
                tn = telnetlib.Telnet()
                tn.open(ip, 2425)
                f = open(fp,"r")
                time.sleep(1)
                f_body = f.read()
                time.sleep(1)
                tn.write(f_body)
                tn.write("n")
                f.close()
                tn.close()
                print fp + u'---(未知协议) Telnet OK'
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
def FromDirGetFile():
    c = control()
    vol = c.GetVol()
    dir = vol + r":\DLP\file\telnet"
    L = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            value = os.path.join(root,file)
            L.insert(1,value)
        return L

if __name__ == "__main__":
    t = Telnet()
    t.TelnetTestFile()
    #FromDirGetFile()
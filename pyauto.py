#!/usr/bin/python
# -*- coding: UTF-8 -*-

from multiprocessing.dummy import Pool
import multiprocessing
import ConfigParser
import time
from edlp import control
from check import check
from https import HTTPSControl
from SSH import *
from telnet import Telnet
from smtp import *
from outlook import defOutlook
import socket
import getopt
import os
import shutil

class pyauto:

    def hello(self):
        print('hello')
    def h0(self):
        ret = True
        http = control()
        ret = http.get_http()
        localtime = time.asctime( time.localtime(time.time()) )
        print localtime
        if ret:
            print "http get OK"
        else:
            print "http get FAIL"
    def h1(self):
        ret = True
        http = control()
        ret = http.post_http_content()
        localtime = time.asctime( time.localtime(time.time()) )
        print localtime
        if ret:
            print "http upload OK"
        else:
            print "http upload FAIL"

    def hh1(self,ip,port,vol):
        filename = "%s:\\DLP\\file\\SN.txt" % vol
        ret = True
        http = control()
        ret = http.whitelist_post_http_file_pyauto(ip,port,filename)
        localtime = time.asctime( time.localtime(time.time()) )
        print localtime
        if ret:
            print "http upload file OK"
        else:
            print "http upload file FAIL"

    def hh1check(self):
        ip = "10.95.41.18"
        port = "8001"
        c = control()
        app = pyauto()
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)

        vol = c.GetVol()
        app.hh1(ip,port,vol)
        print '10.95.41.18'

    def h11(self,ip,port,vol):
        ret = True
        filename = "%s:\\DLP\\file\\SN.txt" % vol
        http = control()
        ret = http.post_http_file(ip,port,filename)
        localtime = time.asctime( time.localtime(time.time()) )
        print localtime
        if ret:
            return ret
        else:
            return False

    def h11check(self):
        ip = "10.95.41.15"
        port = "8000"
        c = control()
        app = pyauto()
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)

        vol = c.GetVol()
        app.h11(ip,port,vol)
        print '10.95.41.15'


    def h2(self):

        ret = True
        https = HTTPSControl()
        ret = https.https()
        if ret:
            print "https upload OK"
        else:
            print " https upload FAIL"

    def h22(self,vol):
        ret = True
        filename = "%s:\\DLP\\file\\SN.txt" % vol
        https = HTTPSControl()
        ret = https.post_https_file(r'%s'%filename)
        if ret:
            print "https upload file OK"
        else:
            print "https upload file FAIL"

    def h22check(self):
        c = control()
        app = pyauto()
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
        vol = c.GetVol()
        app.h22(vol)

    def h3(self,vol):
        ret = True
        ftp = control()
        ret = ftp.ftp_up_pyauto(vol)
        if ret:
            print "ftp upload OK"       
        else:
            print "ftp upload FAIL"

    def h3check(self):
        c = control()
        app = pyauto()
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
        vol = c.GetVol()
        app.h3(vol)
        
    def h4(self):
        ret = True
        #s = control()
        #ret = s.smtp('dlptest1','dlptest2',"wangbaoqiang王宝强","wangbaoqiang王宝强")
        s = SMTP()
        ret = s.SMTPTest()
        if ret:
            print(u"(不带附件的邮件测试)SMTP OK ")
        else:
            print(u" (不带附件的邮件测试)SMTP FAIL")
    
    def h44(self,vol):
        ret = True
        #s = control()
        #ret = s.smtp('dlptest1','dlptest2',"wangbaoqiang王宝强","wangbaoqiang王宝强")
        s = SMTP()
        ret = s.SmtpAttach_pyauto(vol)
        if ret:
            print(u"(带附件的邮件测试)SMTPATTACH OK")
        else:
            print(u"(带附件的邮件测试)SMTPATTACH FAIL")

    def h44check(self):
        c = control()
        app = pyauto()
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
        vol = c.GetVol()
        app.h44(vol)
           
    def h5(self,vol):
        ret = True
        ftp = control()
        ret = ftp.udriver_pyauto(vol)
        if ret:
            print(u"(U盘)udriver OK ")
        else:
            print(u"(U盘)udriver FAIL")
    def h5check(self):
        c = control()
        app = pyauto()
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
        vol = c.GetVol()
        app.h5(vol)
        
    def h6(self,vol):
        ret = True
        ftp = control()
        ret = ftp.netshare_pyauto(vol,2)
        if ret:
            print(u"(共享方式外发关键字文件)netshare OK")
        else:
            print(u"(共享方式外发关键字文件)netshare FAIL")

    def h6check(self):
        c = control()
        app = pyauto()
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
        vol = c.GetVol()
        app.h6(vol)
          
    def h7(self,vol):
        ret = True
        pr = control()
        ret = pr.bluetooth_pyauto(vol)
        if ret:
            print(u"(蓝牙)bluetooth file OK")
        else:
            print(u"(蓝牙)bluetooth file FAIL")
    def h7check(self):
        c = control()
        app = pyauto()
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
        vol = c.GetVol()
        app.h7(vol)
    
    def h8(self,vol):
        ret = True
        pr = control()
        ret = pr.printer_pyauto(vol)
        if ret:
            print(u"(打印)print file OK")     
        else:
            print(u"(打印)print file FAIL")
    def h8check(self):
        c = control()
        app = pyauto()
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
        vol = c.GetVol()
        app.h8(vol)
            
    def e3(self,vol):
        ret = True
        pr = control()
        ret = pr.clipboard_pyauto(vol)
        if ret:
            print(u"(剪切板)clipboard OK")
        else:
            print(u"(剪切板)clipboard FAIL")
    def e3check(self):
        c = control()
        app = pyauto()
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
        vol = c.GetVol()
        app.e3(vol)      
    
    def e4(self):
        ret = True
        hostname = socket.gethostname()
        out = defOutlook()
        if hostname == 'DESKTOP-CHQS1KQ':
            ret = out.outlook()
            if ret:
                print "OUTLOOK OK"
               
            else:
                print "OUTLOOK FAIL"
        
        else:
            print "OUTLOOK FAIL"
           
    
    def e6(self):
        ret = True
        s = SSH()
        ret = s.SSH2Test()
        if ret:
            print "SSH OK"
          
        else:
            print "SSH FAIL"
      
    def n1(self,vol):
        ret = True
        o = control()
        ret = o.netshare_pyauto(vol,3)
        if ret:
            print(u"(受限文件测试)netshare OK")
           
        else:
            print(u"(受限文件测试)netshare FAIL")
    def n1check(self):
        c = control()
        app = pyauto()
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
        vol = c.GetVol()
        app.n1(vol)
        
    def n2(self,vol):
        ret = True
        o = control()
        ret = o.netshare_pyauto(vol,4)
        if ret:
            print(u"(文件名+文件内容测试)netshare OK")
        else:
            print(u"(文件名+文件内容测试)netshare FAIL")
    def n2check(self):
        c = control()
        app = pyauto()
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
        vol = c.GetVol()
        app.n2(vol)
        
    def n3(self,vol):
        ret = True
        o = control()
        ret = o.netshare_pyauto(vol,5)
        if ret:
            print(u"(共享方式测试上传证据文件)netshare OK")
        else:
            print(u"(共享方式测试上传证据文件)netshare FAIL")
    def n3check(self):
        c = control()
        app = pyauto()
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
        vol = c.GetVol()
        app.n3(vol)
           
    def n4(self,vol):
        ret = True
        o = control()
        ret = o.netshare_pyauto(vol,6)
        if ret:
            print(u"(共享方式测试上传5层嵌套文件)netshare OK")
        else:
            print(u"(共享方式测试上传5层嵌套文件)netshare FAIL")
    def n4check(self):
        c = control()
        app = pyauto()
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
        vol = c.GetVol()
        app.n4(vol)
            
    def n5(self,vol):
        ret = True
        o = control()
        ret = o.netshare_pyauto(vol,7)
        if ret:
            print(u"(共享方式测试上传10层嵌套文件)netshare OK")
        else:
            print(u"(共享方式测试上传10层嵌套文件)netshare FAIL")
    def n5check(self):
        c = control()
        app = pyauto()
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
        vol = c.GetVol()
        app.n5(vol)
     
    def n6(self,vol):
        ret = True
        o = control()
        ret = o.netshare_pyauto(vol,8)
        if ret:
            print(u"(共享方式测试备注/脚注/批注/页眉/页脚/正文文件)netshare OK")
        else:
            print(u"(共享方式测试备注、脚注、批注、页眉、页脚、正文文件)netshare FAIL")
    def n6check(self):
        c = control()
        app = pyauto()
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
        vol = c.GetVol()
        app.n6(vol)
          
    def n7(self,vol):
        ret = True
        o = control()
        ret = o.netshare_pyauto(vol,9)
        if ret:
            print(u"(共享方式测试篡改后缀名的文件)netshare OK")
        else:
            print(u"(共享方式测试篡改后缀名的文件)netshare FAIL")
    def n7check(self):
        c = control()
        app = pyauto()
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
        vol = c.GetVol()
        app.n7(vol)
         
    def o1(self,vol):
        ret = True
        o = control()
        ret = o.netshare_pyauto(vol,1)
        if ret:
            print(u"(OCR测试)netshare OK")
        else:
            print(u"(OCR测试)netshare FAIL")
    def o1check(self):
        c = control()
        app = pyauto()
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
        vol = c.GetVol()
        app.o1(vol)
          
    def a1(self,vol):
        ret = True
        a = control()
        ret = a.feiq_pyauto(vol)
        if ret:
            print "FeiQ OK"
        else:
            print "FeiQ FAIL"
    def a1check(self):
        c = control()
        app = pyauto()
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
        vol = c.GetVol()
        app.a1(vol)
          
    def w1(self,ip,port,vol):
        ret = True
        w = control()
        filename = "%s:\\DLP\\file\\SN.txt" % vol
        ret = w.whitelist_post_http_file_pyauto(ip,port,filename)
        if ret:
            print(u"URL白名单 OK")
        else:
            print(u"URL白名单 FAIL")

    def w1check(self):
        c = control()
        app = pyauto()
        ip = "10.95.41.18"
        port = "8001"
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
        vol = c.GetVol()
        app.w1(ip,port,vol)
    
    def w2(self,ip,port,vol):
        ret = True
        w = control()
        filename = "%s:\\DLP\\file\\SN.txt" % vol
        ret = w.whitelist_post_http_file_pyauto(ip,port,filename)
        if ret:
            print(u"IP白名单 OK")
        else:
            print(u"IP白名单 FAIL")

    def w2check(self):
        c = control()
        app = pyauto()
        ip = "10.95.27.119"
        port = "8001"
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
        vol = c.GetVol()
        app.w2(ip,port,vol)
     
    def w3(self,vol):
        ret = True
        w = SMTP()
        ret = w.WhitelistSmtpAttach_pyauto(vol)
        if ret:
            print(u"EMAIL白单 OK")
          
        else:
            print(u"EMAIL白名单 FAIL")

    def w3check(self):
        c = control()
        app = pyauto()
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
        vol = c.GetVol()
        app.w3(vol)

    def netall(self,vol):
        ret = True
        source_files = "%s:\\DLP\\file\\pyauto" % vol
        target_files = "Z:\\"
        o = control()
        os.system(r'net use \\10.95.27.99\IPC$ /del /y 2>nul')
        os.system(r'net use \\10.95.27.99\wuhq\Test /del /y 2>nul')
        time.sleep(10)
        ret = o.PyautoCopyFile(vol,source_files,target_files)
        if ret:
            print(u"netall OK")
        else:
            print(u"netall FAIL")
    def netallcheck(self):
        c = control()
        app = pyauto()
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
        vol = c.GetVol()
        app.netall(vol)
        
    def OutputFile(self,vola,volb):
        ret = True
        source_files = "%s:\\DLP\\file\\pyauto" % vola
        target_files = "%s:\\Test" % volb
        o = control()
        time.sleep(2)
        ret = o.copyFiles(source_files,target_files)
        if ret:
            print(u"output file OK")
        else:
            print(u"output file FAIL")
    def OutputFileCheck(self):
        c = control()
        app = pyauto()
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
        if ipaddr == '10.95.27.116':
            vol = c.GetVol()
            app.OutputFile(vol,"G")

    def OutputFileForMenu(self):
        c = control()
        def OutputFileX(vola,volb):
            source_files = "%s:\\DLP\\file\\dlp.txt" % vola
            target_files = "%s:\\Test" % volb
            o = control()
            time.sleep(2)
            shutil.copy(source_files,target_files)
            print(u"output file OK")

        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
        if ipaddr == '10.95.27.116':
            vol = c.GetVol()
            OutputFileX(vol,"G")
        else:
            return False
        return True
        
    def all(self):
        app = pyauto()
        c = control()
        s = SSH()
        https = HTTPSControl()
        t = Telnet()
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
        app.h0()
        time.sleep(5)
        app.h1()
        time.sleep(5)
        app.h11check()
        time.sleep(5)
        app.h2()
        time.sleep(5)
        app.h22check()
        time.sleep(5)
        app.h3check()
        time.sleep(5)
        c.sftp_up()
        time.sleep(5)
        app.h44check()
        time.sleep(5)
        if ipaddr == '172.24.83.44':
            app.h5check()
            time.sleep(5)
        if ipaddr == '172.24.83.44':
            app.h7check()
            time.sleep(5)
        app.h8check()
        time.sleep(5)
        s.SendMessageForFeiqTCP()
        time.sleep(5)
        t.TelnetTestFile()
        time.sleep(5)
        app.e3check()
        time.sleep(5)
        if ipaddr == '10.95.27.116':
            app.e4()
            time.sleep(5)
        https.httpsSLL()
        time.sleep(5)
        app.e6()
        time.sleep(5)
        '''
        app.h6check()
        time.sleep(5)
        app.h6check()#因为测试过程中发现第一次没有执行，所以再重新执行一次，这里不是手误写错了
        time.sleep(5)
        app.n1check()
        time.sleep(5)
        app.n2check()
        time.sleep(5)
        app.n3check()
        time.sleep(5)
        app.n4check()
        time.sleep(5)
        app.n5check()
        time.sleep(5)
        app.n6check()
        time.sleep(5)
        app.n7check()
        time.sleep(5)
        app.o1check()
        time.sleep(5)
        '''
        app.netallcheck()
        time.sleep(30)
        app.OutputFileCheck()
        time.sleep(5)
        app.w1check()
        time.sleep(5)
        app.w2check()
        time.sleep(5)
        app.w3check()
        time.sleep(5)
        c.window_capture()
        time.sleep(5)
    def LoopAll(self):
        l = pyauto()
        while 1:
            l.all()
            time.sleep(30)
    def grantAll(self):
        ret = True
        g = control()
        ret = g.Grant(1)
        if ret:
            print "grantAll OK"    
        else:
            print "grantAll FAIL"
           
    def grantAllDis(self):
        ret = True
        g = control()
        ret = g.Grant(2)
        if ret:
            print "grantAllDis OK"
        else:
            print "grantAllDis FAIL"
            
    def grantDisPrint(self):
        ret = True
        g = control()
        ret = g.Grant(3)
        if ret:
            print "grantDisPrint OK"
        else:
            print "grantDisPrint FAIL"
          
    def grantReAuth(self):
        ret = True
        g = control()
        ret = g.Grant(4)
        if ret:
           print "grantReAuth OK"
        else:
            print "grantReAuth FAIL"
           
    def grantDisPrintScn(self):
        ret = True
        g = control()
        ret = g.Grant(5)
        if ret:
            print "grantDisPrintScn OK"
        else:
            print "grantDisPrintScn FAIL"
    
    def grantDisCopy(self):
        ret = True
        g = control()
        ret = g.Grant(6)
        if ret:
           print "grantDisCopy OK"
        else:
            print "grantDisCopy FAIL"
    
    def grantDisOfflineUse(self):
        ret = True
        g = control()
        ret = g.Grant(7)
        if ret:
            print "grantDisOfflineUse OK"
        else:
           print "grantDisOfflineUse FAIL"
    
    def EncryptFile(self):
        ret = True
        enc = control()
        ret = enc.EncryptFile()
        if ret:
            print "EncryptFile OK"
        else:
            print "EncryptFile FAIl"
    
    def SortLevel(self):
        ret = True
        sort = control()
        ret = sort.SortLevel()
        if ret:
            print "SortLevel OK"
        else:
            print "SortLevel FAIL"



#end--------------------------------------------------------
if __name__ == "__main__":
    app = pyauto()
    def usage():
        print(u'\
        -h or --help：显示帮助信息\n\
        -t ：运行全量测试\n\
        -p ：运行打印测试\n\
        -c ：运行拷贝文件到共享目录测试\n\
        -l ：死循环运行全量测试\n\
        -v or --version：显示版本\
        ')
    if len(sys.argv) == 1:
        usage()
        sys.exit()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "htpclTv", ["help", "output="])
    except getopt.GetoptError:
        usage()        

    for cmd, arg in opts:
        if cmd in ("-h", "--help"):
            usage()
        elif cmd in ("-t", "1"):
            app.all() 
        elif cmd in ("-p", "1"):
            app.h8check()
        elif cmd in ("-c", "1"):
            app.netallcheck()
        elif cmd in ("-l", "1"):
            app.LoopAll()
        elif cmd in ("-T", "1"):
            app.hh1check()
        elif cmd in ("-v", "--version"):
            print("version 1.0")
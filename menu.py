#!/usr/bin/python
# -*- coding: UTF-8 -*-

import multiprocessing
import time
import signal
import errno
from edlp import control
from check import staf
from https import HTTPSControl
from Tkinter import *
from SSH import *
from smtp import *
from outlook import defOutlook
from office import office
from Windows import Window
from telnet import Telnet
from pyauto import pyauto
import WinAction
import socket
import os
import _winreg

#__author__ = 'luoxianghui'

root = Tk()
#设置标题
root.title("EDLP自动化测试")
#设置窗口的大小宽x高+偏移量
root.geometry('800x600+500+200')
#禁止调整窗口大小
root.resizable(0, 0)
#增加滚动条
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
t = Listbox(root, width=800, height=600, borderwidth=2, font = ('Arial',12), bd = 15, fg='#0000FF', yscrollcommand=scrollbar.set)
t.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=t.yview)
#关闭窗口
def kill():
    k = control()
    root.destroy()
    k.killpython()

root.protocol('WM_DELETE_WINDOW',kill)

#设置窗口图标
root.iconbitmap('img\mainlogo.ico')
#t = Text(root, height=600, width=800)

'''
定义command
'''
#start----------------------------------------------------

def hello():
    t.insert(END,"| 测试 |\n")
    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
    t.update()
    #print('hello')
def wait_child(signum, frame):
    print 'receive SIGINT'
    try:
        while True:
            # -1 表示任意子进程
            # os.WNOHANG 表示如果没有可用的需要 wait 退出状态的子进程，立即返回不阻塞
            cpid, status = os.waitpid(-1, os.WNOHANG)
            if cpid == 0:
                print 'no child process was immediately available'
                break
            exitcode = status >> 8
            print 'child process %s exit with exitcode %s', cpid, exitcode
    except OSError as e:
        if e.errno == errno.ECHILD:
            print 'current process has no existing unwaited-for child processes.'
        else:
            raise
    print 'handle SIGINT end'

def h0():
    ret = True
    http = control()
    ret = http.get_http()
    if ret:
        t.insert(END,"| http get OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| http get FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def h1():
    ret = True
    http = control()
    ret = http.post_http_content()
    if ret:
        t.insert(END,"| http upload OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| http upload FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def h1Pass():
    c = control()
    try:
        #c.post_http_content_pass()
        os.system("start cmd /c edlp.py -1")
    except Exception,e:
        t.insert(END,"| UserConformPass FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    finally:
        t.insert(END,"| UserConformPass OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def h1Refuse():
    c = control()
    try:
        #c.post_http_content_pass()
        os.system("start cmd /c edlp.py -2")
    except Exception,e:
        t.insert(END,"| UserConformRefuse FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    finally:
        t.insert(END,"| UserConformRefuse OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def h11():
    ret = True
    filename = "file\SN.txt"
    ip = "10.95.41.15"
    port = "8000"
    http = control()
    ret = http.post_http_file(ip,port,filename)
    if ret:
        t.insert(END,"| http upload file OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| http upload file FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def h11Pass():
    c = control()
    try:
        #c.post_http_content_pass()
        os.system("start cmd /c edlp.py -3")
    except Exception,e:
        t.insert(END,"| UserConformPass FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    finally:
        t.insert(END,"| UserConformPass OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def h11Refuse():
    c = control()
    try:
        #c.post_http_content_pass()
        os.system("start cmd /c edlp.py -4")
    except Exception,e:
        t.insert(END,"| UserConformRefuse FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    finally:
        t.insert(END,"| UserConformRefuse OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def h2():
    ret = True
    https = HTTPSControl()
    ret = https.https()
    if ret:
        t.insert(END,"| https upload OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| https upload FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def h22():
    ret = True
    filename = "file\SN.txt"
    https = HTTPSControl()
    ret = https.post_https_file(r'%s'%filename)
    if ret:
        t.insert(END,"| https upload file OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| https upload file FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def h3():
    ret = True
    ftp = control()
    ret = ftp.ftp_up()
    if ret:
        t.insert(END,"| ftp upload OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| ftp upload FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def h33():
    ret = True
    ftp = control()
    try:
        ftp.sftp_up()
    except Exception as e:
        t.insert(END,"| sftp upload FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    finally:
        t.insert(END,"| sftp upload OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def h4():
    ret = True
    #s = control()
    #ret = s.smtp('dlptest1','dlptest2',"wangbaoqiang王宝强","wangbaoqiang王宝强")
    s = SMTP()
    ret = s.SMTPTest()
    if ret:
        t.insert(END,"| (不带附件的邮件测试)SMTP OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| (不带附件的邮件测试)SMTP FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def h44():
    ret = True
    #s = control()
    #ret = s.smtp('dlptest1','dlptest2',"wangbaoqiang王宝强","wangbaoqiang王宝强")
    s = SMTP()
    ret = s.SmtpAttach()
    if ret:
        t.insert(END,"| (带附件的邮件测试)SMTPATTACH OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| (带附件的邮件测试)SMTPATTACH FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def h5():
    ret = True
    ftp = control()
    ret = ftp.udriver()
    if ret:
        t.insert(END,"| (U盘)udriver OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| (U盘)udriver FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def h55():
    ret = True
    py = pyauto()
    ret = py.OutputFileForMenu()
    if ret:
        t.insert(END,"| (外挂磁盘)OutputFile OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| (外挂磁盘)OutputFile FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def h6():
    ret = True
    ftp = control()
    ret = ftp.netshare(2)
    if ret:
        t.insert(END,"| (共享方式外发关键字文件)netshare OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| (共享方式外发关键字文件)netshare FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def h7():
    ret = True
    pr = control()
    ret = pr.bluetooth()
    if ret:
        t.insert(END,"| (蓝牙)bluetooth file OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| (蓝牙)bluetooth file FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def h8():
    ret = True
    s = 20
    o = office()
    o.CreateTxt(s)
    time.sleep(3)
    pr = control()
    ret = pr.printer()
    if ret:
        t.insert(END,"| (打印)print file OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| (打印)print file FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def h9():
    try:
        x = os.system("net use * /del /y")
        if x == 0:
            t.insert(END,"| (清除net use)net use OK |\n")
            t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
            t.update()
        else:
            t.insert(END,"| (清除net use)net use FAIL |\n")
            t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
            t.update()
    except Exception,e:
        t.insert(END,"| net use列表是空 |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def h10():
    try:
        os.system("Windows.py -8")
    except Exception as e:
        t.insert(END,"| CreateTelnetWindow FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    finally:
        t.insert(END,"| CreateTelnetWindow OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def e1():
    ret = True
    s = SSH()
    ret = s.SendMessageForFeiqTCP()
    if ret:
        t.insert(END,"| (未知协议)socket OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| (未知协议)socket FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def e11():
    ret = True
    s = Telnet()
    try:
        s.TelnetTestFile()
    except Exception as e:
        t.insert(END,"| (未知协议)Telnet FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    finally:
        t.insert(END,"| (未知协议)Telnet OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()     
def e3():
    ret = True
    pr = control()
    ret = pr.clipboard()
    if ret:
        t.insert(END,"| (剪切板)clipboard OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| (剪切板)clipboard FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def e4():
    ret = True
    hostname = socket.gethostname()
    out = defOutlook()
    if hostname == 'DESKTOP-CHQS1KQ':
        ret = out.outlook()
        if ret:
            t.insert(END,"| OUTLOOK OK |\n")
            t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
   
            t.update()
        else:
            t.insert(END,"| OUTLOOK FAIL |\n")
            t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
   
            t.update()
    else:
        t.insert(END,"| OUTLOOK FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def e5():
    ret = True
    https = HTTPSControl()
    ret = https.httpsSLL()
    if ret:
        t.insert(END,"| (双向)SSL OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| (双向)SLL FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def e6():
    ret = True
    s = SSH()
    ret = s.SSH2Test()
    if ret:
        t.insert(END,"| SSH OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| SSH FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def e7():
    #k = control()
    try:
        os.system("start cmd /k MultiUpload.py -k")
    except Exception as e:
        t.insert(END,"| 同一地址日志合并 FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    finally:
        signal.signal(signal.SIGINT, wait_child)
        t.insert(END,"| 同一地址日志合并 OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
        #k.killpython()
            
def e8():
    #k = control()
    try:
        os.system("start cmd /k MultiUpload.py -K")
    except Exception as e:
        t.insert(END,"| 不同地址日志合并 FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    finally:
        signal.signal(signal.SIGINT, wait_child)
        t.insert(END,"| 不同地址日志合并 OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
        #k.killpython()
            
def n1():
    ret = True
    o = control()
    ret = o.netshare(3)
    if ret:
        t.insert(END,"| (受限文件测试)netshare OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| (受限文件测试)netshare FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def n2():
    ret = True
    o = control()
    ret = o.netshare(4)
    if ret:
        t.insert(END,"| (文件名+文件内容测试)netshare OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| (文件名+文件内容测试)netshare FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def n3():
    ret = True
    o = control()
    ret = o.netshare(5)
    if ret:
        t.insert(END,"| (共享方式测试上传证据文件)netshare OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| (共享方式测试上传证据文件)netshare FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def n4():
    ret = True
    o = control()
    ret = o.netshare(6)
    if ret:
        t.insert(END,"| (共享方式测试上传5层嵌套文件)netshare OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| (共享方式测试上传5层嵌套文件)netshare FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def n5():
    ret = True
    o = control()
    ret = o.netshare(7)
    if ret:
        t.insert(END,"| (共享方式测试上传10层嵌套文件)netshare OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| (共享方式测试上传10层嵌套文件)netshare FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def n6():
    ret = True
    o = control()
    ret = o.netshare(8)
    if ret:
        t.insert(END,"| (共享方式测试备注/脚注/批注/页眉/页脚/正文文件)netshare OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| (共享方式测试备注、脚注、批注、页眉、页脚、正文文件)netshare FAIL |\n")
        t.update()
def n7():
    ret = True
    o = control()
    ret = o.netshare(9)
    if ret:
        t.insert(END,"| (共享方式测试篡改后缀名的文件)netshare OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| (共享方式测试篡改后缀名的文件)netshare FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def n9():
    try:
        os.system("Windows.py -2")
    except Exception as e:
        t.insert(END,"| CreateWordWindow FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    finally:
        t.insert(END,"| CreateWordWindow OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def n10():
    try:
        os.system("Windows.py -3")
    except Exception as e:
        t.insert(END,"| CreateExcelWindow FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    finally:
        t.insert(END,"| CreateExcelWindow OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def n11():
    try:
        os.system("Windows.py -4")
    except Exception as e:
        t.insert(END,"| CreatePptWindow FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    finally:
        t.insert(END,"| CreatePptWindow OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def n12():
    try:
        os.system("Windows.py -1")
    except Exception as e:
        t.insert(END,"| CreateTxtWindow FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    finally:
        t.insert(END,"| CreateTxtWindow OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def n13():
    try:
        os.system("Windows.py -5")
    except Exception as e:
        t.insert(END,"| CreateImageWindow FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    finally:
        t.insert(END,"| CreateImageWindow OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def n14():
    try:
        os.system("Windows.py -6")
    except Exception as e:
        t.insert(END,"| CreatePdfWindow FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    finally:
        t.insert(END,"| CreatePdfWindow OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def n15():
    try:
        os.system("Windows.py -7")
    except Exception as e:
        t.insert(END,"| CreateGenSizeWindow FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    finally:
        t.insert(END,"| CreateGenSizeWindow OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def o1():
    ret = True
    o = control()
    ret = o.netshare(1)
    if ret:
        t.insert(END,"| (OCR测试)netshare OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| (OCR测试)netshare FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def o2():
    ret = True
    o = control()
    ret = o.window_capture()
    if ret:
        t.insert(END,"| WindowCapture OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| WindowCapture FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def o3():
    ret = True
    o = control()
    ret = o.GenImage()
    if ret:
        t.insert(END,"| ImageGrabCapture OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| ImageGrabCapture FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def o4():
    ret = True
    o = control()
    ret = o.WechatCapture()
    if ret:
        t.insert(END,"| WechatCapture OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| WechatCapture FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def o5():
    ret = True
    o = control()
    ret = o.QQCapture()
    if ret:
        t.insert(END,"| QQCapture OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| QQCapture FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def m1():
    ret = True
    s = 20
    o = office()
    o.CreateTxt(s)
    time.sleep(3)
    c = control()
    ret = c.EncryptAction(1)
    #ret = os.system('start "" /d "D:\\DLP\\autoit" "D:\\DLP\\autoit\\EncryptAction.exe" 1')
    if ret:
        t.insert(END,"| (右键申请文件加白)EncryptAction OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| (右键申请文件加白)EncryptAction FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def m2():
    ret = True
    s = 20
    o = office()
    o.CreateTxt(s)
    time.sleep(3)
    c = control()
    ret = c.EncryptAction(2)
    #ret = os.system('start "" /d "D:\\DLP\\autoit" "D:\\DLP\\autoit\\EncryptAction.exe" 2')
    if ret:
        t.insert(END,"| (右键文件普通加密)EncryptAction OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| (右键文件普通加密)EncryptAction FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def m3():
    ret = True
    s = 20
    o = office()
    o.CreateTxt(s)
    time.sleep(3)
    c = control()
    ret = c.EncryptAction(3)
    #ret = os.system('start "" /d "D:\\DLP\\autoit" "D:\\DLP\\autoit\\EncryptAction.exe" 3')
    if ret:
        t.insert(END,"| (右键文件私有加密)EncryptAction OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| (右键文件私有加密)EncryptAction FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def m4():
    ret = True
    o = office()
    c = control()
    filename = o.get_desktop() + '\www.txt'
    isf = os.path.exists(filename)
    if isf == True: 
        flag = o.filetype(filename)
        if flag == 1:
            ret = c.EncryptAction(4)
            #ret = os.system('start "" /d "D:\\DLP\\autoit" "D:\\DLP\\autoit\\EncryptAction.exe" 4')
            if ret:
                t.insert(END,"| (右键文件解密)EncryptAction OK |\n")
                t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
                t.update()
            else:
                t.insert(END,"| (右键文件解密)EncryptAction FAIL |\n")
                t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
                t.update()
        else:
            t.insert(END,"| 不是加密文件,无法执行解密操作! |\n")
            t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
            t.update()
    else:
        t.insert(END,"| 文件不存在! |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def a1():
    ret = True
    s = SSH()
    ret = s.SendMessageForFeiq()
    if ret:
        t.insert(END,"| FeiQ OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| FeiQ FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def w1():
    ret = True
    w = control()
    filename = 'file\SN.txt'
    ret = w.whitelist_post_http_file(filename)
    if ret:
        t.insert(END,"| URL白名单 OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| URL白名单 FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def w2():
    ret = True
    w = control()
    filename = 'file\SN.txt'
    ret = w.whitelist_ip_post_http_file(filename)
    if ret:
        t.insert(END,"| IP白名单 OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| IP白名单 FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def w3():
    ret = True
    w = SMTP()
    ret = w.WhitelistSmtpAttach()
    if ret:
        t.insert(END,"| EMAIL白单 OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| EMAIL白名单 FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()

#更新svn-------------------------------------------------------------------------------------------------------------------------------------------------------------------
def svn76():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.116"
    vol = "D"
    command = "D:\\DLP\\edlp.py"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            svn = a.pythonSTAF(clientip,command)
            if svn:
                t.insert(END,"| 27.76 svn update OK |\n")
                t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")      
                t.update()
            else:
                t.insert(END,"| 27.76 svn update FAIL |\n")
                t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
                t.update()
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
#更新svn-------------------------------------------------------------------------------------------------------------------------------------------------------------------



#zhanglu-------------------------------------------------------------------------------------------------------------------------------------------------------------------

def svn83():
    ret = True
    hostname = socket.gethostname()
    vol = "C"
    username = "zhanglu83"
    password = "admin"
    if hostname == 'kdp-win7-PC':
        a = staf()
        svn = a.svn_up(vol,username,password)
        if svn == True:
            t.insert(END,"| 27.83 svn update OK |\n")
            t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")      
            t.update()
        else:
            t.insert(END,"| 27.83 svn update FAIL |\n")
            t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
            t.update()       
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()

def svn79():
    ret = True
    hostname = socket.gethostname()
    vol = "C"
    username = "zhanglu79"
    password = "admin"
    if hostname == 'kdp-win7-PC':
        a = staf()
        svn = a.svn_up(vol,username,password)
        if svn == True:
            t.insert(END,"| 27.79 svn update OK |\n")
            t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")      
            t.update()
        else:
            t.insert(END,"| 27.79 svn update FAIL |\n")
            t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
            t.update()       
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()


#zhanglu--------------------------------------------------------------------------------------------------------------------------------------------------------

#zhangji start---------------------------------------------------------------------------------------------------------------------------------------
'''def svn75():
    ret = True
    hostname = socket.gethostname()
    clientip = "local"
    vol = "C"
    command = ":\\DLP\\STAF\\svn_update\\svn_update.bat"
    if hostname == 'kdp-win7-PC':
        a = control()
        if (a.pingSTAF(clientip) == 'PONG'):
            svn = a.svnSTAF(clientip,vol,command)
            time.sleep(5)
            if svn:
                t.insert(END,"|27.75 svn update ok |\n")
                t.insert(END,"----------------------------\n")
                t.update()
            else:
                t.insert(END,"|27.75 svn update fail |\n")
                t.insert(END,"----------------------------\n")
                t.update()
                kill()

        else:
            kill()
    else:
        t.insert(END,"|sorry，you may not be the control center |\n")
        t.insert(END,"")
        t.update()

def svn77():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.77"
    vol = "C"
    command = ":\\DLP\\STAF\\svn_update\\svn_update.bat"
    if hostname == 'kdp-win7-PC':
        a = control()
        if (a.pingSTAF(clientip) == 'PONG'):
            svn = a.svnSTAF(clientip,vol,command)
            time.sleep(5)
            if svn:
                t.insert(END,"|27.77 svn update ok |\n")
                t.insert(END,"----------------------------\n")
                t.update()
            else:
                t.insert(END,"|27.77 svn update fail |\n")
                t.insert(END,"----------------------------\n")
                t.update()
            kill()

        else:
            kill()
    else:
        t.insert(END,"|sorry，you may not be the control center |\n")
        t.insert(END,"")
        t.update()


def svn80():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.80"
    vol = "D"
    command = ":\\DLP\\STAF\\svn_update\\svn_update.bat"
    if hostname == 'kdp-win7-PC':
        a = control()
        if (a.pingSTAF(clientip) == 'PONG'):
            svn = a.svnSTAF(clientip,vol,command)
            time.sleep(5)
            if svn:
                t.insert(END,"|27.80 svn update ok |\n")
                t.insert(END,"----------------------------\n")
                t.update()
            else:
                t.insert(END,"|27.80 svn update fail |\n")
                t.insert(END,"----------------------------\n")
                t.update()
                kill()
        else:
            kill()
    else:
        t.insert(END,"|sorry，you may not be the control center |\n")
        t.insert(END,"")
        t.update()
'''
def svn75():
    ret = True
    hostname = socket.gethostname()
#    clientip = "10.95.27.77"
    vol = "C"
    username = "zhangji75"
    passwd = "admin"
#    command = ":\\DLP\\STAF\\svn_update\\svn_update.bat"
    if hostname == 'kdp-win7-PC':
        a = staf()
        svn = a.svn_up(vol,username,passwd)
        time.sleep(5)
        if svn == True:
            print "27.75 svn update ok "
        else:
            print "27.75 svn update fail"
        kill()
    else:
        print "sorry，you may not be the control center"

def svn77():
    ret = True
    hostname = socket.gethostname()
#    clientip = "10.95.27.77"
    vol = "C"
    username = "zhangji77"
    passwd = "admin"
#    command = ":\\DLP\\STAF\\svn_update\\svn_update.bat"
    if hostname == 'kdp-win7-PC':
        a = staf()
        svn = a.svn_up(vol,username,passwd)
        time.sleep(5)
        if svn == True:
            print "27.77 svn update ok "
        else:
            print "27.77 svn update fail"
        kill()
    else:
        print "sorry，you may not be the control center"


def svn80():
    ret = True
    hostname = socket.gethostname()
#    clientip = "10.95.27.80"
    vol = "D"
    username = "zhangji80"
    passwd = "admin"
#    command = ":\\DLP\\STAF\\svn_update\\svn_update.bat"
    if hostname == 'kdp-win7-PC':
        a = staf()
        svn = a.svn_up(vol,username,passwd)
#        if (a.pingSTAF(clientip) == 'PONG'):
#           svn = a.svnSTAF(clientip,vol,command)
        time.sleep(5)
        if svn == True:
            print "27.80 svn update ok"
        else:
            print "27.80 svn update fail"
            kill()
    else:
        print "sorry，you may not be the control center"


#zhangji end-------------------------------------------------------------------------------------------------------------------------------------------

#安装终端-------------------------------------------------------------------------------------------------------------------------------------------------------------------
def i76():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.76"
    vol = "D"
    inst = ":\\DLP\\file\\install\\skylarinst-winc(10.95.27.118_80).exe"
    command = ":\\DLP\\autoit\\install.exe"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            sky = a.runSTAF(clientip,vol,inst)
            time.sleep(5)
            if sky:
                ret = a.install(clientip,vol,command)
                if ret:
                    t.insert(END,"| 27.76 install START |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")      
                    t.update()
                else:
                    t.insert(END,"| 27.76 install FAIL |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
                    t.update()
                    kill()
            else:
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def i116():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.116"
    vol = "D"
    inst = ":\\DLP\\file\\install\\skylarinst-winc(10.95.27.118_80).exe"
    command = ":\\DLP\\autoit\\install.exe"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            sky = a.runSTAF(clientip,vol,inst)
            time.sleep(5)
            if sky:
                ret = a.install(clientip,vol,command)
                if ret:
                    t.insert(END,"| 27.116 install START |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")      
                    t.update()
                else:
                    t.insert(END,"| 27.116 install FAIL |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
                    t.update()
                    kill()
            else:
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def i44():
    ret = True
    hostname = socket.gethostname()
    clientip = "172.24.83.44"
    vol = "E"
    inst = ":\\DLP\\file\\install\\skylarinst-winc(10.95.27.118_80).exe"
    command = ":\\DLP\\autoit\\install.exe"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            sky = a.runSTAF(clientip,vol,inst)
            time.sleep(5)
            if sky:
                ret = a.install(clientip,vol,command)
                if ret:
                    t.insert(END,"| 83.44 install START |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")      
                    t.update()
                else:
                    t.insert(END,"| 83.44 install FAIL |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
                    t.update()
                    kill()
            else:
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def i80():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.80"
    vol = "D"
    inst = ":\\DLP\\file\\install\\skylarinst-winc(10.95.27.118_80).exe"
    command = ":\\DLP\\autoit\\install.exe"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            sky = a.runSTAF(clientip,vol,inst)
            time.sleep(5)
            if sky:
                ret = a.install(clientip,vol,command)
                if ret:
                    t.insert(END,"| 27.80 install START |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")      
                    t.update()
                else:
                    t.insert(END,"| 27.80 install FAIL |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
                    t.update()
                    kill()
            else:
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def i75():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.75"
    vol = "C"
    inst = ":\\DLP\\file\\install\\skylarinst-winc(10.95.27.118_80).exe"
    command = ":\\DLP\\autoit\\install.exe"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            sky = a.runSTAF(clientip,vol,inst)
            time.sleep(5)
            if sky:
                ret = a.install(clientip,vol,command)
                if ret:
                    t.insert(END,"| 27.75 install START |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")      
                    t.update()
                else:
                    t.insert(END,"| 27.75 install FAIL |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
                    t.update()
                    kill()
            else:
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def i77():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.77"
    vol = "C"
    inst = ":\\DLP\\file\\install\\skylarinst-winc(10.95.27.118_80).exe"
    command = ":\\DLP\\autoit\\install.exe"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            sky = a.runSTAF(clientip,vol,inst)
            time.sleep(5)
            if sky:
                ret = a.install(clientip,vol,command)
                if ret:
                    t.insert(END,"| 27.77 install START |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")      
                    t.update()
                else:
                    t.insert(END,"| 27.77 install FAIL |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
                    t.update()
                    kill()
            else:
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def i74():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.74"
    vol = "D"
    inst = ":\\DLP\\file\\install\\skylarinst-winc(10.95.27.118_80).exe"
    command = ":\\DLP\\autoit\\install.exe"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            sky = a.runSTAF(clientip,vol,inst)
            time.sleep(5)
            if sky:
                ret = a.install(clientip,vol,command)
                if ret:
                    t.insert(END,"| 27.74 install START |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")      
                    t.update()
                else:
                    t.insert(END,"| 27.74 install FAIL |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
                    t.update()
                    kill()
            else:
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def i20():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.41.20"
    vol = "D"
    inst = ":\\DLP\\file\\install\\skylarinst-winc(10.95.27.118_80).exe"
    command = ":\\DLP\\autoit\\install.exe"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            sky = a.runSTAF(clientip,vol,inst)
            time.sleep(5)
            if sky:
                ret = a.install(clientip,vol,command)
                if ret:
                    t.insert(END,"| 41.20 install START |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")      
                    t.update()
                else:
                    t.insert(END,"| 41.20 install FAIL |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
                    t.update()
                    kill()
            else:
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def i76_129():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.76"
    vol = "D"
    inst = ":\\DLP\\file\\install\\skylarinst-winc(10.95.27.129_80).exe"
    command = ":\\DLP\\autoit\\install.exe"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            sky = a.runSTAF(clientip,vol,inst)
            time.sleep(5)
            if sky:
                ret = a.install(clientip,vol,command)
                if ret:
                    t.insert(END,"| 27.76 install START |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")      
                    t.update()
                else:
                    t.insert(END,"| 27.76 install FAIL |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
                    t.update()
                    kill()
            else:
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def i116_129():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.116"
    vol = "D"
    inst = ":\\DLP\\file\\install\\skylarinst-winc(10.95.27.129_80).exe"
    command = ":\\DLP\\autoit\\install.exe"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            sky = a.runSTAF(clientip,vol,inst)
            time.sleep(5)
            if sky:
                ret = a.install(clientip,vol,command)
                if ret:
                    t.insert(END,"| 27.116 install START |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")      
                    t.update()
                else:
                    t.insert(END,"| 27.116 install FAIL |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
                    t.update()
                    kill()
            else:
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def i44_129():
    ret = True
    hostname = socket.gethostname()
    clientip = "172.24.83.44"
    vol = "E"
    inst = ":\\DLP\\file\\install\\skylarinst-winc(10.95.27.129_80).exe"
    command = ":\\DLP\\autoit\\install.exe"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            sky = a.runSTAF(clientip,vol,inst)
            time.sleep(5)
            if sky:
                ret = a.install(clientip,vol,command)
                if ret:
                    t.insert(END,"| 83.44 install START |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")      
                    t.update()
                else:
                    t.insert(END,"| 83.44 install FAIL |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
                    t.update()
                    kill()
            else:
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def i80_129():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.80"
    vol = "D"
    inst = ":\\DLP\\file\\install\\skylarinst-winc(10.95.27.129_80).exe"
    command = ":\\DLP\\autoit\\install.exe"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            sky = a.runSTAF(clientip,vol,inst)
            time.sleep(5)
            if sky:
                ret = a.install(clientip,vol,command)
                if ret:
                    t.insert(END,"| 27.80 install START |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")      
                    t.update()
                else:
                    t.insert(END,"| 27.80 install FAIL |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
                    t.update()
                    kill()
            else:
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def i75_129():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.75"
    vol = "C"
    inst = ":\\DLP\\file\\install\\skylarinst-winc(10.95.27.129_80).exe"
    command = ":\\DLP\\autoit\\install.exe"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            sky = a.runSTAF(clientip,vol,inst)
            time.sleep(5)
            if sky:
                ret = a.install(clientip,vol,command)
                if ret:
                    t.insert(END,"| 27.75 install START |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")      
                    t.update()
                else:
                    t.insert(END,"| 27.75 install FAIL |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
                    t.update()
                    kill()
            else:
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def i77_129():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.77"
    vol = "C"
    inst = ":\\DLP\\file\\install\\skylarinst-winc(10.95.27.129_80).exe"
    command = ":\\DLP\\autoit\\install.exe"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            sky = a.runSTAF(clientip,vol,inst)
            time.sleep(5)
            if sky:
                ret = a.install(clientip,vol,command)
                if ret:
                    t.insert(END,"| 27.77 install START |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")      
                    t.update()
                else:
                    t.insert(END,"| 27.77 install FAIL |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
                    t.update()
                    kill()
            else:
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def i74_129():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.74"
    vol = "D"
    inst = ":\\DLP\\file\\install\\skylarinst-winc(10.95.27.129_80).exe"
    command = ":\\DLP\\autoit\\install.exe"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            sky = a.runSTAF(clientip,vol,inst)
            time.sleep(5)
            if sky:
                ret = a.install(clientip,vol,command)
                if ret:
                    t.insert(END,"| 27.74 install START |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")      
                    t.update()
                else:
                    t.insert(END,"| 27.74 install FAIL |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
                    t.update()
                    kill()
            else:
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def i20_129():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.41.20"
    vol = "D"
    inst = ":\\DLP\\file\\install\\skylarinst-winc(10.95.27.129_80).exe"
    command = ":\\DLP\\autoit\\install.exe"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            sky = a.runSTAF(clientip,vol,inst)
            time.sleep(5)
            if sky:
                ret = a.install(clientip,vol,command)
                if ret:
                    t.insert(END,"| 41.20 install START |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")      
                    t.update()
                else:
                    t.insert(END,"| 41.20 install FAIL |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
                    t.update()
                    kill()
            else:
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
def z76():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.76"
    vol = "D"
    command = ":\\DLP\\autoit\\uninstall.exe"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            ret = a.runSTAF(clientip,vol,command)
            if ret:
                t.insert(END,"| 27.76 uninstall START |\n")
                t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                t.update()
            else:
                t.insert(END,"| 27.76 uninstall FAIL |\n")
                t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                t.update()
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def z116():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.116"
    vol = "D"
    command = "D:\\DLP\\autoit\\uninstall.exe"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            ret = a.runSTAF(clientip,vol,command)
            if ret:
                t.insert(END,"| 27.116 uninstall START |\n")
                t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
                t.update()
            else:
                t.insert(END,"| 27.116 uninstall FAIL |\n")
                t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                t.update()
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def z44():
    ret = True
    hostname = socket.gethostname()
    clientip = "172.24.83.44"
    vol = "E"
    command = ":\\DLP\\autoit\\uninstall.exe"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            ret = a.runSTAF(clientip,vol,command)
            if ret:
                t.insert(END,"| 83.44 uninstall START |\n")
                t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
                t.update()
            else:
                t.insert(END,"| 83.44 uninstall FAIL |\n")
                t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                t.update()
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def z80():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.80"
    vol = "D"
    command = ":\\DLP\\autoit\\uninstall.exe"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            ret = a.runSTAF(clientip,vol,command)
            if ret:
                t.insert(END,"| 27.80 uninstall START |\n")
                t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                t.update()
            else:
                t.insert(END,"| 27.80 uninstall FAIL |\n")
                t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                t.update()
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def z75():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.75"
    vol = "C"
    command = ":\\DLP\\autoit\\uninstall.exe"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            ret = a.runSTAF(clientip,vol,command)
            if ret:
                t.insert(END,"| 27.75 uninstall START |\n")
                t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
                t.update()
            else:
                t.insert(END,"| 27.75 uninstall FAIL |\n")
                t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                t.update()
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def z77():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.77"
    vol = "C"
    command = ":\\DLP\\autoit\\uninstall.exe"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            ret = a.runSTAF(clientip,vol,command)
            if ret:
                t.insert(END,"| 27.77 uninstall START |\n")
                t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
                t.update()
            else:
                t.insert(END,"| 27.77 uninstall FAIL |\n")
                t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                t.update()
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def z74():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.74"
    vol = "D"
    command = ":\\DLP\\autoit\\uninstall.exe"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            ret = a.runSTAF(clientip,vol,command)
            if ret:
                t.insert(END,"| 27.74 uninstall START |\n")
                t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                t.update()
            else:
                t.insert(END,"| 27.74 uninstall FAIL |\n")
                t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                t.update()
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def z20():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.41.20"
    vol = "D"
    command = ":\\DLP\\autoit\\uninstall.exe"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            ret = a.runSTAF(clientip,vol,command)
            if ret:
                t.insert(END,"| 41.20 uninstall START |\n")
                t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                t.update()
            else:
                t.insert(END,"| 41.20 uninstall FAIL |\n")
                t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                t.update()
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def z83():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.83"
    vol = "C"
    command = ":\\DLP\\autoit\\uninstall.exe"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            ret = a.runSTAF(clientip,vol,command)
            if ret:
                t.insert(END,"| 27.83 uninstall START |\n")
                t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                t.update()
            else:
                t.insert(END,"| 27.83 uninstall FAIL |\n")
                t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                t.update()
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
#STAF--START--checksvn---------------------------------------------------------------------------------------------------------------------------------------------------------
def TestSTAF_svn(clientip,vol):
    ret = True
    hostname = socket.gethostname()
    command = ":\\DLP\\check.py -t"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            ret = a.pythonSTAF(clientip,vol,command)
            if ret:
                return True
            else:
                return False
        else:
            return False
            kill()
    else:
        return False
#STAF--END--checksvn---------------------------------------------------------------------------------------------------------------------------------------------------------
#START----STAF控制--------------------------------------------------------------------------------------------------------------------------------------------------------
def TestSTAF_shenji76():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.76"
    vol = "D"
    svncmd = ":\\DLP\\check.py -t"
    command = ":\\DLP\\pyauto.py -t"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            svn = a.pythonSTAF(clientip,vol,svncmd)
            time.sleep(10*6)
            if svn:
                ret = a.pythonSTAF(clientip,vol,command)
                if ret:
                    t.insert(END,"| 27.76 TestSTAF_shenji START |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                    t.update()
                else:
                    t.insert(END,"| 27.76 TestSTAF_shenji FAIL |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                    t.update()
                    kill()
            else:
                kill()
        else:
            t.insert(END,"| 对不起！你可能不是CC |\n")
            t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
            t.update()

def TestSTAF_shenji116():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.116"
    vol = "D"
    command = ":\\DLP\\pyauto.py -t"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            svn = TestSTAF_svn(clientip,vol)
            time.sleep(10)
            if svn:
                ret = a.pythonSTAF(clientip,vol,command)
                if ret:
                    t.insert(END,"| 27.116 TestSTAF_shenji START |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                    t.update()
                else:
                    t.insert(END,"| 27.116 TestSTAF_shenji FAIL |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                    t.update()
                    kill()
            else:
                kill()
        else:
            t.insert(END,"| 对不起！你可能不是CC |\n")
            t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
            t.update()

def TestSTAF_shenji74():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.74"
    vol = "D"
    command = ":\\DLP\\pyauto.py -t"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            svn = TestSTAF_svn(clientip,vol)
            time.sleep(10)
            if svn:
                ret = a.pythonSTAF(clientip,vol,command)
                if ret:
                    t.insert(END,"| 27.74 TestSTAF_shenji START |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                    t.update()
                else:
                    t.insert(END,"| 27.74 TestSTAF_shenji FAIL |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                    t.update()
                    kill()
            else:
                kill()
        else:
            t.insert(END,"| 对不起！你可能不是CC |\n")
            t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
            t.update()

def TestSTAF_shenji20():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.41.20"
    vol = "D"
    svncmd = ":\\DLP\\check.py -t"
    command = ":\\DLP\\pyauto.py -t"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            svn = a.pythonSTAF(clientip,vol,svncmd)
            time.sleep(10*6)
            if svn:
                ret = a.pythonSTAF(clientip,vol,command)
                if ret:
                    t.insert(END,"| 41.20 TestSTAF_shenji START |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                    t.update()
                else:
                    t.insert(END,"| 41.20 TestSTAF_shenji FAIL |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                    t.update()
                    kill()
            else:
                kill()
        else:
            t.insert(END,"| 对不起！你可能不是CC |\n")
            t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
            t.update()


#zhangji---STAF---START---------------------------------------------------------------------------------------------------------------------------------------------

def TestSTAF_shenji75():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.75"
    vol = "C"
    command = ":\\DLP\\pyauto.py -t"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            svn = TestSTAF_svn(clientip,vol)
            time.sleep(10)
            if svn:
                ret = a.pythonSTAF(clientip,vol,command)
                if ret:
                    t.insert(END,"| 27.75 TestSTAF_shenji START |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                    t.update()
                else:
                    t.insert(END,"| 27.75 TestSTAF_shenji FAIL |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                    t.update()
                    kill()
            else:
                kill()
        else:
            t.insert(END,"| 对不起！你可能不是CC |\n")
            t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
            t.update()



def TestSTAF_shenji77():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.77"
    vol = "C"
    command = ":\\DLP\\pyauto.py -t"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            svn = TestSTAF_svn(clientip,vol)
            time.sleep(10)
            if svn:
                ret = a.pythonSTAF(clientip,vol,command)
                if ret:
                    t.insert(END,"| 27.77 TestSTAF_shenji START |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                    t.update()
                else:
                    t.insert(END,"| 27.77 TestSTAF_shenji FAIL |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                    t.update()
                    kill()
            else:
                kill()
        else:
            t.insert(END,"| 对不起！你可能不是CC |\n")
            t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
            t.update()

def TestSTAF_shenji80():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.80"
    vol = "D"
    command = ":\\DLP\\pyauto.py -t"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            svn = TestSTAF_svn(clientip,vol)
            time.sleep(10)
            if svn:
                ret = a.pythonSTAF(clientip,vol,command)
                if ret:
                    t.insert(END,"| 27.80 TestSTAF_shenji START |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                    t.update()
                else:
                    t.insert(END,"| 27.80 TestSTAF_shenji FAIL |\n")
                    t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                    t.update()
                    kill()
            else:
                kill()
        else:
            t.insert(END,"| 对不起！你可能不是CC |\n")
            t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
            t.update()



#zhangji---STAF---END-----------------------------------------------------------------------------------------------------------------------------------------------

#zhanglu----------------------------------------------------------------------------------------------------------------------------------------
def TestSTAF_shenji83():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.83"
    vol = "C"
    command = ":\\DLP\\pyauto.py -t"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            ret = a.pythonSTAF(clientip,vol,command)
            if ret:
                t.insert(END,"| 27.83 TestSTAF_shenji START |\n")
                t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                t.update()
            else:
                t.insert(END,"| 27.83 TestSTAF_shenji FAIL |\n")
                t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                t.update()
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()

def TestSTAF_shenji79():
    ret = True
    hostname = socket.gethostname()
    clientip = "10.95.27.79"
    vol = "C"
    command = ":\\DLP\\pyauto.py -t"
    if hostname == 'kdp-win7-PC':
        a = staf()
        if (a.pingSTAF(clientip) == 'PONG'):
            ret = a.pythonSTAF(clientip,vol,command)
            if ret:
                t.insert(END,"| 27.79 TestSTAF_shenji START |\n")
                t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                t.update()
            else:
                t.insert(END,"| 27.79 TestSTAF_shenji FAIL |\n")
                t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")       
                t.update()
                kill()
        else:
            kill()
    else:
        t.insert(END,"| 对不起！你可能不是CC |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
#zhanglu----------------------------------------------------------------------------------------------------------------------------------------------------


#END----STAF控制----------------------------------------------------------------------------------------------------------------------------------------------------------
def all():
    py = pyauto()
    py.all()

def UserConformPass():
    hostname = socket.gethostname()
    #h0()
    #time.sleep(3)
    #Pass()
    #time.sleep(5)
    h1Pass()
    time.sleep(10)
    h11Pass()
    time.sleep(10)
    '''
    h1()
    time.sleep(5)
    h11()
    time.sleep(5)
    h2()
    time.sleep(5)
    h22()
    time.sleep(5)
    h3()
    time.sleep(5)
    h4()
    time.sleep(5)
    h44()
    time.sleep(5)
    if hostname == '3PFTVS4-Wuhq':
        h5()
        time.sleep(5)
    h6()
    time.sleep(5)
    if hostname == '3PFTVS4-Wuhq':
        h7()
        time.sleep(5)
    h8()
    time.sleep(5)
    e3()
    time.sleep(5)
    if hostname == 'DESKTOP-CHQS1KQ':
        e4()
        time.sleep(5)
    #e6()
    #time.sleep(5)
    n1()
    time.sleep(5)
    n2()
    time.sleep(5)
    n3()
    time.sleep(5)
    n4()
    time.sleep(5)
    n5()
    time.sleep(5)
    n6()
    time.sleep(5)
    n7()
    time.sleep(5)
    o1()
    time.sleep(5)
    w1()
    time.sleep(5)
    w2()
    time.sleep(5)
    w3()
    time.sleep(5)
    '''
def UserConformRefuse():
    hostname = socket.gethostname()
    #h0()
    #time.sleep(3)
    #Pass()
    #time.sleep(5)
    h1Refuse()
    time.sleep(10)
    h11Refuse()
    time.sleep(10)
    '''
    h1()
    time.sleep(5)
    h11()
    time.sleep(5)
    h2()
    time.sleep(5)
    h22()
    time.sleep(5)
    h3()
    time.sleep(5)
    h4()
    time.sleep(5)
    h44()
    time.sleep(5)
    if hostname == '3PFTVS4-Wuhq':
        h5()
        time.sleep(5)
    h6()
    time.sleep(5)
    if hostname == '3PFTVS4-Wuhq':
        h7()
        time.sleep(5)
    h8()
    time.sleep(5)
    e3()
    time.sleep(5)
    if hostname == 'DESKTOP-CHQS1KQ':
        e4()
        time.sleep(5)
    #e6()
    #time.sleep(5)
    n1()
    time.sleep(5)
    n2()
    time.sleep(5)
    n3()
    time.sleep(5)
    n4()
    time.sleep(5)
    n5()
    time.sleep(5)
    n6()
    time.sleep(5)
    n7()
    time.sleep(5)
    o1()
    time.sleep(5)
    w1()
    time.sleep(5)
    w2()
    time.sleep(5)
    w3()
    time.sleep(5)
    '''
def installAll_118():
    hostname = socket.gethostname()
    if hostname == 'kdp-win7-PC':
        i76()
        time.sleep(10)
        i116()
        time.sleep(10)
        i44()
        time.sleep(10)
        i80()
        time.sleep(10)
        i75()
        time.sleep(10)
        i77()
        time.sleep(10)
        #i74()
        #time.sleep(10)
        i20()
        time.sleep(10)
    else:
        kill()

def installAll_129():
    hostname = socket.gethostname()
    if hostname == 'kdp-win7-PC':
        i76_129()
        time.sleep(10)
        i116_129()
        time.sleep(10)
        i44_129()
        time.sleep(10)
        i80_129()
        time.sleep(10)
        i75_129()
        time.sleep(10)
        i77_129()
        time.sleep(10)
        #i74_129()
        #time.sleep(10)
        i20_129()
        time.sleep(10)
    else:
        kill()

def uninstallAll():
    hostname = socket.gethostname()
    if hostname == 'kdp-win7-PC':
        z76()
        time.sleep(10)
        z116()
        time.sleep(10)
        z44()
        time.sleep(10)
        z80()
        time.sleep(10)
        z75()
        time.sleep(10)
        z77()
        time.sleep(10)
        #z74()
        #time.sleep(10)
        z20()
        time.sleep(10)
    else:
        kill()

def grantAll():
    ret = True
    g = control()
    ret = g.Grant(1)
    if ret:
        t.insert(END,"| grant OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| grant FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def grantAllDis():
    ret = True
    g = control()
    ret = g.Grant(2)
    if ret:
        t.insert(END,"| grant OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| grant FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def grantDisPrint():
    ret = True
    g = control()
    ret = g.Grant(3)
    if ret:
        t.insert(END,"| grant OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| grant FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def grantReAuth():
    ret = True
    g = control()
    ret = g.Grant(4)
    if ret:
        t.insert(END,"| grant OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| grant FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def grantDisPrintScn():
    ret = True
    g = control()
    ret = g.Grant(5)
    if ret:
        t.insert(END,"| grant OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| grant FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def grantDisCopy():
    ret = True
    g = control()
    ret = g.Grant(6)
    if ret:
        t.insert(END,"| grant OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| grant FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def grantDisOfflineUse():
    ret = True
    g = control()
    ret = g.Grant(7)
    if ret:
        t.insert(END,"| grant OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| grant FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def EncryptFile():
    ret = True
    enc = control()
    ret = enc.EncryptFile()
    if ret:
        t.insert(END,"| EncryptFile OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| EncryptFile FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
def SortLevel():
    ret = True
    sort = control()
    ret = sort.SortLevel()
    if ret:
        t.insert(END,"| SortLevel OK |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()
    else:
        t.insert(END,"| SortLevel FAIL |\n")
        t.insert(END,"|--------------------------------------------------------------------------------------------------------------------------------|\n")
        t.update()

#end--------------------------------------------------------

menubar = Menu(root)

#创建下拉菜单 通道控制
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="HTTP-GET", command=h0)
filemenu.add_command(label="HTTP-POST content", command=h1)
filemenu.add_command(label="HTTP-上传文件", command=h11)
filemenu.add_command(label="HTTPS-POST content", command=h2)
filemenu.add_command(label="HTTPS-上传文件", command=h22)
filemenu.add_command(label="FTP上传文件", command=h3)
filemenu.add_command(label="SFTP上传文件", command=h33)
filemenu.add_command(label="SMTP-无附件", command=h4)
filemenu.add_command(label="SMTP-带附件", command=h44)
filemenu.add_command(label="移动存储", command=h5)
filemenu.add_command(label="外挂磁盘(仅在116上运行)", command=h55)
filemenu.add_command(label="网络共享", command=h6)
filemenu.add_command(label="蓝牙", command=h7)
filemenu.add_command(label="XPS虚拟打印", command=h8)
filemenu.add_separator()
filemenu.add_command(label="清除net use", command=h9)
filemenu.add_command(label="TELNET端口测试", command=h10)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=kill)
menubar.add_cascade(label="通道控制", menu=filemenu)

#创建另一个下拉菜单 通道增强
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="未知协议(socket)", command=e1)
editmenu.add_command(label="未知协议(Telnet)", command=e11)
editmenu.add_command(label="剪切板", command=e3)
editmenu.add_command(label="OUTLOOK(只能在27.116上正常运行)", command=e4)
editmenu.add_command(label="双向SSL", command=e5)
editmenu.add_command(label="SSH通道传输", command=e6)
editmenu.add_command(label="测试同一目的地址日志合并", command=e7)
editmenu.add_command(label="测试不同目的地址日志合并", command=e8)
editmenu.add_separator()
editmenu.add_command(label="Exit", command=kill)
menubar.add_cascade(label="通道增强",menu=editmenu)

#创建下拉菜单 功能控制
netmenu = Menu(menubar,tearoff=0)
netmenu.add_command(label="受限文件上传共享目录", command=n1)
netmenu.add_command(label="文件名+文件内容检测", command=n2)
netmenu.add_command(label="使用共享方式测试上传证据文件", command=n3)
netmenu.add_command(label="使用共享方式测试5层嵌套文件", command=n4)
netmenu.add_command(label="使用共享方式测试10层嵌套文件", command=n5)
netmenu.add_command(label="使用共享方式测试备注、脚注、批注、页眉、页脚、正文文件", command=n6)
netmenu.add_command(label="使用共享方式测试篡改后缀名的文件", command=n7)
netmenu.add_separator()
netmenu.add_command(label="随机创建WORD文件(文件输出位置DLP\Result)", command=n9)
netmenu.add_command(label="随机创建EXCEL文件(文件输出位置DLP\Result)", command=n10)
netmenu.add_command(label="随机创建PPT文件(文件输出位置DLP\Result)", command=n11)
netmenu.add_command(label="随机创建TXT文件(文件输出位置DLP\Result)", command=n12)
netmenu.add_command(label="随机创建PNG文件，用于测试OCR识别(文件输出位置DLP\Result)", command=n13)
netmenu.add_command(label="随机创建PDF文件(文件输出位置DLP\Result)", command=n14)
netmenu.add_command(label="随机创建指定大小TXT文件(文件输出位置DLP\Result)", command=n15)
netmenu.add_separator()
netmenu.add_command(label="Exit", command=kill)
menubar.add_cascade(label="功能控制", menu=netmenu)

#创建下拉菜单 图象文字识别
ocrmenu = Menu(menubar, tearoff=0)
ocrmenu.add_command(label="ORC图片拷贝到共享目录", command=o1)
ocrmenu.add_command(label="模拟feiQ发敏感消息(UDP协议)", command=a1)
ocrmenu.add_separator()
ocrmenu.add_command(label="WindowsCapture截屏", command=o2)
ocrmenu.add_command(label="ImageGrabCapture截屏", command=o3)
ocrmenu.add_command(label="微信截屏(只支持32位系统)", command=o4)
ocrmenu.add_command(label="QQ截屏(只支持32位系统)", command=o5)
ocrmenu.add_separator()
#ocrmenu.add_command(label="svn76", command=svn76)
#ocrmenu.add_command(label="svn83", command=svn83)
#ocrmenu.add_command(label="svn79", command=svn79)
#ocrmenu.add_command(label="svn75", command=svn75)
#ocrmenu.add_command(label="svn77", command=svn77)
#ocrmenu.add_command(label="svn80", command=svn80)
ocrmenu.add_command(label="Exit", command=kill)
menubar.add_cascade(label="图象文字识别", menu=ocrmenu)

#创建下拉菜单 右键菜单
Encrmenu = Menu(menubar, tearoff=0)
Encrmenu.add_command(label="右键申请文件加白", command=m1)
Encrmenu.add_command(label="右键文件普通加密", command=m2)
Encrmenu.add_command(label="右键文件私有加密", command=m3)
Encrmenu.add_command(label="右键文件解密", command=m4)
Encrmenu.add_separator()
Encrmenu.add_command(label="Exit", command=kill)
menubar.add_cascade(label="右键菜单", menu=Encrmenu)

#创建下拉菜单 应用程序控制
appmenu = Menu(menubar, tearoff=0)
appmenu.add_command(label="冒烟测试-全审计策略76", command=TestSTAF_shenji76)
appmenu.add_separator()
appmenu.add_command(label="冒烟测试-全审计策略20", command=TestSTAF_shenji20)
appmenu.add_separator()
appmenu.add_command(label="冒烟测试-全审计策略75", command=TestSTAF_shenji75)
appmenu.add_separator()
appmenu.add_command(label="冒烟测试-全审计策略77", command=TestSTAF_shenji77)
appmenu.add_separator()
appmenu.add_command(label="冒烟测试-全审计策略80", command=TestSTAF_shenji80)
appmenu.add_separator()
appmenu.add_command(label="冒烟测试-全审计策略83", command=TestSTAF_shenji83)
appmenu.add_separator()
appmenu.add_command(label="冒烟测试-全审计策略79", command=TestSTAF_shenji79)
appmenu.add_separator()
appmenu.add_command(label="Exit", command=kill)
menubar.add_cascade(label="STAF控制", menu=appmenu)

#创建下拉菜单 DLP过滤防护
whitelist = Menu(menubar, tearoff=0)
whitelist.add_command(label="上传文件测试URL白名单(URL白名单地址:41.18)", command=w1)
whitelist.add_command(label="上传文件测试IP白名单(IP白名单地址:27.119)", command=w2)
whitelist.add_command(label="带附件测试EMAIL白名单(收件人:dlptest3@dlp.cn)", command=w3)
whitelist.add_separator()
whitelist.add_command(label="Exit", command=kill)
menubar.add_cascade(label="DLP过滤防护", menu=whitelist)

#创建下拉菜单 冒烟测试
fany = Menu(menubar, tearoff=0)
fany.add_command(label="冒烟测试-全审计策略", command=all)
fany.add_command(label="冒烟测试-用户确认并阻断", command=UserConformRefuse)
fany.add_command(label="冒烟测试-用户确认并放行", command=UserConformPass)
fany.add_command(label="冒烟测试-全阻断策略(未实现)", command=hello)
fany.add_separator()
fany.add_command(label="Exit", command=kill)
menubar.add_cascade(label="冒烟测试", menu=fany)

#创建下拉菜单 加密授权文件
grant = Menu(menubar, tearoff=0)
grant.add_command(label="加密授权-全允许", command=grantAll)
grant.add_command(label="加密授权-全禁止", command=grantAllDis)
grant.add_command(label="加密授权-禁止打印", command=grantDisPrint)
grant.add_command(label="加密授权-禁止再授权", command=grantReAuth)
grant.add_command(label="加密授权-禁止截屏", command=grantDisPrintScn)
grant.add_command(label="加密授权-禁止拷贝", command=grantDisCopy)
grant.add_command(label="加密授权-禁止离线打开", command=grantDisOfflineUse)
grant.add_separator()
grant.add_command(label="文件自动加密", command=EncryptFile)
grant.add_command(label="文件分类分级加密", command=SortLevel)
grant.add_separator()
grant.add_command(label="Exit", command=kill)
menubar.add_cascade(label="终端加密授权", menu=grant)

#创建下拉菜单 安装卸载
install = Menu(menubar, tearoff=0)
install.add_command(label="118安装(安装27.76)", command=i76)
install.add_command(label="118安装(安装27.116)", command=i116)
install.add_command(label="118安装(安装83.44)", command=i44)
install.add_command(label="118安装(安装27.80)", command=i80)
install.add_command(label="118安装(安装27.75)", command=i75)
install.add_command(label="118安装(安装27.77)", command=i77)
install.add_command(label="118安装(安装27.74)", command=i74)
install.add_command(label="118安装(安装41.20)", command=i20)
install.add_separator()
install.add_command(label="129安装(安装27.76)", command=i76_129)
install.add_command(label="129安装(安装27.116)", command=i116_129)
install.add_command(label="129安装(安装83.44)", command=i44_129)
install.add_command(label="129安装(安装27.80)", command=i80_129)
install.add_command(label="129安装(安装27.75)", command=i75_129)
install.add_command(label="129安装(安装27.77)", command=i77_129)
install.add_command(label="129安装(安装27.74)", command=i74_129)
install.add_command(label="129安装(安装41.20)", command=i20_129)
install.add_separator()
install.add_command(label="118全部安装(安装76|116|44|80|75|77|20)", command=installAll_118)
install.add_command(label="129全部安装(安装76|116|44|80|75|77|20)", command=installAll_129)
install.add_command(label="全部卸载(卸载76|116|44|80|75|77|20)", command=uninstallAll)
install.add_separator()
install.add_command(label="卸载(卸载27.76)", command=z76)
install.add_command(label="卸载(卸载27.116)", command=z116)
install.add_command(label="卸载(卸载83.44)", command=z44)
install.add_command(label="卸载(卸载27.80)", command=z80)
install.add_command(label="卸载(卸载27.75)", command=z75)
install.add_command(label="卸载(卸载27.77)", command=z77)
install.add_command(label="卸载(卸载27.74)", command=z74)
install.add_command(label="卸载(卸载41.20)", command=z20)
install.add_command(label="卸载(卸载27.83)", command=z83)
install.add_separator()
install.add_command(label="Exit", command=kill)
menubar.add_cascade(label="一键安装/卸载终端", menu=install)

'''
#zhangji start---------------------------------------------------------------
#创建SVN菜单 SVN自动下发
ocrmenu = Menu(menubar, tearoff=0)
ocrmenu.add_separator()
ocrmenu.add_command(label="svn76", command=svn76)
ocrmenu.add_separator()
ocrmenu.add_command(label="svn75", command=svn75)
ocrmenu.add_separator()
ocrmenu.add_command(label="svn77", command=svn77)
ocrmenu.add_separator()
ocrmenu.add_command(label="svn80", command=svn80)
ocrmenu.add_separator()
ocrmenu.add_command(label="Exit", command=kill)
menubar.add_cascade(label="SVN自动下发", menu=ocrmenu)

#zhangji end------------------------------------------------------------------
'''

#显示菜单
root.config(menu=menubar)

mainloop()
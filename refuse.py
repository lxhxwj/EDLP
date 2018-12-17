#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
import urllib2
import httplib
import requests
import socket
import ssl
import json
import os
import random
import string
import shutil
import win32print
import win32ui
import win32con
import win32api
import win32process
import time
import smtplib
from selenium import webdriver
from email.mime.text import MIMEText
from email.utils import formataddr
from sys import argv
from ftplib import FTP
# 禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



class controlR:

   #模拟HTTP提交content 
   def post_http_content(self):
      ret=True
      try:      
         #定义一个要提交的数据数组(字典)
         data = {}
         data['contents'] = 'wangbaoqiang王宝强'
         #data['fileImage'] = '123456' 
         #定义post的地址
         url = 'http://10.95.41.15:8000/php/post.php'
         post_data = urllib.urlencode(data) 
         #提交，发送数据
         req = urllib2.urlopen(url, post_data) 
         #获取提交后返回的信息
         content = req.read()
         #return content
         print "http upload OK"
         return ret   
      except Exception,e:
         print e
         print "http upload False"
         return False
      return

   #模拟FTP上传文件 
   def ftp_up(self):
      ret=True
      try:
         ftp=FTP()
         ftp.set_debuglevel(0)
         #打开调试级别2，显示详细信息;0为关闭调试信息
         ftp.connect('10.95.41.1','21')
         #连接
         ftp.login('test','1')
         #登录，如果匿名登录则用空串代替即可
         #print ftp.getwelcome()
         #显示ftp服务器欢迎信息
         ftp.cwd('FTP')
         #选择操作目录
         bufsize = 1024
         #设置缓冲块大小
         file_handler = open("file\\ftp.txt",'rb')
         #以读模式在本地打开文件
         upload = ftp.storbinary('STOR %s' % os.path.basename("file\\ftp.txt"),file_handler,bufsize)
         #上传文件
         ftp.set_debuglevel(0)
         file_handler.close()
         ftp.quit()
         print upload
         print "ftp upload OK"
         return ret
      except Exception,e:
         print e
         print "ftp upload False"
         return False
      return

   #拷贝文件到共享目录，共享地址已写死
   def cpfile(self):
      ret=True
      try:
         #sharePath = '\\\\10.95.41.15\\project\\Test\\cpfile'
         sharePath = '\\\\10.95.27.99\\wuhq'
         srcFilename = 'file\\ftp.txt'
         if os.path.exists(srcFilename):
            os.popen('copy %s %s'%(srcFilename,sharePath),'rw')
            print "samba upload OK"
            return ret
         else:
            print "samba upload False"
            return False
      except Exception,e:
         print e
         print "samba upload False"
         return False
      return
   #拷贝文件到共享目录，共享地址已写死
   #\\10.95.27.99
   #待拷贝的文件：dlp.doc,与netsharefile.exe同目录
   def netsharefile(self):
      ret=True
      try:
         x = os.system('autoit\\netsharefile.exe')
         if x == 0:
            print "netsharefile OK"
            return True
         else:
            print "netsharefile False"
            return False
      except Exception,e:
         print e
         print "netsharefile False"
         return False
      return

   #打印功能，含操作windows控件操作
   def print2Printer(self):
      ret=True
      try:  
         rfile = string.join(random.sample('abcdefghijklmnopqistuvwxyz',3))         
         dfile = "C:\Users\Administrator\Desktop\\" + rfile.replace(' ', '') + ".xps"
         pfile = 'file\\ftp.txt'
         if os.path.exists(pfile):
            win32api.ShellExecute(0,'print',pfile,win32print.GetDefaultPrinterW(),".",0)
            x = os.system('dialogconform.exe')
            if x == 0:
               print "print file OK"
               return True
            else:
               print "print file False"
               return False
         else:
            print "打印文件不存在"
            print "print file False"
            return False
      except Exception,e:
         print e
         print "print file False"
         return False
      return

   def printer(self):
      ret=True
      try:
         x = os.system('autoit\\printer.exe')
         if x == 0:
            print "print OK"
            return True
         else:
            print "print False"
            return False
      except Exception,e:
         print e
         print "print False"
         return False
      return  

   #杀掉python进程         
   def killpython(self):
      ret=True
      try:
         num = 1
         while (num < 6):
            os.system('autoit\\killpython.exe')
            num = num + 1
            if num == 6:
               break
         return True
      except Exception,e:
         print e
         return False
      return


   #模拟SMTP发送邮件  
   def smtp(self,fr,to,t,sub):
      #if _DEBUG == True:
      #import pdb
      #pdb.set_trace()
      #my_sender = 'test1@dlp.cn'
      my_sender = fr + '@dlp.cn'
      my_pass = 'Aa123456'
      #my_user = 'test2@dlp.cn'
      my_user = to + '@dlp.cn'

      ret=True
      try:
         msg=MIMEText(t,'plain','utf-8')
         msg['From']=formataddr([fr,my_sender])
         msg['To']=formataddr([to,my_user])
         msg['Subject']=sub
         server=smtplib.SMTP("10.95.41.18",25)
         server.login(my_sender,my_pass)
         server.sendmail(my_sender,[my_user,],msg.as_string())
         server.quit()
         print "SMTP OK"
         return True
      except Exception,e:
         print e
         print "SMTP False"
         return False
      return

   #模拟蓝牙传输文件        
   def bluetooth(self):
      ret=True
      try:
         os.system('autoit\\bluetooth.exe')
         os.system('autoit\\ALLRefuse.exe')
         print "bluetooth OK" 
         return True
      except Exception,e:
         print e
         print "bluetooth False" 
         return False    
      return

   #模拟剪切板复制  王宝强|wangbaoqiang        
   def clipboard(self):
      ret=True
      try:
         os.system('autoit\\clipboard.exe')
         print "clipboard OK" 
         return True
      except Exception,e:
         print e
         print "clipboard False" 
         return False    
      return

   #模拟拷贝文件到U盘
   #必须插入U盘
   #待拷贝的文件：dlp.doc,与udriver.exe同目录
   def udriver(self):
      ret=True
      try:
         x = os.system('autoit\\udriver.exe')
         os.system('autoit\\uDriverRefuse.exe')
         if x == 0:
            print "udriver OK"
            return True
         else:
            print "udriver False"
            return False
      except Exception,e:
         print e
         print "udriver False"
         return False
      return
	  
   # def udriver(self):
		# try :
			# handle = win32process.CreateProcess('udriver.exe',
                # '', None, None, 0,
                # win32process.CREATE_NO_WINDOW, 
                # None , 
                # exe_path,
                # win32process.STARTUPINFO())
			# running = True        
		# except Exception, e:
			# print "Create Error!"
			# handle = None
			# running = False
		# return

if __name__ == "__main__":
   app = controlR()
   print(app.ftp_up())
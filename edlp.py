#!/usr/bin/python
# -*- coding: UTF-8 -*-

import ctypes
import platform
import urllib
import urllib2
import base64
import platform
import ConfigParser
import re
import base64
from urlparse import urlparse 
import httplib
import requests
import socket
import paramiko 
import ssl
import json
import getopt
import WinAction
import multiprocessing
hostname = socket.getfqdn(socket.gethostname())
ipaddr = socket.gethostbyname(hostname)
if platform.machine() == 'AMD64' and ipaddr == '10.95.41.17':
   from PySTAF import *
   from PySTAFMon import *
   from PySTAFLog import *
import subprocess
import sys,os
sys.path.append("C:\STAF\lib")
import random
import string
import shutil
import win32console
import win32print
import win32ui
import win32con
import win32gui
import win32api
import win32process
import signal
import time
import smtplib
import win32clipboard as wc
#import numpy as np
from PIL import Image
from PIL import ImageGrab
from faker import Factory
from faker import Faker
from selenium import webdriver
from email.mime.text import MIMEText
from email.utils import formataddr
from sys import argv
from ftplib import FTP

#import itchat
#from itchat.content import *
# 禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class control:

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
   def post_http_content_pass(self):
      c = control()
      try:
         #p1 = multiprocessing.Process(target=urllib2.urlopen,args=(url, post_data))
         p1 = multiprocessing.Process(target=c.post_http_content,args=())
         p2 = multiprocessing.Process(target=WinAction.Pass,args=())
         
         p1.start()
         time.sleep(3)
         p2.start()
         
         p1.join()
         p2.join()
         return True   
      except Exception,e:
         print e
         return False
      return
   def post_http_content_refuse(self):
      c = control()
      try:
         #p1 = multiprocessing.Process(target=urllib2.urlopen,args=(url, post_data))
         p1 = multiprocessing.Process(target=c.post_http_content,args=())
         p2 = multiprocessing.Process(target=WinAction.Refuse,args=())
         
         p1.start()
         time.sleep(3)
         p2.start()
         
         p1.join()
         p2.join()
         return True   
      except Exception,e:
         print e
         return False
      return
   def get_http(self):
   		ret=True
   		try:
	   		url = "http://www.baidu.com/s?wd=王宝强"
			req = urllib2.Request(url)
			#print req
			res_data = urllib2.urlopen(req)
			res = res_data.read()
			#print res
			print "http get OK"
			return ret
		except Exception,e:
			print e
         	print "http get False"
         	return False
		return
   #模拟HTTP提交file
   def post_http_file(self,ip,port,filename):
      ret=True
      try:
         data = []
         boundary = '----------%s' % hex(int(time.time() * 1000))
         data.append('--%s' % boundary)

         url = "http://%s:%s/upload_file.php" % (ip, port)

         data.append('Content-Disposition: form-data; name="%s"\r\n' % 'args')
         data.append(base64.b64encode(filename))
         data.append('--%s' % boundary)


         fr=open(filename,'rb')
         data.append('Content-Disposition: form-data; name="%s"; filename="%s"' % ('file', filename))
         data.append('Content-Type: %s\r\n' % 'application/octet-stream')
         data.append(fr.read())
         fr.close()
         data.append('--%s--\r\n' % boundary)

         http_body='\r\n'.join(data)
         #   print http_body
         #buld http request
         req=urllib2.Request(url, data=http_body)
         #header
         req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
         req.add_header('User-Agent','Mozilla/5.0')
         req.add_header('Referer','http://%s/' % ip)
         #post data to server
         resp = urllib2.urlopen(req, timeout=5)
         #get response
         qrcont=resp.read()
         #print qrcont
         print "http upload file OK"
         return ret
      except Exception as e:
         #print(": unable to send URL: {0}".format(e))
         print "http upload file False"
         return False
      return
   def post_http_file_pass(self,ip,port,filename):
      c = control()
      try:
         #p1 = multiprocessing.Process(target=urllib2.urlopen,args=(url, post_data))
         p1 = multiprocessing.Process(target=c.post_http_file,args=(ip,port,filename))
         p2 = multiprocessing.Process(target=WinAction.Pass,args=())
         
         p1.start()
         time.sleep(3)
         p2.start()
         
         p1.join()
         p2.join()
         return True   
      except Exception,e:
         print e
         return False
      return
   def post_http_file_refuse(self,ip,port,filename):
      c = control()
      try:
         #p1 = multiprocessing.Process(target=urllib2.urlopen,args=(url, post_data))
         p1 = multiprocessing.Process(target=c.post_http_file,args=(ip,port,filename))
         p2 = multiprocessing.Process(target=WinAction.Refuse,args=())
         
         p1.start()
         time.sleep(3)
         p2.start()
         
         p1.join()
         p2.join()
         return True   
      except Exception,e:
         print e
         return False
      return
   #白名单测试模拟HTTP提交file
   def whitelist_post_http_file(self,filename):
      data = []
      boundary = '----------%s' % hex(int(time.time() * 1000))
      data.append('--%s' % boundary)

      url = "http://%s:%s/HTTP" % ('10.95.41.18', '8001')

      data.append('Content-Disposition: form-data; name="%s"\r\n' % 'args')
      data.append(base64.b64encode(filename))
      data.append('--%s' % boundary)


      fr=open(filename,'rb')
      data.append('Content-Disposition: form-data; name="%s"; filename="%s"' % ('file', filename))
      data.append('Content-Type: %s\r\n' % 'application/octet-stream')
      data.append(fr.read())
      fr.close()
      data.append('--%s--\r\n' % boundary)

      http_body='\r\n'.join(data)

      #带密码认证HTTP网页上传文件
      Username = 'test'
      Password = '1'
      base64string = base64.encodestring('%s:%s' % (Username, Password))[:-1] #注意哦，这里最后会自动添加一个\n
      authheader =  "Basic %s" % base64string
      
      #   print http_body
      #buld http request
      req=urllib2.Request(url, data=http_body)
      #header
      req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
      req.add_header('User-Agent','Mozilla/5.0')
      req.add_header('Referer','http://10.95.41.18/')
      req.add_header("Authorization", authheader)

      ret=True
      try:
         #post data to server
         #resp = urllib2.urlopen(req, timeout=10)
         resp = urllib2.urlopen(req)
         #get response
         #qrcont=resp.read()
         #print qrcont
         print "whitelist URL http upload file OK"
         return ret
      except urllib2.URLError as e:
         if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
            print "whitelist URL http upload file False"
            #print(": unable to send URL: {0}".format(e))
            return False
         elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
            print "whitelist URL http upload file False"
            return False
         else:
            qrcont = resp.read()
            print qrcont
            return ret
   def whitelist_post_http_file_pyauto(self,ip,port,filename):
      data = []
      boundary = '----------%s' % hex(int(time.time() * 1000))
      data.append('--%s' % boundary)

      url = "http://%s:%s/HTTP" % (ip, port)

      data.append('Content-Disposition: form-data; name="%s"\r\n' % 'args')
      data.append(base64.b64encode(filename))
      data.append('--%s' % boundary)


      fr=open(filename,'rb')
      data.append('Content-Disposition: form-data; name="%s"; filename="%s"' % ('file', filename))
      data.append('Content-Type: %s\r\n' % 'application/octet-stream')
      data.append(fr.read())
      fr.close()
      data.append('--%s--\r\n' % boundary)

      http_body='\r\n'.join(data)

      #带密码认证HTTP网页上传文件
      Username = 'test'
      Password = '1'
      base64string = base64.encodestring('%s:%s' % (Username, Password))[:-1] #注意哦，这里最后会自动添加一个\n
      authheader =  "Basic %s" % base64string
      
      #   print http_body
      #buld http request
      req=urllib2.Request(url, data=http_body)
      #header
      req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
      req.add_header('User-Agent','Mozilla/5.0')
      req.add_header('Referer','http://%s/' % ip)
      req.add_header("Authorization", authheader)

      ret=True
      try:
         #post data to server
         #resp = urllib2.urlopen(req, timeout=10)
         resp = urllib2.urlopen(req)
         #get response
         #qrcont=resp.read()
         #print qrcont
         
         return ret
      except urllib2.URLError as e:
         if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
            print(": unable to send URL: {0}".format(e))
            
            return False
         elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
            
            return False
         else:
            qrcont = resp.read()
            print qrcont
            return ret

   #白名单测试模拟HTTP提交file
   def whitelist_ip_post_http_file(self,filename):
      data = []
      boundary = '----------%s' % hex(int(time.time() * 1000))
      data.append('--%s' % boundary)

      url = "http://%s:%s/HTTP" % ('10.95.27.119', '8001')

      data.append('Content-Disposition: form-data; name="%s"\r\n' % 'args')
      data.append(base64.b64encode(filename))
      data.append('--%s' % boundary)


      fr=open(filename,'rb')
      data.append('Content-Disposition: form-data; name="%s"; filename="%s"' % ('file', filename))
      data.append('Content-Type: %s\r\n' % 'application/octet-stream')
      data.append(fr.read())
      fr.close()
      data.append('--%s--\r\n' % boundary)

      http_body='\r\n'.join(data)

      #带密码认证HTTP网页上传文件
      Username = 'test'
      Password = '1'
      base64string = base64.encodestring('%s:%s' % (Username, Password))[:-1] #注意哦，这里最后会自动添加一个\n
      authheader =  "Basic %s" % base64string
      
      #   print http_body
      #buld http request
      req=urllib2.Request(url, data=http_body)
      #header
      req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
      req.add_header('User-Agent','Mozilla/5.0')
      req.add_header('Referer','http://10.95.27.119/')
      req.add_header("Authorization", authheader)

      ret=True
      try:
         #post data to server
         #resp = urllib2.urlopen(req, timeout=10)
         resp = urllib2.urlopen(req)
         print "whitelist IP http upload file OK"
         return True
      except urllib2.URLError as e:
         if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
            #print(": unable to send URL: {0}".format(e))
            print "whitelist IP http upload file False"
            return False
         elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
            print "whitelist IP http upload file False"
            return False
         else:
            qrcont = resp.read()
            print qrcont
            return ret

   #模拟FTP上传文件
   def ftp_up(self):
      ret=True
      try:
         filename = "file\\ftp.txt"
         ftp=FTP()
         ftp.set_debuglevel(0)
         #打开调试级别2，显示详细信息;0为关闭调试信息
         ftp.connect('10.95.41.15','21')
         #连接
         ftp.login('test','1')
         #登录，如果匿名登录则用空串代替即可
         #print ftp.getwelcome()
         #显示ftp服务器欢迎信息
         ftp.cwd('FTP')
         #选择操作目录
         bufsize = 1024
         #设置缓冲块大小
         file_handler = open(filename,'rb')
         #以读模式在本地打开文件
         ftp.storbinary('STOR %s' % os.path.basename(filename),file_handler,bufsize)
         #上传文件
         ftp.set_debuglevel(0)
         file_handler.close()
         ftp.quit()
         print "ftp upload OK"
         return ret
      except Exception,e:
         print e
         print "ftp upload False"
         return False
      return
   def sftp_up(self):
      c = control()
      host = '10.95.41.15'
      port = 22
      username = 'root'
      password = 'www.360.cn'
      vol = c.GetVol()
      local = vol + r':\DLP\file\dlp.doc'
      remote = '/home/test/dlp.doc'
      try:
        t = paramiko.Transport((host, 22))
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(local, remote)
        t.close()
        print 'sftp upload OK'
        return True
      except Exception, e:
        print e
        print 'sftp upload False'
        return False

   def ftp_up_pyauto(self,vol):
      ret=True
      try:
         filename = "%s:\\DLP\\file\\ftp.txt" % vol
         ftp=FTP()
         ftp.set_debuglevel(0)
         #打开调试级别2，显示详细信息;0为关闭调试信息
         ftp.connect('10.95.41.15','21')
         #连接
         ftp.login('test','1')
         #登录，如果匿名登录则用空串代替即可
         #print ftp.getwelcome()
         #显示ftp服务器欢迎信息
         ftp.cwd('FTP')
         #选择操作目录
         bufsize = 1024
         #设置缓冲块大小
         file_handler = open(filename,'rb')
         #以读模式在本地打开文件
         ftp.storbinary('STOR %s' % os.path.basename(filename),file_handler,bufsize)
         #上传文件
         ftp.set_debuglevel(0)
         file_handler.close()
         ftp.quit()
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
   def netshare(self,param):
      ret=True
      try:
         x = os.system("autoit\\netsharefile.exe %s" %param)
         if x == 0:
            print "netshare OK"
            return True
         else:
            print "netshare False"
            return False
      except Exception,e:
         print e
         print "netshare False"
         return False
      return

   def netshare_pyauto(self,vol,param):
      ret=True
      try:
         x = os.system("%s:\\DLP\\autoit\\netsharefilePyauto.exe %s" % (vol,param))
         if x == 0:
            print "netshare OK"
            return True
         else:
            print "netshare False"
            return False
      except Exception,e:
         print e
         print "netshare False"
         return False
      return

   def file_name(self,file_dir):
      L=[]
      for root, dirs, files in os.walk(file_dir):
         for file in files:
            L.append(os.path.join(root, file))
      return L

   def PyautoCopyFile(self,vol,source_files,target_files):
      o = control()
      try:         
         x = os.system("%s:\\DLP\\autoit\\netLogon.exe" % vol)
         time.sleep(15)
         if x == 0:
            file = o.file_name(source_files)
            for f in file:    
               shutil.copy(f,target_files)
            return True
         else:
            print "netLogon False"
            return False
      except Exception,e:
         print e
         print "netLogon False"
         return False
   def copyFiles(self,source_files,target_files):
      o = control()
      try:         
         file = o.file_name(source_files)
         for f in file:    
            shutil.copy(f,target_files)
         return True
      except Exception,e:
         print e
         return False
   #打印功能，含操作windows控件操作
   def print2Printer(self):
      ret=True
      try:  
         rfile = string.join(random.sample('abcdefghijklmnopqistuvwxyz',3))         
         dfile = "C:\Users\Administrator\Desktop\\" + rfile.replace(' ', '') + ".xps"
         pfile = 'file\\ftp.txt'
         if os.path.exists(pfile):
            win32api.ShellExecute(0,'print',pfile,win32print.GetDefaultPrinterW(),".",0)
            x = os.system('autoit\\dialogconform.exe')
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

   def printer_pyauto(self,vol):
      ret=True
      try:
         x = os.system('%s:\\DLP\\autoit\\printerPyauto.exe' % vol)
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
         print "bluetooth OK" 
         return True
      except Exception,e:
         print e
         print "bluetooth False" 
         return False    
      return
   def bluetooth_pyauto(self,vol):
      ret=True
      try:
         os.system('%s:\\DLP\\autoit\\bluetooth.exe' % vol)
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
   def clipboard_pyauto(self,vol):
      ret=True
      try:
         os.system('%s:\\DLP\\autoit\\clipboard.exe' % vol)
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

   def udriver_pyauto(self,vol):
      ret=True
      try:
         x = os.system('%s:\\DLP\\autoit\\udriver.exe' % vol)
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

   def Grant(self,param):
      ret = True
      try:
         x = os.system("autoit\\DLPGrant.exe %s" %param)
         if x == 0:
            print "Grant OK"
            return True
         else:
            print "Grant False"
            return False
      except Exception,e:
         print e
         print "Grant False"
         return False
      return

   def EncryptFile(self):
      ret = True
      try:
         x = os.system('autoit\\EncryptFile.exe')
         if x == 0:
            print "EncryptFile OK"
            return True
         else:
            print "EncryptFile False"
            return False
      except Exception,e:
         print e
         print "EncryptFile False"
         return False
      return

   def SortLevel(self):
      ret = True
      try:
         x = os.system('autoit\\SortLevel.exe')
         if x == 0:
            print "SortLevel OK"
            return True
         else:
            print "SortLevel False"
            return False
      except Exception,e:
         print e
         print "SortLevel False"
         return False
      return

   def feiq(self):
      ret = True
      try:
         x = os.system('autoit\\FeiQ.exe')
         if x == 0:
            print "FeiQ OK"
            return True
         else:
            print "FeiQ False"
            return False
      except Exception,e:
         print e
         print "FeiQ False"
         return False
      return
   def feiq_pyauto(self,vol):
      ret = True
      try:
         x = os.system('%s:\\DLP\\autoit\\FeiQ.exe' % vol)
         if x == 0:
            print "FeiQ OK"
            return True
         else:
            print "FeiQ False"
            return False
      except Exception,e:
         print e
         print "FeiQ False"
         return False
      return

   def svn_up(self,vol,username,password):
      ret = True
      os.system('svn cleanup %s:\\DLP' % vol)
      try:
         x = os.system('svn update %s:\\DLP --username %s --password %s' % (vol,username,password))
         if x == 0:
            print "svn_up OK"
            return True
         else:
            print "svn_up False"
            return False
      except Exception,e:
         print e
         print "svn_up False"
         return False
      return

   def UserConformPass(self):
      hostname = socket.getfqdn(socket.gethostname())
      ipaddr = socket.gethostbyname(hostname)
      try:
         if ipaddr == '10.95.27.76':
            x = os.system('D:\\DLP\\autoit\\UserConformPass.exe')
            if x == 0:
               print "UserConformPass OK"
               return True
            else:
               print "UserConformPass False"
               return False
         elif ipaddr == '10.95.41.20':
            x = os.system('D:\\DLP\\autoit\\UserConformPass.exe')
            if x == 0:
               print "UserConformPass OK"
               return True
            else:
               print "UserConformPass False"
               return False
         elif ipaddr == '10.95.27.116':
            x = os.system('D:\\DLP\\autoit\\UserConformPass.exe')
            if x == 0:
               print "UserConformPass OK"
               return True
            else:
               print "UserConformPass False"
               return False
         elif ipaddr == '10.95.27.74':
            x = os.system('D:\\DLP\\autoit\\UserConformPass.exe')
            if x == 0:
               print "UserConformPass OK"
               return True
            else:
               print "UserConformPass False"
               return False
         elif ipaddr == '10.95.41.17':
            x = os.system('D:\\DLP\\autoit\\UserConformPass.exe')
            if x == 0:
               print "UserConformPass OK"
               return True
            else:
               print "UserConformPass False"
               return False
         elif ipaddr == '10.95.27.75':
            x = os.system('C:\\DLP\\autoit\\UserConformPass.exe')
            if x == 0:
               print "UserConformPass OK"
               return True
            else:
               print "UserConformPass False"
               return False
         elif ipaddr == '10.95.27.77':
            x = os.system('C:\\DLP\\autoit\\UserConformPass.exe')
            if x == 0:
               print "UserConformPass OK"
               return True
            else:
               print "UserConformPass False"
               return False
         elif ipaddr == '10.95.27.80':
            x = os.system('D:\\DLP\\autoit\\UserConformPass.exe')
            if x == 0:
               print "UserConformPass OK"
               return True
            else:
               print "UserConformPass False"
               return False
         elif ipaddr == '10.95.27.83':
            x = os.system('C:\\DLP\\autoit\\UserConformPass.exe')
            if x == 0:
               print "UserConformPass OK"
               return True
            else:
               print "UserConformPass False"
               return False
         elif ipaddr == '10.95.27.79':
            x = os.system('C:\\DLP\\autoit\\UserConformPass.exe')
            if x == 0:
               print "UserConformPass OK"
               return True
            else:
               print "UserConformPass False"
               return False
         elif ipaddr == '172.24.83.62':
            x = os.system('D:\\DLP\\autoit\\UserConformPass.exe')
            if x == 0:
               print "UserConformPass OK"
               return True
            else:
               print "UserConformPass False"
               return False
         else:
         	print(u"非法IP地址,默认按照D盘路径执行,请测试人员确认!")
         	x = os.system('D:\\DLP\\autoit\\UserConformPass.exe')
         	if x == 0:
         		print "UserConformPass OK"
         		return True
         	else:
         		print "UserConformPass False"
         		return False
            #sys.exit(2)     
      except Exception,e:
         print e
         print "UserConformPass False"
         return False
      return

   def UserConformRefuse(self):
      hostname = socket.getfqdn(socket.gethostname())
      ipaddr = socket.gethostbyname(hostname)
      try:
         if ipaddr == '10.95.27.76':
            x = os.system('D:\\DLP\\autoit\\UserConformRefuse.exe')
            if x == 0:
               print "UserConformRefuse OK"
               return True
            else:
               print "UserConformRefuse False"
               return False
         elif ipaddr == '10.95.41.20':
            x = os.system('D:\\DLP\\autoit\\UserConformRefuse.exe')
            if x == 0:
               print "UserConformRefuse OK"
               return True
            else:
               print "UserConformRefuse False"
               return False
         elif ipaddr == '10.95.27.116':
            x = os.system('D:\\DLP\\autoit\\UserConformRefuse.exe')
            if x == 0:
               print "UserConformRefuse OK"
               return True
            else:
               print "UserConformRefuse False"
               return False
         elif ipaddr == '10.95.27.74':
            x = os.system('D:\\DLP\\autoit\\UserConformRefuse.exe')
            if x == 0:
               print "UserConformRefuse OK"
               return True
            else:
               print "UserConformRefuse False"
               return False
         elif ipaddr == '10.95.41.17':
            x = os.system('D:\\DLP\\autoit\\UserConformRefuse.exe')
            if x == 0:
               print "UserConformRefuse OK"
               return True
            else:
               print "UserConformRefuse False"
               return False
         elif ipaddr == '10.95.27.75':
            x = os.system('C:\\DLP\\autoit\\UserConformRefuse.exe')
            if x == 0:
               print "UserConformRefuse OK"
               return True
            else:
               print "UserConformRefuse False"
               return False
         elif ipaddr == '10.95.27.77':
            x = os.system('C:\\DLP\\autoit\\UserConformRefuse.exe')
            if x == 0:
               print "UserConformRefuse OK"
               return True
            else:
               print "UserConformRefuse False"
               return False
         elif ipaddr == '10.95.27.80':
            x = os.system('D:\\DLP\\autoit\\UserConformRefuse.exe')
            if x == 0:
               print "UserConformRefuse OK"
               return True
            else:
               print "UserConformRefuse False"
               return False
         elif ipaddr == '10.95.27.83':
            x = os.system('C:\\DLP\\autoit\\UserConformRefuse.exe')
            if x == 0:
               print "UserConformRefuse OK"
               return True
            else:
               print "UserConformRefuse False"
               return False
         elif ipaddr == '10.95.27.79':
            x = os.system('C:\\DLP\\autoit\\UserConformRefuse.exe')
            if x == 0:
               print "UserConformRefuse OK"
               return True
            else:
               print "UserConformRefuse False"
               return False
         elif ipaddr == '172.24.83.62':
            x = os.system('D:\\DLP\\autoit\\UserConformRefuse.exe')
            if x == 0:
               print "UserConformRefuse OK"
               return True
            else:
               print "UserConformRefuse False"
               return False
         else:
         	print(u"非法IP地址,默认按照D盘路径执行,请测试人员确认!")
         	x = os.system('D:\\DLP\\autoit\\UserConformRefuse.exe')
         	if x == 0:
         		print "UserConformRefuse OK"
         		return True
         	else:
         		print "UserConformRefuse False"
         		return False
            #sys.exit(2)     
      except Exception,e:
         print e
         print "UserConformRefuse False"
         return False
      return

   def RunAs(self):
      #username = "administrator"
      #domain = "."
      #password ="www.360.cn"
      cmd = "uninstall.exe"

      free_console=True
      try:
         win32console.AllocConsole()
      except win32console.error as exc:
         if exc.winerror!=5:
            raise
      ## only free console if one was created successfully
      free_console=False

      stdin=win32console.GetStdHandle(win32console.STD_INPUT_HANDLE)

      #p = subprocess.Popen(["runas",r"/user:{}\{}".format(domain,username),cmd],stdout=subprocess.PIPE)

      subprocess.Popen("runas /savecred /user:Administrator %s" %cmd, shell=True)
      '''
      while True:
         if p.stdout.read(1)==":":
            for c in "{}\r".format(password):  # end by CR to send "RETURN"
               ## write some records to the input queue
               x=win32console.PyINPUT_RECORDType(win32console.KEY_EVENT)
               x.Char=unicode(c)
               x.KeyDown=True
               x.RepeatCount=1
               x.VirtualKeyCode=0x0
               x.ControlKeyState=win32con.SHIFT_PRESSED
               stdin.WriteConsoleInput([x])
            p.wait()
            break
      '''      
   def EncryptAction(self,param):
      hostname = socket.getfqdn(socket.gethostname())
      ipaddr = socket.gethostbyname(hostname)
      try:
         if ipaddr == '10.95.27.76':
            x = os.system('start "" /d "D:\\DLP\\autoit" "D:\\DLP\\autoit\\EncryptAction.exe" %s' %param)
            if x == 0:
               print "EncryptAction OK"
               return True
            else:
               print "EncryptAction False"
               return False
         elif ipaddr == '10.95.41.20':
            x = os.system('start "" /d "D:\\DLP\\autoit" "D:\\DLP\\autoit\\EncryptAction.exe" %s' %param)
            if x == 0:
               print "EncryptAction OK"
               return True
            else:
               print "EncryptAction False"
               return False
         elif ipaddr == '10.95.27.116':
            x = os.system('start "" /d "D:\\DLP\\autoit" "D:\\DLP\\autoit\\EncryptAction.exe" %s' %param)
            if x == 0:
               print "EncryptAction OK"
               return True
            else:
               print "EncryptAction False"
               return False
         elif ipaddr == '10.95.27.74':
            x = os.system('start "" /d "D:\\DLP\\autoit" "D:\\DLP\\autoit\\EncryptAction.exe" %s' %param)
            if x == 0:
               print "EncryptAction OK"
               return True
            else:
               print "EncryptAction False"
               return False
         elif ipaddr == '10.95.41.17':
            x = os.system('start "" /d "D:\\DLP\\autoit" "D:\\DLP\\autoit\\EncryptAction.exe" %s' %param)
            if x == 0:
               print "EncryptAction OK"
               return True
            else:
               print "EncryptAction False"
               return False
         elif ipaddr == '10.95.27.75':
            x = os.system('start "" /d "C:\\DLP\\autoit" "C:\\DLP\\autoit\\EncryptAction.exe" %s' %param)
            if x == 0:
               print "EncryptAction OK"
               return True
            else:
               print "EncryptAction False"
               return False
         elif ipaddr == '10.95.27.77':
            x = os.system('start "" /d "C:\\DLP\\autoit" "C:\\DLP\\autoit\\EncryptAction.exe" %s' %param)
            if x == 0:
               print "EncryptAction OK"
               return True
            else:
               print "EncryptAction False"
               return False
         elif ipaddr == '10.95.27.80':
            x = os.system('start "" /d "D:\\DLP\\autoit" "D:\\DLP\\autoit\\EncryptAction.exe" %s' %param)
            if x == 0:
               print "EncryptAction OK"
               return True
            else:
               print "EncryptAction False"
               return False
         elif ipaddr == '10.95.27.83':
            x = os.system('start "" /d "C:\\DLP\\autoit" "C:\\DLP\\autoit\\EncryptAction.exe" %s' %param)
            if x == 0:
               print "EncryptAction OK"
               return True
            else:
               print "EncryptAction False"
               return False
         elif ipaddr == '10.95.27.79':
            x = os.system('start "" /d "C:\\DLP\\autoit" "C:\\DLP\\autoit\\EncryptAction.exe" %s' %param)
            if x == 0:
               print "EncryptAction OK"
               return True
            else:
               print "EncryptAction False"
               return False
         elif ipaddr == '172.24.83.62':
            x = os.system('start "" /d "D:\\DLP\\autoit" "D:\\DLP\\autoit\\EncryptAction.exe" %s' %param)
            if x == 0:
               print "EncryptAction OK"
               return True
            else:
               print "EncryptAction False"
               return False
         else:
         	print(u"非法IP地址,默认按照D盘路径执行,请测试人员确认!")
         	x = os.system('start "" /d "D:\\DLP\\autoit" "D:\\DLP\\autoit\\EncryptAction.exe" %s' %param)
         	if x == 0:
         		print "EncryptAction OK"
         		return True
         	else:
         		print "EncryptAction False"
         		return False
            #sys.exit(2)     
      except Exception,e:
         print e
         print "EncryptAction False"
         return False
      return
   def PortIsOpen(self,ip,port):
      s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      try:
         s.connect((ip,int(port)))
         s.shutdown(2)
         print '%d is open' % port
         return True
      except:
         print '%d is down' % port
         return False
   def GetVol(self):
      vol = "D"
      valuesC = []
      valuesD = []
      cf = ConfigParser.ConfigParser()
      cf.read("conf/endpoint.ini")
      hostname = socket.getfqdn(socket.gethostname())
      ipaddr = socket.gethostbyname(hostname)
      opts_ipC = cf.options("ipC")
      kvs_ipC = cf.items("ipC")
      opts_ipD = cf.options("ipD")
      kvs_ipD = cf.items("ipD")

      for opts in opts_ipC:
         value = cf.get("ipC", opts)
         valuesC.insert(1,value)
      #print valuesC

      for opts in opts_ipD:
         value = cf.get("ipD", opts)
         valuesD.insert(1,value)
      #print valuesD

      if ipaddr in valuesC:
         vol = "C"
         return vol
      elif ipaddr in valuesD:
         vol = "D"
         return vol
      else:
         print(u"非法IP地址,默认按照D盘处理，请测试人员确认!")
         vol = "D"
         return vol
         #sys.exit(2)
      return vol
 
   def window_capture(self):
      ''''' 
      截屏函数,调用方法window_capture('d:\\') ,参数为指定保存的目录 
      返回图片文件名,文件名格式:日期.jpg 如:2009328224853.jpg 
      ''' 
      c = control()
      hwnd = 0
      dpath = c.GetVol() + ':\\DLP\\Result\\'
      hwndDC = win32gui.GetWindowDC(hwnd)
      mfcDC=win32ui.CreateDCFromHandle(hwndDC)
      saveDC=mfcDC.CreateCompatibleDC()
      saveBitMap = win32ui.CreateBitmap()
      MoniterDev=win32api.EnumDisplayMonitors(None,None)
      w = MoniterDev[0][2][2]
      h = MoniterDev[0][2][3]
      #print w,h　　　＃图片大小
      saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
      saveDC.SelectObject(saveBitMap)
      saveDC.BitBlt((0,0),(w, h) , mfcDC, (0,0), win32con.SRCCOPY)
      cc=time.gmtime()
      bmpname=str(cc[0])+str(cc[1])+str(cc[2])+str(cc[3]+8)+str(cc[4])+str(cc[5])+'_WindowsCapture'+'.bmp'
      saveBitMap.SaveBitmapFile(saveDC, bmpname)
      Image.open(bmpname).save(bmpname[:-4]+".jpg")
      os.remove(bmpname)
      jpgname=bmpname[:-4]+'.jpg'
      djpgname=dpath+jpgname  
      copy_command = "move %s %s" % (jpgname, djpgname)
      os.popen(copy_command)
      return True

   def GenImage(self):
      c = control()
      debug = False
      cc = time.gmtime()
      jpgname = str(cc[0])+str(cc[1])+str(cc[2])+str(cc[3]+8)+str(cc[4])+str(cc[5])+'_ImageGrabCapture'+'.jpg'
      for i in range(10):
         img = ImageGrab.grab(bbox=(250, 161, 1641, 1024))
         img.save('Result\\%s' % jpgname , 'jpeg')
         #img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3) 
      return True
   def WechatCapture(self):
      sysstr = platform.architecture()
      if sysstr[0] == '64bit':
         print u"暂不支持64位系统"
         return False
      else:     
         try:
            dll = ctypes.cdll.LoadLibrary("lib\\PrScrn.dll")
         except Exception as e:
            print("Dll load error!")
            return
         else:
            try:
               dll.PrScrn(0)
            except Exception as e:
               print("Sth wrong in capture!")
               return
         return True
   def QQCapture(self):
      sysstr = platform.architecture()
      if sysstr[0] == '64bit':
         print u"暂不支持64位系统"
         return False
      else:  
         try:
            dll = ctypes.cdll.LoadLibrary("lib\\CameraDll.dll")
         except Exception as e:
            print("Dll load error!")
            return
         else:
            try:
               dll.CameraSubArea(0)
            except Exception as e:
               print("Sth wrong in capture!")
               return True
         return True
   def genfaker(self,num):
      faker = Faker("zh_CN")
      file = 'Result\\card.txt'
      if os.path.exists(file):
         os.remove(file)
         pass
      f = open('Result\\card.txt','a')
      i = 0
      while(i < num):
         #f.writelines("姓名: ")
         #f.writelines(faker.name())
         #f.writelines("\n")
         f.writelines("电话号码: ")
         f.writelines(faker.phone_number())
         f.writelines("\n")
         f.writelines("18位身份证号: ")
         f.writelines(faker.ssn())
         f.writelines("\n")
         f.writelines("信用卡卡号: ")
         f.writelines(faker.credit_card_number(card_type=None))
         #f.writelines("\n")
         #f.writelines("地址: ")
         #f.writelines(faker.address())
         f.writelines("\n----------------------------------------\n")
         #f.writelines(["phone: " + faker.phone_number() + "\n","user sn: " + faker.ssn() + "\n","bank card: " + faker.credit_card_number(card_type=None) + "\n"])
         i = i + 1
      f.close()
      return True
if __name__ == "__main__":
    app = control()
    def usage():
        print(u'\
        -h or --help：显示帮助信息\n\
        -v or --version：显示版本\
        ')
    if len(sys.argv) == 1:
        usage()
        sys.exit()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "h123456v", ["help","version"])
    except getopt.GetoptError:
        print("argv error,please input")

    for cmd, arg in opts:
        if cmd in ("-h", "--help"):
            usage()
        elif cmd in ("-1", "--get"):
            app.post_http_content_pass()
        elif cmd in ("-2", "--get"):
            app.post_http_content_refuse()
        elif cmd in ("-3", "--get"):
            filename = "file\SN.txt"
            ip = "10.95.41.15"
            port = "8000"
            app.post_http_file_pass(ip,port,filename)
        elif cmd in ("-4", "--get"):
            filename = "file\SN.txt"
            ip = "10.95.41.15"
            port = "8000"
            app.post_http_file_refuse(ip,port,filename)
        elif cmd in ("-5", "--get"):
            #app.window_capture()
            #time.sleep(3)
            #app.GenImage()
            app.sftp_up()
        elif cmd in ("-6", "--get"):
            #app.window_capture()
            #time.sleep(3)
            #app.GenImage()
            app.genfaker(10)
        elif cmd in ("-v", "--version"):
            print("version 1.0")
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import urllib
import urllib2
import base64
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

class HTTPSConnectionV3(httplib.HTTPSConnection):
   def __init__(self,*args,**kwargs):
      httplib.HTTPSConnection.__init__(self,*args,**kwargs)
         
   def connect(self):
      sock= socket.create_connection((self.host,self.port),self.timeout)
      if self._tunnel_host:
         self.sock= sock
         self._tunnel()
      try:
         self.sock= ssl.wrap_socket(sock,self.key_file,self.cert_file,ssl_version=ssl.PROTOCOL_SSLv1)
      except ssl.SSLError,e:
         print("TryingSSLv1.")
         self.sock= ssl.wrap_socket(sock,self.key_file,self.cert_file,ssl_version=ssl.PROTOCOL_SSLv1)

class HTTPSHandlerV3(urllib2.HTTPSHandler):
   def https_open(self,req):
      return self.do_open(HTTPSConnectionV1,req)
      #install opener
      urllib2.install_opener(urllib2.build_opener(HTTPSHandlerV3()))

'''
class MyAdapter(HTTPAdapter):
   def init_poolmanager(self,connections, maxsize):
      self.poolmanager= PoolManager(num_pools=connections,maxsize=maxsize,ssl_version=ssl.PROTOCOL_SSLv3)
'''
class HTTPSControl:
   def https(self):
      ret=True
      try:      
         #定义一个要提交的数据数组(字典)
         context = ssl._create_unverified_context()
         url = 'https://10.95.41.15/php/post.php'
         headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
         request = urllib2.Request(url, headers = headers)
         data = {}
         data['contents'] = 'wangbaoqiang王宝强'
         #data['fileImage'] = '123456' 
         #定义post的地址
         post_data = urllib.urlencode(data)
         #提交，发送数据
         req = urllib2.urlopen(url, post_data,context = context)
         #获取提交后返回的信息
         content = req.read()
         #return content
         print "https upload OK"
         return ret   
      except Exception,e:
         print e
         print "https upload False"
         return False
   def httpsSLL(self):
      ret=True
      try:      
         #定义一个要提交的数据数组(字典)
         context = ssl._create_unverified_context()
         url = 'https://10.95.27.121'
         #提交，发送数据
         req = urllib2.urlopen(url)
         #获取提交后返回的信息
         content = req.read()
         #return content
         return ret
      except Exception,e:
         print e
         return ret
   #模拟HTTP提交file
   def post_https_file(self,filename):
      ret=True
      try:
         context = ssl._create_unverified_context()
         data = []
         boundary = '----------%s' % hex(int(time.time() * 1000))
         data.append('--%s' % boundary)

         url = "https://%s:%s/upload_file.php" % ('10.95.41.15', '443')

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
         req.add_header('Referer','http://10.95.41.15/')
         #post data to server
         resp = urllib2.urlopen(req, timeout=5,context = context)
         #get response
         qrcont=resp.read()
         #print qrcont
         print "https upload file OK"
         return ret
      except Exception as e:
         #print(": unable to send URL: {0}".format(e))
         print "https upload file False"
         return False
      return

if __name__ == "__main__":
   #r = urllib2.urlopen("https://10.95.41.15")
   #print(r.read())
   filename = "D:\\DLP\\file\\SN.txt"
   r = HTTPSControl()
   r.httpsSLL()
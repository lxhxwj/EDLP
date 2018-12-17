#!/usr/bin/python
# -*- coding: UTF-8 -*-

import win32com.client as win32
import win32api
import os
import time
import socket

class defOutlook:
	def outlook(self):
		ret = True
		try:
			win32api.ShellExecute(0,'open',r'C:\Program Files\Microsoft Office\Office14\OUTLOOK.EXE','','',1)
			time.sleep(5)
			outlook = win32.Dispatch('outlook.application')
			mail = outlook.CreateItem(0)
			mail.To = 'test02@360gtb.com'
			mail.Subject = u'张秀昌发送的带附件的测试邮件'
			mail.Body = u'王宝强先生！恭喜您查收到该邮件'
			mail.HTMLBody = u'<h1 style="text-algin:center">王宝强先生！恭喜您查收到该邮件</h1><span style="color:red">详情如下：</span><br><img src="cid:zg">' #this field is optional
			# To attach a file to the email (optional):
			#attachment  = 'menu.py'
			#mail.Attachments.Add(attachment)
			mail.Send()
			time.sleep(5)
			os.system("taskkill /F /IM OUTLOOK.EXE")
			print "OUTLOOK OK" 
			return ret
		except Exception,e:
			print e
			print "OUTLOOK False" 
			return False
		return

	def get_host_ip(self):
		"""
		查询本机ip地址
		:return: ip
		"""
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect(('8.8.8.8', 80))
			ip = s.getsockname()[0]
		finally:
			s.close()
		return ip


if __name__ == "__main__":
	app = defOutlook()

	app.get_host_ip()
	print socket.gethostname()
	app.outlook()
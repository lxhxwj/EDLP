#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import getopt
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


class WebDLP(object):
	def InitDriver(self):
		driver = webdriver.Firefox(executable_path="./geckodriver")
		return driver

	def WebLogin(self,ip,username,password):
		#driver = webdriver.Firefox(executable_path="./geckodriver")
		driver = WebDLP().InitDriver()
		#driver.maximize_window()
		#sleep(3)
		#driver.set_window_size(480, 760)
		driver.get('http://%s:8080' % ip)
		cookie1 = driver.get_cookies()
		#print cookie1
		sleep(3)
		elem = driver.find_element_by_xpath('//*[@id="username"]')
		elem.clear()
		elem.send_keys(username)
		elem = driver.find_element_by_xpath('//*[@id="userpass"]')
		elem.clear()
		elem.send_keys(password)
		elem = driver.find_element_by_xpath('//*[@id="login"]')
		elem.send_keys(Keys.ENTER)
		cookie2 = driver.get_cookies()
		#print cookie2
		sleep(5)
		driver.quit()

	def WebCreatePolicy(self,ip,username,password,name,num):
		#driver = webdriver.Firefox(executable_path="./geckodriver")
		driver = WebDLP().InitDriver()
		#driver.maximize_window()
		#sleep(3)
		#driver.set_window_size(480, 760)
		driver.get('http://%s:8080' % ip)
		cookie1 = driver.get_cookies()
		#print cookie1
		sleep(3)
		elem = driver.find_element_by_xpath('//*[@id="username"]')
		elem.clear()
		elem.send_keys(username)
		elem = driver.find_element_by_xpath('//*[@id="userpass"]')
		elem.clear()
		elem.send_keys(password)
		elem = driver.find_element_by_xpath('//*[@id="login"]')
		elem.send_keys(Keys.ENTER)
		cookie2 = driver.get_cookies()
		#print cookie2
		sleep(15)
		driver.get('http://%s:8080/dlp/library/keyword#gid=0' % ip)
		sleep(15)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div[1]/a[1]').click()
		sleep(3)
		elem = driver.find_element_by_xpath('//*[@id="keywordName"]')
		elem.clear()
		elem.send_keys(name)
		sleep(3)
		elem = driver.find_element_by_xpath('//*[@id="keywordDesc"]')
		elem.clear()
		elem.send_keys(name)
		sleep(3)
		s1 = Select(driver.find_element_by_id('keywordDensity'))
		s1.select_by_value("15")
		sleep(3)
		elem = driver.find_element_by_xpath('//*[@id="keyword"]')
		elem.clear()
		elem.send_keys(name)
		sleep(3)
		elem = driver.find_element_by_xpath('//*[@id="weight"]')
		elem.clear()
		elem.send_keys(num)
		sleep(3)
		driver.find_element_by_xpath('//*[@id="btnNewKeyword"]').click()
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/button[1]').click()
		sleep(5)
		driver.quit()

	def WebCreatePolicyGroup(self,ip,username,password,name):
		#driver = webdriver.Firefox(executable_path="./geckodriver")
		driver = WebDLP().InitDriver()
		#driver.maximize_window()
		#sleep(3)
		#driver.set_window_size(480, 760)
		driver.get('http://%s:8080' % ip)
		cookie1 = driver.get_cookies()
		#print cookie1
		sleep(3)
		elem = driver.find_element_by_xpath('//*[@id="username"]')
		elem.clear()
		elem.send_keys(username)
		elem = driver.find_element_by_xpath('//*[@id="userpass"]')
		elem.clear()
		elem.send_keys(password)
		elem = driver.find_element_by_xpath('//*[@id="login"]')
		elem.send_keys(Keys.ENTER)
		cookie2 = driver.get_cookies()
		#print cookie2
		sleep(15)
		driver.get('http://%s:8080/dlp/librarycombo/tpl#tplId=8' % ip)
		sleep(15)
		#点击新建模板
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/a').click()
		sleep(3)
		elem = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/div/p[1]/input')
		elem.clear()
		elem.send_keys(name)
		sleep(3)
		s1 = Select(driver.find_element_by_id('base-tpl'))
		s1.select_by_value("0")
		#点击确认
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[3]/button[1]').click()
		#选择感知库规则
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[1]/ul/li[2]').click()
		#点击添加感知库规则
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/fieldset/div[1]/button').click()
		#新建感知库规则，关键字
		#选择类型
		sleep(3)
		s1 = Select(driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/fieldset/div[3]/div/div[2]/div/fieldset/label/select'))
		s1.select_by_value("2")
		#输入名称
		sleep(3)
		elem = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/fieldset/div[3]/div/div[2]/div/fieldset/div[1]/input')
		elem.clear()
		elem.send_keys(name)
		#勾选统计重复内容
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/fieldset/div[3]/div/div[2]/div/fieldset/div[2]/div[1]/p[1]/label/input').click()
		#勾选区分大小写
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/fieldset/div[3]/div/div[2]/div/fieldset/div[2]/div[1]/p[2]/label/input').click()
		#点击确认
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/fieldset/div[3]/div/div[3]/button[1]').click()
		#点击保存
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[2]/button').click()
		#返回基本设置
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[1]/ul/li[1]').click()
		#点击发布
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/table/tr[3]/td/button[1]').click()
		#点击确认
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/div[3]/div/div[3]/button[1]').click()


		sleep(5)
		driver.close()
		#driver.quit()

	def WebDLPTemplate(self,ip,username,password,name):
		#driver = webdriver.Firefox(executable_path="./geckodriver")
		driver = WebDLP().InitDriver()
		#driver.maximize_window()
		#sleep(3)
		#driver.set_window_size(480, 760)
		driver.get('http://%s:8080' % ip)
		cookie1 = driver.get_cookies()
		#print cookie1
		sleep(3)
		elem = driver.find_element_by_xpath('//*[@id="username"]')
		elem.clear()
		elem.send_keys(username)
		elem = driver.find_element_by_xpath('//*[@id="userpass"]')
		elem.clear()
		elem.send_keys(password)
		elem = driver.find_element_by_xpath('//*[@id="login"]')
		elem.send_keys(Keys.ENTER)
		cookie2 = driver.get_cookies()
		#print cookie2
		sleep(15)
		driver.get('http://%s:8080/dlp/chanlprotecttpl/combo#tplId=1' % ip)
		sleep(15)
		#点击新建模板
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[1]/a').click()
		sleep(3)
		elem = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/div/p[1]/input')
		elem.clear()
		elem.send_keys(name)
		sleep(3)
		s1 = Select(driver.find_element_by_id('base-tpl'))
		s1.select_by_value("0")
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div[3]/button[1]').click()
		
		#选择DLP防护页
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/ul/li[3]').click()
		#配置DLP模板
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[1]/h4/label[1]/input').click()
		#勾选HTTP
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[1]/div[2]/label[1]/input').click()
		#勾选HTTPS
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[1]/div[2]/label[2]/input').click()
		#勾选FTP
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[1]/div[2]/label[3]/input').click()
		#勾选SMTP
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[1]/div[2]/label[4]/input').click()
		#勾选移动存储
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[1]/div[2]/label[5]/input').click()
		#勾选网络共享
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[1]/div[2]/label[6]/input').click()
		#勾选蓝牙
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[1]/div[2]/label[7]/input').click()
		#勾选打印
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[1]/div[2]/label[8]/input').click()
		#内容识别，选择策略
		#sleep(3)
		#driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[2]/div[2]/div/div/div/button').click()
		#响应动作，核心商密选择用户确认
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[3]/div[2]/div/table/tbody/tr[1]/td[4]/input').click()
		#高级模式
		#勾选未知协议
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[1]/div[2]/label[1]/input').click()
		#勾选内容拖拽
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[1]/div[2]/label[2]/input').click()
		#勾选剪切板
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[1]/div[2]/label[3]/input').click()
		#勾选Outlook控制
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[1]/div[2]/label[4]/input').click()
		#选择双向SSL传输，审计传输地址
		sleep(3)
		s1 = Select(driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[1]/div[2]/label[5]/select'))
		s1.select_by_value("2")
		#选择SSH通道传输，审计传输地址
		sleep(3)
		s2 = Select(driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[1]/div[2]/label[6]/select'))
		s2.select_by_value("2")
		#功能控制
		#选择受限文件，用户确认
		sleep(3)
		s3 = Select(driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[2]/div[2]/label[1]/select'))
		s3.select_by_value("3")
		#选择文件检测，文件名+文件内容
		sleep(3)
		s4 = Select(driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[2]/div[2]/label[2]/select'))
		s4.select_by_value("3")
		#勾选上传证据文件
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[2]/div[2]/label[3]/input').click()
		#勾选检测系统磁盘之外的本地磁盘
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[2]/div[2]/label[4]/input').click()
		#图像文字识别
		#勾选启动文字识别
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[3]/div[2]/span/label/input').click()
		#应用程序控制
		#勾选即时消息（IM）
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[4]/div[2]/div/div[1]/label/input').click()
		#全部选择即时消息应用
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[4]/div[2]/div/div[1]/fieldset/div/div[3]/label/input').click()
		#文件访问控制
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[4]/div[2]/div/div[2]/label/input').click()
		#全部选择文件访问控制应用
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[4]/div[2]/div/div[2]/fieldset/div/div[3]/label/input').click()
		#CD-ROM
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[4]/div[2]/div/div[3]/label/input').click()
		#全部选择CD-ROM应用
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[4]/div[2]/div/div[3]/fieldset/div/div[3]/label/input').click()
		#点击保存
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/button').click()
		#返回基本设置
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/ul/li[1]').click()
		#点击发布
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/table/tr[3]/td/button[1]').click()
		#点击确认
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/div[3]/div/div[3]/button[1]').click()


		sleep(5)
		driver.close()		
		#driver.quit()

	def WebTest(self,ip,username,password,name):
		#driver = webdriver.Firefox(executable_path="./geckodriver")
		driver = WebDLP().InitDriver()
		#driver.maximize_window()
		#sleep(3)
		#driver.set_window_size(480, 760)
		driver.get('http://%s:8080' % ip)
		cookie1 = driver.get_cookies()
		#print cookie1
		sleep(3)
		elem = driver.find_element_by_xpath('//*[@id="username"]')
		elem.clear()
		elem.send_keys(username)
		elem = driver.find_element_by_xpath('//*[@id="userpass"]')
		elem.clear()
		elem.send_keys(password)
		elem = driver.find_element_by_xpath('//*[@id="login"]')
		elem.send_keys(Keys.ENTER)
		cookie2 = driver.get_cookies()
		#print cookie2
		sleep(15)
		driver.get('http://%s:8080/dlp/chanlprotecttpl/combo#tplId=1' % ip)
		sleep(15)



		def NewTemplate():
			
			#点击新建模板
			driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[1]/a').click()
			sleep(3)
			elem = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/div/p[1]/input')
			elem.clear()
			elem.send_keys(name)
			sleep(3)
			s1 = Select(driver.find_element_by_id('base-tpl'))
			s1.select_by_value("0")
			sleep(3)
			driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div[3]/button[1]').click()

			#选择DLP防护页
			sleep(3)
			driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/ul/li[2]').click()
			#配置DLP模板
			sleep(3)
			driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[1]/h4/label[1]/input').click()
		

			#内容识别，选择策略
			sleep(3)
			driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[2]/div[2]/div/div/div/button').click()
		
			#获取策略table数据，增加判断
			sleep(3)
			t = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[2]')
			keyword = t.get_attribute('title')
			#内容识别，选择策略
			if keyword == name:
				sleep(3)
				driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[1]/input').click()
			else:
				sleep(3)
				driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/table/tbody/tr[2]/td[1]/input').click()			

			'''
			#点击保存
			sleep(3)
			driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/button').click()
			#返回基本设置
			sleep(3)
			driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/ul/li[1]').click()
			#点击发布
			sleep(3)
			driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/table/tr[3]/td/button[1]').click()
			#点击确认
			sleep(3)
			driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/div[3]/div/div[3]/button[1]').click()
			'''



		#获取策略ul数据，增加判断
		sleep(3)
		ul = [el.text for el in driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul")]
		for li in ul:
			print li
		#内容识别，选择策略
		sleep(15)
		if li != name:
			sleep(3)
			driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[2]/span[1]').click()
			sleep(3)
			with open('http://10.95.27.118:8080/res/build/dlp/ChanlProtectCombo.js', 'r') as jquery_js: 
				jquery = jquery_js.read()
				driver.execute_script(jquery)
				driver.execute_script('$("#apply").click()')
			#driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/table/tr[3]/td/button[2]').click()
			sleep(3)
			driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/div[3]/div/div[3]/button[1]').click()
			sleep(3)
			driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[2]/i').click()
			sleep(3)
			driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div[3]/button[1]').click()
		else:
			NewTemplate()


		
		sleep(5)
		driver.close()		
		#driver.quit()

	def WebAddAuthGroup(self,ip,username,password,i):
		#driver = webdriver.Firefox(executable_path="./geckodriver")
		driver = WebDLP().InitDriver()
		#driver.maximize_window()
		#sleep(3)
		#driver.set_window_size(480, 760)
		driver.get('http://%s:8080' % ip)
		cookie1 = driver.get_cookies()
		#print cookie1
		sleep(3)
		elem = driver.find_element_by_xpath('//*[@id="username"]')
		elem.clear()
		elem.send_keys(username)
		elem = driver.find_element_by_xpath('//*[@id="userpass"]')
		elem.clear()
		elem.send_keys(password)
		elem = driver.find_element_by_xpath('//*[@id="login"]')
		elem.send_keys(Keys.ENTER)
		cookie2 = driver.get_cookies()
		#print cookie2
		sleep(15)
		driver.get('http://%s:8080/dlp/library/encryptauthorize' % ip)
		sleep(15)


		#点击添加
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div[1]/button[1]').click()
		#添加名称
		sleep(3)
		elem = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div[3]/div/div[2]/p[1]/input')
		elem.clear()
		elem.send_keys(u'王宝强123456789%s' % i)
		#添加描述
		sleep(3)
		elem = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div[3]/div/div[2]/p[2]/textarea')
		elem.clear()
		elem.send_keys(u'王宝强123456789')
		#点击组织架构
		sleep(3)
		driver.find_element_by_xpath('//*[@id="gid-0"]/span').click()
		#搜索用户
		sleep(3)
		elem = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div[3]/div/div[2]/div/section[3]/div[1]/input')
		elem.clear()
		elem.send_keys('nacwin8164')
		#点击搜索按钮
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div[3]/div/div[2]/div/section[3]/div[1]/button').click()
		#点击添加
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div[3]/div/div[2]/div/section[3]/div[2]/div[2]/table/tbody/tr[1]/td[3]/span').click()
		#点击保存按钮
		sleep(3)
		driver.find_element_by_xpath('//*[@id="send-button"]').click()

		sleep(5)
		#driver.close()
		driver.quit()


	def WebDiscvry(self,ip,username,password,name):
		#driver = webdriver.Firefox(executable_path="./geckodriver")
		driver = WebDLP().InitDriver()
		#driver.maximize_window()
		#sleep(3)
		#driver.set_window_size(480, 760)
		driver.get('http://%s:8080' % ip)
		cookie1 = driver.get_cookies()
		#print cookie1
		sleep(3)
		elem = driver.find_element_by_xpath('//*[@id="username"]')
		elem.clear()
		elem.send_keys(username)
		elem = driver.find_element_by_xpath('//*[@id="userpass"]')
		elem.clear()
		elem.send_keys(password)
		elem = driver.find_element_by_xpath('//*[@id="login"]')
		elem.send_keys(Keys.ENTER)
		cookie2 = driver.get_cookies()
		#print cookie2
		sleep(15)
		driver.get('http://%s:8080/dlp/datadiscvryindex/tpl' % ip)
		sleep(15)
		#点击新建模板
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[1]/a').click()
		sleep(3)
		elem = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/div/p[1]/input')
		elem.clear()
		elem.send_keys(name)
		sleep(3)
		s1 = Select(driver.find_element_by_id('base-tpl'))
		s1.select_by_value("0")
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div[3]/button[1]').click()
		


		#配置发现目标
		#输入要包含的文件路径
		sleep(3)
		elem = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div[2]/div[2]/fieldset[1]/div/textarea')
		elem.clear()
		elem.send_keys(u"D:\DLP\file")
		#输入要排除的文件路径
		sleep(3)
		elem = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div[2]/div[2]/fieldset[2]/div/textarea')
		elem.clear()
		elem.send_keys(u"D:\DLP\file\install")
		#文件属性
		#输入要包含的文件扩展名
		sleep(3)
		elem = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div/div/div[2]/div[2]/div[2]/fieldset[1]/div/textarea')
		elem.clear()
		elem.send_keys(u"docx;txt;doc;zip;xlsx")
		#输入要排除的文件扩展名
		sleep(3)
		elem = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div/div/div[2]/div[2]/div[2]/fieldset[2]/div/textarea')
		elem.clear()
		elem.send_keys(u"pdf;pptx")
		#处理选项
		#处理方式-选择审计
		sleep(3)
		s1 = Select(driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div/div/div[3]/div[2]/span[1]/label/select'))
		s1.select_by_value("4")
		#文件检测-选择文件名+文件内容
		sleep(3)
		s1 = Select(driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div/div/div[3]/div[2]/span[2]/label/select'))
		s1.select_by_value("3")
		#内容识别
		#点击编辑
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div/div/div[4]/div[2]/div/div/div/button').click()

		
		#内容识别，选择策略
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[2]/div[2]/div/div/div/button').click()
		
		#获取策略table数据，增加判断
		sleep(3)
		t = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[2]')
		keyword = t.get_attribute('title')
		#内容识别，选择策略
		if keyword == name:
			sleep(3)
			driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[1]/input').click()
		else:
			sleep(3)
			driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/table/tbody/tr[2]/td[1]/input').click()			


		'''
		#选择DLP防护页
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/ul/li[2]').click()
		#配置DLP模板
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[1]/h4/label[1]/input').click()
		#勾选HTTP
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[1]/div[2]/label[1]/input').click()
		#勾选HTTPS
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[1]/div[2]/label[2]/input').click()
		#勾选FTP
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[1]/div[2]/label[3]/input').click()
		#勾选SMTP
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[1]/div[2]/label[4]/input').click()
		#勾选移动存储
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[1]/div[2]/label[5]/input').click()
		#勾选网络共享
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[1]/div[2]/label[6]/input').click()
		#勾选蓝牙
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[1]/div[2]/label[7]/input').click()
		#勾选打印
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[1]/div[2]/label[8]/input').click()
		#内容识别，选择策略
		#sleep(3)
		#driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[2]/div[2]/div/div/div/button').click()
		#响应动作，核心商密选择用户确认
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/div[3]/div[2]/div/table/tbody/tr[1]/td[4]/input').click()
		#高级模式
		#勾选未知协议
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[1]/div[2]/label[1]/input').click()
		#勾选内容拖拽
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[1]/div[2]/label[2]/input').click()
		#勾选剪切板
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[1]/div[2]/label[3]/input').click()
		#勾选Outlook控制
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[1]/div[2]/label[4]/input').click()
		#选择双向SSL传输，审计传输地址
		sleep(3)
		s1 = Select(driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[1]/div[2]/label[5]/select'))
		s1.select_by_value("2")
		#选择SSH通道传输，审计传输地址
		sleep(3)
		s2 = Select(driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[1]/div[2]/label[6]/select'))
		s2.select_by_value("2")
		#功能控制
		#选择受限文件，用户确认
		sleep(3)
		s3 = Select(driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[2]/div[2]/label[1]/select'))
		s3.select_by_value("3")
		#选择文件检测，文件名+文件内容
		sleep(3)
		s4 = Select(driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[2]/div[2]/label[2]/select'))
		s4.select_by_value("3")
		#勾选上传证据文件
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[2]/div[2]/label[3]/input').click()
		#勾选检测系统磁盘之外的本地磁盘
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[2]/div[2]/label[4]/input').click()
		#图像文字识别
		#勾选启动文字识别
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[3]/div[2]/span/label/input').click()
		#应用程序控制
		#勾选即时消息（IM）
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[4]/div[2]/div/div[1]/label/input').click()
		#全部选择即时消息应用
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[4]/div[2]/div/div[1]/fieldset/div/div[3]/label/input').click()
		#文件访问控制
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[4]/div[2]/div/div[2]/label/input').click()
		#全部选择文件访问控制应用
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[4]/div[2]/div/div[2]/fieldset/div/div[3]/label/input').click()
		#CD-ROM
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[4]/div[2]/div/div[3]/label/input').click()
		#全部选择CD-ROM应用
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/fieldset[2]/fieldset/div[4]/div[2]/div/div[3]/fieldset/div/div[3]/label/input').click()
		#点击保存
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/button').click()
		#返回基本设置
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/ul/li[1]').click()
		#点击发布
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/table/tr[3]/td/button[1]').click()
		#点击确认
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/div[3]/div/div[3]/button[1]').click()

		'''
		sleep(5)
		driver.close()		
		#driver.quit()


if __name__ == '__main__':
	web = WebDLP()

	username = "admin"
	password = "www.360.cn"
	name = u"王宝强123456789"
	num = 1
	ip = '10.95.27.118'

	def usage():
		print(u'\
			-h ：显示帮助信息\n\
			-l ：登录控制台\n\
			-c ：创建关键字感知库\n\
			-g ：创建感知库模板\n\
			-t ：创建DLP策略模板\n\
			-T ：调试代码，勿使用\n\
			-a ：创建加密授权虚拟组\n\
			-d ：创建数据发现模板\n\
			-v ：显示版本\
			')

	if len(sys.argv) == 1:
		usage()
		sys.exit()

	try:
		opts, args = getopt.getopt(sys.argv[1:], "hlcgtTadv", ["help", "output="])
	except getopt.GetoptError:
		usage()        
	for cmd, arg in opts:
		if cmd in ("-h", "--help"):
			usage()
		elif cmd in ("-l", "1"):
			web.WebLogin(ip,username,password)
		elif cmd in ("-c", "1"):
			web.WebCreatePolicy(ip,username,password,name,num)
		elif cmd in ("-g", "1"):
			web.WebCreatePolicyGroup(ip,username,password,name)
		elif cmd in ("-t", "1"):
			web.WebDLPTemplate(ip,username,password,name)
		elif cmd in ("-T", "1"):
			web.WebTest(ip,username,password,name)
		elif cmd in ("-a", "1"):
			i = 1
			web.WebAddAuthGroup(ip,username,password,i)
		elif cmd in ("-d", "1"):
			web.WebDiscvry(ip,username,password,name)
		elif cmd in ("-v", "--version"):
			print("version 1.0")

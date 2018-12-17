#!/usr/bin/python
# -*- coding: UTF-8 -*-


from pywinauto import application
import SendKeys
import time
import os


class Pywin(object):

	SLEEP_TIME = 1

	def __init__(self):
		self.app = application.Application()


	def run(self, tool_name):
		self.app.start_(tool_name)
        time.sleep(1)
	
	def connect(self, window_name):
		self.app.connect_(title = window_name)
    	time.sleep(1)

	def close(self, window_name):
		self.app[window_name].Close()
		time.sleep(1)
	
	def max_window(self, window_name):
		self.app[window_name].Maximize()
        time.sleep(1)


	def menu_click(self, window_name, menulist):
		self.app[window_name].MenuSelect(menulist)
		time.sleep(1)

	def input(self, window_name, controller, content):
		self.app[window_name][controller].TypeKeys(content)
		time.sleep(1)
	
	def click(self, window_name, controller):
		self.app[window_name][controller].Click()
		time.sleep(1)

	def double_click(self, window_name, controller, x = 0,y = 0):
		self.app[window_name][controller].DoubleClick(button = "left", pressed = "",  coords = (x, y))
		time.sleep(1)

	def right_click(self, window_name, controller, order):
		self.app[window_name][controller].RightClick()
		for down in range(order):
			SendKeys.SendKeys('{DOWN}')
			time.sleep(0.5)
		SendKeys.SendKeys('{ENTER}')
		time.sleep(1)


if __name__ ==  "__main__":
	app = Pywin()

	tool_name = "NOTEPAD.EXE"

	window_name = u"无标题 - 记事本"	
	menulist = u"帮助->关于记事本"

	controller = "Edit"
	content = u"johnny"
	window_name_new = content + ".txt"

	#app.run(tool_name)
	os.popen('NOTEPAD.EXE')

	#app.connect(window_name)
	#app.max_window(window_name)
	#app.menu_click(window_name,menulist)
	app.click(u'关于记事本', u'确定')
	app.input(window_name,controller,content)
	app.input(window_name,controller,"^a")
	app.right_click(window_name,controller,3)
	app.right_click(window_name,controller,4)
	SendKeys.SendKeys('{ENTER}')
	app.input(window_name,controller,"^v")
	app.input(window_name,controller,"^s")
	app.input(u"另存为",controller,content)
	app.click(u"另存为","Button")
	try:
		app.click(u"确认另存为","Button")
	except:
		pass
	finally:
		app.close(window_name_new)
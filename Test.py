#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
from office import office
import getopt
from socket import *
import wmi
#import AutoItLibrary
import pymssql
class Window:
	def autoitTEST(self):
		AutoItLibrary.run('notepad.exe')
	def disk(self):
		c = wmi.WMI()
		for physical_disk in c.Win32_DiskDrive():
			for partition in physical_disk.associators ("Win32_DiskDriveToDiskPartition"):
				for logical_disk in partition.associators ("Win32_LogicalDiskToPartition"):
					print logical_disk.Caption
	def SendMessageForFeiq(self):
		s = socket(AF_INET,SOCK_DGRAM)
		add = ("10.95.27.76",2425)
		a = u"1:525:杨曙光:杨曙光:32:我是王宝强，我无敌!"
		s.sendto(a.encode("gbk"),add)
		s.close()

	def CreateTxtWindow():

		root = Tk()
		#设置标题
		root.title("")
		#设置窗口的大小宽x高+偏移量
		root.geometry('440x30+700+300')
		#禁止调整窗口大小
		#root.resizable(0, 0)
		#设置窗口图标
		#root.iconbitmap('img\mainlogo.ico')

		root.overrideredirect(True) #清除所有的tkinters窗口选项
		#root.attributes('-disabled', True) #防止与窗口中的任何用户交互

		root.wm_attributes('-topmost',1) #置顶窗口


		l1 = Label(root, text="文件行数，不得超过500行:",bg = 'red')
		l1.pack(side=LEFT)
		num1 = StringVar()
		txt1 = Entry(root, width=5,borderwidth=2, textvariable = num1)
		num1.set("50")
		txt1.pack(side=LEFT)


		l2 = Label(root, text="文件个数，不得超过500个:",bg = 'red')
		l2.pack(side=LEFT)
		num2 = StringVar()
		txt2 = Entry(root, width=5,borderwidth=2, textvariable = num2)
		num2.set("1")
		txt2.pack(side=LEFT)


		def on_click():
			ret = True
			o = office()
			x = num1.get()
			y = num2.get()
			if x is not None:
				s = int(x)
				n = int(y)
				if 0 < s <= 500 and 0 < n <= 500:
					ret = o.CreateTxtE(s,n)
					if ret:
						print("OK")
					else:
						print("FALSE")
				else:
					print("最大可设置500")

			root.destroy()
			return True

		Button(root, text="生成文件", command = on_click).pack(side=LEFT)
		    
		root.mainloop()
	def MSSQLCONN(self):
		server = '10.95.41.11'
		user = 'sa'
		password = 'www.360.cn'
		database = 'test'
		conn = pymssql.connect(server, user, password, database)

		cursor = conn.cursor()

		cursor.execute('SELECT * FROM nac_user')
		row = cursor.fetchone()
		while row:
			print("%s, %s" % (row[1], row[2]))
			row = cursor.fetchone()
		conn.close()
if __name__ == "__main__":
    app = Window()
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
            #app.WechatCapture()
            app.autoitTEST()
        elif cmd in ("-6", "--get"):
            app.MSSQLCONN()
        elif cmd in ("-v", "--version"):
            print("version 1.0")
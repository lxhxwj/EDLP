#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import socket
import getopt
import sys
import os
import platform
hostname = socket.getfqdn(socket.gethostname())
ipaddr = socket.gethostbyname(hostname)
if platform.machine() == 'AMD64' and ipaddr == '10.95.41.17':
   from PySTAF import *
   from PySTAFMon import *
   from PySTAFLog import *
reload(sys)
sys.setdefaultencoding('utf-8')


class check:
	def svn_up(self,vol,username,password):
   		ret = True
   		#os.system('net use \\10.95.27.99\IPC$ /del /y')
   		#time.sleep(10)
   		os.system('svn cleanup %s:\\DLP --username %s --password %s --no-auth-cache' % (vol,username,password))
   		time.sleep(10)
   		try:
   			x = os.system('svn update %s:\\DLP --username %s --password %s --no-auth-cache' % (vol,username,password))
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

	def svnC(self,username):
		ret = True
		hostname = socket.getfqdn(socket.gethostname())
		vol = "C"
		password = "admin"
		a = check()
		svn = a.svn_up(vol,username,password)
		if svn == True:
			print("svn update OK")
		else:
			print("svn update FAIL")

	def svnD(self,username):
		ret = True
		hostname = socket.getfqdn(socket.gethostname())
		vol = "D"
		password = "admin"
		a = check()
		svn = a.svn_up(vol,username,password)
		if svn == True:
			print("svn update OK")
		else:
			print("svn update FAIL")

	def checksvn(self):
		username = "luoxianghui"
		username8164 = "win8164"
		username732 = "win732"
		username1064 = "win1064"
		username1032 = "win1032"
		username75 = "zhangji75"
		username77 = "zhangji77"
		username80 = "zhangji80"
		username79 = "zhanglu79"
		username83 = "zhanglu83"
		app = check()
		hostname = socket.getfqdn(socket.gethostname())
		ipaddr = socket.gethostbyname(hostname)
		if ipaddr == '10.95.27.76':
			app.svnD(username8164)
			time.sleep(10)
		elif ipaddr == '10.95.41.20':
			app.svnD(username732)
			time.sleep(10)
		elif ipaddr == '10.95.27.116':
			app.svnD(username1064)
			time.sleep(10)
		elif ipaddr == '10.95.27.74':
			app.svnD(username1032)
			time.sleep(10)
		elif ipaddr == '10.95.41.17':
			app.svnD(username)
			time.sleep(10)
		elif ipaddr == '10.95.27.75':
			app.svnC(username75)
			time.sleep(10)
		elif ipaddr == '10.95.27.77':
			app.svnC(username77)
			time.sleep(10)
		elif ipaddr == '10.95.27.80':
			app.svnD(username80)
			time.sleep(10)
		elif ipaddr == '10.95.27.83':
			app.svnC(username83)
			time.sleep(10)
		elif ipaddr == '10.95.27.79':
			app.svnC(username79)
			time.sleep(10)
		else:
			print(u"非法IP地址,不能在该机器上运行测试，请测试人员确认!")
			sys.exit(2)

class staf:
   def svnupdateSTAF(self,clientip,cmd,user,passwd,remote_temp_dir):
      ret = True
      request = 'start command "%s > svn.log" username "%s" password "%s" workdir "%s"' % (cmd, user, passwd, remote_temp_dir)
      try:
         try:
            handle = STAFHandle("svn")
         except STAFException, e:
            print "Error registering with STAF, RC: %d" % e.rc
            sys.exit(e.rc)

         result = handle.submit(clientip, "process", request)

         if (result.rc != 0):
            print("Error submitting request, RC: %d, Result: %s" % (result.rc, result.result))
            print "svnupdateSTAF False"
            return False
         else:
            print("RC: %d" % result.rc)
            print "svnupdateSTAF True"
            return ret
         rc = handle.unregister()
         sys.exit(rc)
      except Exception,e:
         print e
         print "svnupdateSTAF False"
         return False
      return

   def createSTAF(self,clientip,product_dir):
      ret = True
      request = 'CREATE DIRECTORY %s FULLPATH ' % (product_dir)
      try:
         try:
            handle = STAFHandle("create")
         except STAFException, e:
            print "Error registering with STAF, RC: %d" % e.rc
            sys.exit(e.rc)

         result = handle.submit(clientip, "FS", request)

         if (result.rc != 0):
            print("Error submitting request, RC: %d, Result: %s" % (result.rc, result.result))
            print "createSTAF False"
            return False
         else:
            print("RC: %d" % result.rc)
            print "createSTAF True"
            return ret
         rc = handle.unregister()
         sys.exit(rc)
      except Exception,e:
         print e
         print "createSTAF False"
         return False
      return

   def copySTAF(self,clientip,zip_file,remote_temp_dir,mach_name):
      ret = True
      request = 'COPY FILE %s TODIRECTORY %s TOMACHINE %s ' % (zip_file, remote_temp_dir, mach_name)
      try:
         try:
            handle = STAFHandle("copy")
         except STAFException, e:
            print "Error registering with STAF, RC: %d" % e.rc
            sys.exit(e.rc)

         result = handle.submit(clientip, "FS", request)

         if (result.rc != 0):
            print("Error submitting request, RC: %d, Result: %s" % (result.rc, result.result))
            print "copySTAF False"
            return False
         else:
            print("RC: %d" % result.rc)
            print "copySTAF True"
            return ret
         rc = handle.unregister()
         sys.exit(rc)
      except Exception,e:
         print e
         print "copySTAF False"
         return False
      return

   def pingSTAF(self,clientip):
      try:
         try:
            handle = STAFHandle("test")
         except STAFException, e:
            print "Error registering with STAF, RC: %d" % e.rc
            sys.exit(e.rc)

         #request = 'START "D:\dlp\autoit\uninstall.exe"'
         result = handle.submit(clientip, "PING", "PING")
         if (result.rc != 0):
            print("Error submitting request, RC: %d, Result: %s" % (result.rc, result.result))
            print "pingSTAF False"
            return False
         else:
            print("RC: %s" % result.result)
            print "pingSTAF True"
            return result.result
         rc = handle.unregister()
         sys.exit(rc)
      except Exception as e:
         print e
         print "pingSTAF False"
         return False
      return result.result

   def svnSTAF(self,clientip,vol,command):
      ret = True
      try:
         try:
            handle = STAFHandle("test")
         except STAFException, e:
            print "Error registering with STAF, RC: %d" % e.rc
            sys.exit(e.rc)

         #request = 'START "D:\dlp\autoit\uninstall.exe"'
         result = handle.submit(clientip, "process", "start command" + " " + vol + command)

         if (result.rc != 0):
            print("Error submitting request, RC: %d, Result: %s" % (result.rc, result.result))
            print "svnSTAF False"
            return False
         else:
            print("RC: %d" % result.rc)
            print "svnSTAF True"
            return ret
         rc = handle.unregister()
         sys.exit(rc)
      except Exception,e:
         print e
         print "svnSTAF False"
         return False
      return

   def runSTAF(self,clientip,vol,command):
      ret = True
      try:
         try:
            handle = STAFHandle("test")
         except STAFException, e:
            print "Error registering with STAF, RC: %d" % e.rc
            sys.exit(e.rc)

         #request = 'START "D:\dlp\autoit\uninstall.exe"'
         result = handle.submit(clientip, "process", "start command" + " " + vol + command)

         if (result.rc != 0):
            print("Error submitting request, RC: %d, Result: %s" % (result.rc, result.result))
            print "runSTAF False"
            return False
         else:
            print("RC: %d" % result.rc)
            print "runSTAF True"
            return ret
         rc = handle.unregister()
         sys.exit(rc)
      except Exception,e:
         print e
         print "runSTAF False"
         return False
      return

   def pythonSTAF(self,clientip,vol,command):
      ret = True
      try:
         try:
            handle = STAFHandle("test")
         except STAFException, e:
            print "Error registering with STAF, RC: %d" % e.rc
            sys.exit(e.rc)

         #request = 'START "D:\dlp\autoit\uninstall.exe"'
         result = handle.submit(clientip, "process", "start command python" + " " + vol + command)

         if (result.rc != 0):
            print("Error submitting request, RC: %d, Result: %s" % (result.rc, result.result))
            print "pythonSTAF False"
            return False
         else:
            print("RC: %d" % result.rc)
            print "pythonSTAF True"
            return ret
         rc = handle.unregister()
         sys.exit(rc)
      except Exception,e:
         print e
         print "pythonSTAF False"
         return False
      return

   def install(self,clientip,vol,command):
      ret = True
      try:
         try:
            handle = STAFHandle("inst")
         except STAFException, e:
            print "Error registering with STAF, RC: %d" % e.rc
            sys.exit(e.rc)

         #request = 'START "D:\dlp\autoit\uninstall.exe"'
         result = handle.submit(clientip, "process", "start command" + " " + vol + command)

         if (result.rc != 0):
            print("Error submitting request, RC: %d, Result: %s" % (result.rc, result.result))
            print "install False"
            return False
         else:
            print("RC: %d" % result.rc)
            print "install True"
            return ret
         rc = handle.unregister()
         sys.exit(rc)
         #time.sleep(10)
         #os.system("shutdown /r /t 0")
      except Exception,e:
         print e
         print "install False"
         return False
      return



if __name__ == "__main__":
    app = check()
    def usage():
        print(u'\
        -h or --help：显示帮助信息\n\
        -t ：查看帮助传入对应参数运行测试\n\
        -v or --version：显示版本\
        ')
    if len(sys.argv) == 1:
        usage()
        sys.exit()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "htpv", ["help", "output="])
    except getopt.GetoptError:
        print("argv error,please input")

    for cmd, arg in opts:
        if cmd in ("-h", "--help"):
            usage()
        elif cmd in ("-t", "1"):
            app.checksvn()
        elif cmd in ("-p", "1"):
            print(u"测试")
        elif cmd in ("-v", "--version"):
            print("version 1.0")
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import multiprocessing
import requests
import os
import time
import sys
import getopt
import socket
from edlp import control

def h1():
	ret = True
	http = control()
	ret = http.post_http_content()
	localtime = time.asctime( time.localtime(time.time()) )
	print localtime
	if ret:
	    return ret
	else:
	    return False
def hh1(ip,port,vol):
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

def hh1check():
	ip = "10.95.41.18"
	port = "8001"
	hostname = socket.getfqdn(socket.gethostname())
	ipaddr = socket.gethostbyname(hostname)
	if ipaddr == '10.95.27.76':
	    vol = "D"
	    hh1(ip,port,vol)
	    print '10.95.41.18'
	elif ipaddr == '10.95.41.20':
	    vol = "D"
	    hh1(ip,port,vol)
	    print '10.95.41.18'
	elif ipaddr == '10.95.27.116':
	    vol = "D"
	    hh1(ip,port,vol)
	    print '10.95.41.18'
	elif ipaddr == '10.95.27.74':
	    vol = "D"
	    hh1(ip,port,vol)
	    print '10.95.41.18'
	elif ipaddr == '10.95.41.17':
	    vol = "D"
	    hh1(ip,port,vol)
	    print '10.95.41.18'
	elif ipaddr == '10.95.27.75':
	    vol = "C"
	    hh1(ip,port,vol)
	    print '10.95.41.18'
	elif ipaddr == '10.95.27.77':
	    vol = "C"
	    hh1(ip,port,vol)
	    print '10.95.41.18'
	elif ipaddr == '10.95.27.80':
	    vol = "D"
	    hh1(ip,port,vol)
	    print '10.95.41.18'
	elif ipaddr == '10.95.27.83':
	    vol = "C"
	    hh1(ip,port,vol)
	    print '10.95.41.18'
	elif ipaddr == '10.95.27.79':
	    vol = "C"
	    hh1(ip,port,vol)
	    print '10.95.41.18'
	elif ipaddr == '172.24.83.62':
	    vol = "D"
	    hh1(ip,port,vol)
	    print '10.95.41.18'
	else:
	    print(u"非法IP地址,不能在该机器上运行测试，请测试人员确认!")
	    sys.exit(2)
           
def h11(ip,port,vol):
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

def h11check():
	ip = "10.95.41.15"
	port = "8000"
	hostname = socket.getfqdn(socket.gethostname())
	ipaddr = socket.gethostbyname(hostname)
	if ipaddr == '10.95.27.76':
	    vol = "D"           
	    h11(ip,port,vol)
	    print '10.95.41.15'
	elif ipaddr == '10.95.41.20':
	    vol = "D"
	    h11(ip,port,vol)
	    print '10.95.41.15'
	elif ipaddr == '10.95.27.116':
	    vol = "D"
	    h11(ip,port,vol)
	    print '10.95.41.15'
	elif ipaddr == '10.95.27.74':
	    vol = "D"
	    h11(ip,port,vol)
	    print '10.95.41.15'
	elif ipaddr == '10.95.41.17':
	    vol = "D"
	    h11(ip,port,vol)
	    print '10.95.41.15'
	elif ipaddr == '10.95.27.75':
	    vol = "C"
	    h11(ip,port,vol)
	    print '10.95.41.15'
	elif ipaddr == '10.95.27.77':
	    vol = "C"
	    h11(ip,port,vol)
	    print '10.95.41.15'
	elif ipaddr == '10.95.27.80':
	    vol = "D"
	    h11(ip,port,vol)
	    print '10.95.41.15'
	elif ipaddr == '10.95.27.83':
	    vol = "C"
	    h11(ip,port,vol)
	    print '10.95.41.15'
	elif ipaddr == '10.95.27.79':
	    vol = "C"
	    h11(ip,port,vol)
	    print '10.95.41.15'
	elif ipaddr == '172.24.83.62':
	    vol = "D"
	    h11(ip,port,vol)
	    print '10.95.41.15'
	else:
	    print(u"非法IP地址,不能在该机器上运行测试，请测试人员确认!")
	    sys.exit(2)

if __name__ == '__main__':

    def usage():
        print(u'\
        -h or --help：显示帮助信息\n\
        -k ：多进程并发执行HTTP协议POST CONTENT(测试1s内合并同一目的地址的日志)\n\
        -K ：多进程并发执行HTTP协议POST FILE(测试1s内合并不同目的地址的日志)\n\
        -v or --version：显示版本\
        ')
    if len(sys.argv) == 1:
        usage()
        sys.exit()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hkKv", ["help", "output="])
    except getopt.GetoptError:
        usage()        

    for cmd, arg in opts:
        if cmd in ("-h", "--help"):
            usage()
        elif cmd in ("-k", "1"):
        	multiprocessing.freeze_support()
        	p = multiprocessing.Pool(4)
        	for i in xrange(8):
        		p.apply_async(h1, args=(), callback='')
        	p.close()
        	p.join()
        elif cmd in ("-K", "1"):
        	multiprocessing.freeze_support()
        	p = multiprocessing.Pool(4)
        	for i in xrange(8):
        		p.apply_async(h11check, args=(), callback='')
        		p.apply_async(hh1check, args=(), callback='')
        	p.close()
        	p.join()
        elif cmd in ("-v", "--version"):
            print("version 1.0")
#!/usr/bin/python
# -*- coding: UTF-8 -*-
#载入必要的模块
import MySQLdb
import datetime

class mydb:
    db = MySQLdb.connect(host = 'localhost',#本地数据库
                        user = 'root', #用户名
                        passwd = 'XXXXX', #数据库密码
                        db = 'test', #数据库名
                        charset = 'utf8')  #数据库编码
    Url = "http://www.baidu.com"
    Time = datetime.datetime.now() #系统当前时刻


    db.close()
#end--------------------------------------------------------
if __name__ == "__main__":
    app = office()
    def usage():
        print(u'\
        -h or --help：显示帮助信息\n\
        -v or --version：显示版本\
        ')
    if len(sys.argv) == 1:
        usage()
        sys.exit()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hv", ["help", "version"])
    except getopt.GetoptError:
        usage()        

    for cmd, arg in opts:
        if cmd in ("-h", "--help"):
            usage()
        elif cmd in ("-v", "--version"):
            print("version 1.0")
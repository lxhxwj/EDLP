#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import string
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')

# 说明：UTF兼容ISO8859-1和ASCII，GB18030兼容GBK，GBK兼容GB2312，GB2312兼容ASCII
CODES = ['UTF-8', 'UTF-16', 'GB18030', 'BIG5']
# UTF-8 BOM前缀字节
UTF_8_BOM = b'\xef\xbb\xbf'
#汇总整理成函数库
class CODE:
	# win下命令行参数为gbk编码：star.gbk2unicode(sys.argv[1]) + u'也有'
	def gbk2unicode(self,s):
		return s.decode('gbk', 'ignore')

	# 脚本文件#coding:utf-8时默认不带u的字符串为utf8字符串：star.utf82unicode('我')
	def utf82unicode(self,s):
		return s.decode('utf-8', 'ignore')

	# 带u的字符串为unicode
	# star.unicode2gbk(u'\u4e5f\u6709')
	# star.unicode2gbk(u'也有')
	def unicode2gbk(self,s):
		return s.encode('gbk')

	# 带u的字符串为unicode
	# star.unicode2utf8(u'\u4e5f\u6709')
	# star.unicode2utf8(u'也有')
	def unicode2utf8(self,s):
		return s.encode('utf-8')

	# win下命令行参数为gbk编码：star.gbk2utf8(sys.argv[1]) + '也有'
	def gbk2utf8(self,s):
		return s.decode('gbk', 'ignore').encode('utf-8')

	def utf82gbk(self,s):
		return s.decode('utf-8', 'ignore').encode('gbk')

	def changecode(self,src,dst):
		tt = codecs.open(src, 'rb', 'utf-16')  # src为unicode编码文件，以unicode编码打开，utf-16=unicode
		mm = codecs.open(dst, 'wb', 'utf-8')
		ff = tt.readlines()
		for i in ff:
			mm.write(i.encode('utf-8'))
		tt.close
		mm.close

	# 获取文件编码类型
	def file_encoding(self,file_path):
		#获取文件编码类型\n
    	#param file_path: 文件路径\n
    	#return: \n
		with open(file_path, 'rb') as f:
			return string_encoding(f.read())

	# 获取字符编码类型
	def string_encoding(self,b):
		#获取字符编码类型\n
    	#param b: 字节数据\n
    	#return: \n
    	# 遍历编码类型
		for code in CODES:
			try:
				b.decode(encoding=code)
				if 'UTF-8' == code and b.startswith(UTF_8_BOM):
					return 'UTF-8-SIG'
				return code
			except Exception:
				continue
		return '未知的字符编码类型'


if __name__ == "__main__":
	c = CODE()
	s = c.gbk2unicode('我是谁')
	#print(c.string_encoding(s))
	#print sys.getdefaultencoding()
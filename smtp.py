#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import smtplib
import email
import getopt
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header
from email.utils import parseaddr, formataddr
reload(sys)
sys.setdefaultencoding('utf-8')

class SMTP:


    def SMTPTest(self):
        ret = True
        try:
            msg = MIMEText('王宝强 您好！', 'plain', 'utf-8')
            # 输入Email地址和口令:
            from_addr = 'dlptest1@dlp.cn'
            #这里的密码一定是授权码
            password = 'Aa123456'
            # 输入SMTP服务器地址:这里我们用自己搭建hMailServer
            smtp_server = '10.95.41.18'
            # 输入收件人地址:
            to_addr = 'dlptest2@dlp.cn'
            def _format_addr(s):
                name, addr = parseaddr(s)#这个函数会解析出姓名和邮箱地址
                return formataddr(( \
                    Header(name, 'utf-8').encode(), \
                    addr.encode('utf-8') if isinstance(addr, unicode) else addr))
            #设置发件人，收件人姓名和邮件主题
            msg['From'] = _format_addr(u'张秀昌 <%s>' % from_addr)
            msg['To'] = _format_addr(u'王宝强 <%s>' % to_addr)
            msg['Subject'] = Header(u'公司停电通知', 'utf-8').encode()
            server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
            #server.ehlo() 
            #server.starttls()  #开启加密传输
            server.set_debuglevel(0)#打印出和SMTP服务器交互的所有信息，不想打印就设置为0
            server.login(from_addr, password)#登录服务器
            #发送邮件，这里第二个参数是个列表，可以有多个收件人
            #邮件正文是一个str，as_string()把MIMEText对象变成str
            server.sendmail(from_addr, [to_addr], msg.as_string())
            server.quit()
            print "SMTP OK" 
            return ret
        except Exception,e:
            print e
            print "SMTP False" 
            return False
        return
    def SmtpsAttach(self):
        HOST = "smtp.126.com" #定义smtp主机
        SUBJECT = "test-smtps" #定义邮件主题
        TO = "datasec360@126.com" #定义邮件收件人
        FROM = "datasec360@126.com" #定义邮件发件人
        '''
        text = "python test mail" #邮件的内容
        BODY=string.join(( #组装sendmail方法的邮件主体内容，各段以"\r\n"进行分隔
        "From:%s" %FROM,
        "To:%s" %TO,
        "Subject:%s"%SUBJECT,
        "",
        text
        ),"\r\n")
        '''
        message = MIMEMultipart()
        message['From'] = "datasec360@126.com"
        message['To'] = "datasec360@126.com"
        message['Subject'] = "test-smtps"

        with open('file\\index.html','r') as f:
            content = f.read()

        part1 = MIMEText(content,'html','utf-8')

        with open('file\\dlp.txt','r')as h:
            content2 = h.read()

        part2 = MIMEText(content2,'plain','utf-8')

        part2['Content-Type'] = 'application/octet-stream'

        part2['Content-Disposition'] = 'attachment;filename="dlp.txt"'

        with open('file\\att.png','rb')as fp:
            picture = MIMEImage(fp.read())

            picture['Content-Type'] = 'application/octet-stream'
            picture['Content-Disposition'] = 'attachment;filename="att.png"'

        message.attach(part1)
        message.attach(part2)
        message.attach(picture)
        try:
            server = smtplib.SMTP() #创建一个SMTP对象
            server.connect(HOST,"25") #通过connect方法连接smtp主机
            #server.starttls() #启动安全传输模式
            s = smtplib.SMTP_SSL(HOST)
            s.login("datasec360@126.com","Aa123456") #邮件账户登录校验
            #server.sendmail(FROM,TO,BODY) #邮件发送
            s.sendmail(FROM,TO,message.as_string())
            s.quit() #断开smtp连接
            print(u"邮件发送成功")
            return True
        except smtplib.SMTPException as e:
            print(u'邮件发送失败',e)
            return False
    def SmtpAttach(self):
        ret = True
        try:
            HOST = '10.95.41.18'
            SUBJECT = '张秀昌发送的带附件的测试邮件'
            FROM = 'dlptest1@dlp.cn'
            PASSWORD = 'Aa123456'
            To = 'dlptest2@dlp.cn'
            msg = MIMEMultipart('related')
            # 创建一个用于发送文本的MIMEText对象
            msg_text = MIMEText('<h1 style="text-algin:center">王宝强先生！恭喜您查收到该邮件</h1><span style="color:red">详情如下：</span><br><img src="cid:zg">','html','utf-8')

            msg.attach(msg_text)

            def add_image(path,imgid):

                data = open(path,'rb')
                # 创建MIMEImage对象，读取图片作为imgdata的数据参数
                msg_image = MIMEImage(data.read())
                # 关闭文件
                data.close()
                # 指定图片文件的Content-ID
                msg_image.add_header('Content-ID',imgid)
                return msg_image

            # 添加图片附件
            msg.attach(add_image(u'file\\我是tupian.jpg','zg'))

            # 将xls作为附件添加到邮件中
            # 创建MIMEText对象，保存txt文件
            attach = MIMEText(open(u'file\\我是tupian附件.txt','rb').read(),'base64','utf-8')
            # 指定当前文件格式类型
            attach['Content-type'] = 'application/octet-stream'
            # 配置附件显示的文件名称,当点击下载附件时，默认使用的保存文件的名称
            # gb18030 qq邮箱中使用的是gb18030编码，防止出现中文乱码
            #attach['Content-Disposition'] = 'attachment;filename="我是tupian附件.txt"'.decode('utf-8').encode('gb18030')
            attach['Content-Disposition'] = 'attachment;filename="我是tupian附件.txt"'
            # 把附件添加到msg中
            msg.attach(attach)
            # 设置必要请求头信息
            msg['From'] = FROM
            msg['To'] = To
            msg['Subject'] = SUBJECT

            # 发送邮件
            server = smtplib.SMTP(HOST, 25) # SMTP协议默认端口是25
            #server.ehlo() 
            #server.starttls()  #开启加密传输
            server.set_debuglevel(0)#打印出和SMTP服务器交互的所有信息，不想打印就设置为0
            server.login(FROM,PASSWORD)#登录服务器
            server.sendmail(FROM,To,msg.as_string())
            server.quit()
            print "SMTP OK" 
            return ret
        except Exception,e:
            print e
            print "SMTP False" 
            return False
        return

    def SmtpAttach_pyauto(self,vol):
        ret = True
        try:
            HOST = '10.95.41.18'
            SUBJECT = '张秀昌发送的带附件的测试邮件'
            FROM = 'dlptest1@dlp.cn'
            PASSWORD = 'Aa123456'
            To = 'dlptest2@dlp.cn'
            msg = MIMEMultipart('related')
            filename1 = u"%s:\\DLP\\file\\tupian.jpg" % vol
            filename2 = u"%s:\\DLP\\file\\tupianfujian.txt" % vol
            # 创建一个用于发送文本的MIMEText对象
            msg_text = MIMEText('<h1 style="text-algin:center">王宝强先生！恭喜您查收到该邮件</h1><span style="color:red">详情如下：</span><br><img src="cid:zg">','html','utf-8')

            msg.attach(msg_text)

            def add_image(path,imgid):

                data = open(path,'rb')
                # 创建MIMEImage对象，读取图片作为imgdata的数据参数
                msg_image = MIMEImage(data.read())
                # 关闭文件
                data.close()
                # 指定图片文件的Content-ID
                msg_image.add_header('Content-ID',imgid)
                return msg_image

            # 添加图片附件
            msg.attach(add_image(filename1,'zg'))

            # 将xls作为附件添加到邮件中
            # 创建MIMEText对象，保存txt文件
            attach = MIMEText(open(filename2,'rb').read(),'base64','utf-8')
            # 指定当前文件格式类型
            attach['Content-type'] = 'application/octet-stream'
            # 配置附件显示的文件名称,当点击下载附件时，默认使用的保存文件的名称
            # gb18030 qq邮箱中使用的是gb18030编码，防止出现中文乱码
            #attach['Content-Disposition'] = 'attachment;filename="我是tupian附件.txt"'.decode('utf-8').encode('gb18030')
            attach['Content-Disposition'] = 'attachment;filename="我是tupian附件.txt"'
            # 把附件添加到msg中
            msg.attach(attach)
            # 设置必要请求头信息
            msg['From'] = FROM
            msg['To'] = To
            msg['Subject'] = SUBJECT

            # 发送邮件
            server = smtplib.SMTP(HOST, 25) # SMTP协议默认端口是25
            #server.ehlo() 
            #server.starttls()  #开启加密传输
            server.set_debuglevel(0)#打印出和SMTP服务器交互的所有信息，不想打印就设置为0
            server.login(FROM,PASSWORD)#登录服务器
            server.sendmail(FROM,To,msg.as_string())
            server.quit()
            print "SMTP OK" 
            return ret
        except Exception,e:
            print e
            print "SMTP False" 
            return False
        return

    def WhitelistSmtpAttach(self):
        ret = True
        try:
            HOST = '10.95.41.18'
            SUBJECT = '张秀昌发送的带附件的测试邮件'
            FROM = 'dlptest1@dlp.cn'
            PASSWORD = 'Aa123456'
            To = 'dlptest3@dlp.cn'
            msg = MIMEMultipart('related')
            # 创建一个用于发送文本的MIMEText对象
            msg_text = MIMEText('<h1 style="text-algin:center">王宝强先生！恭喜您查收到该邮件</h1><span style="color:red">详情如下：</span><br><img src="cid:zg">','html','utf-8')

            msg.attach(msg_text)

            def add_image(path,imgid):

                data = open(path,'rb')
                # 创建MIMEImage对象，读取图片作为imgdata的数据参数
                msg_image = MIMEImage(data.read())
                # 关闭文件
                data.close()
                # 指定图片文件的Content-ID
                msg_image.add_header('Content-ID',imgid)
                return msg_image

            # 添加图片附件
            msg.attach(add_image(u'file\\我是tupian.jpg','zg'))

            # 将xls作为附件添加到邮件中
            # 创建MIMEText对象，保存txt文件
            attach = MIMEText(open(u'file\\我是tupian附件.txt','rb').read(),'base64','utf-8')
            # 指定当前文件格式类型
            attach['Content-type'] = 'application/octet-stream'
            # 配置附件显示的文件名称,当点击下载附件时，默认使用的保存文件的名称
            # gb18030 qq邮箱中使用的是gb18030编码，防止出现中文乱码
            #attach['Content-Disposition'] = 'attachment;filename="我是tupian附件.txt"'.decode('utf-8').encode('gb18030')
            attach['Content-Disposition'] = 'attachment;filename="我是tupian附件.txt"'
            # 把附件添加到msg中
            msg.attach(attach)
            # 设置必要请求头信息
            msg['From'] = FROM
            msg['To'] = To
            msg['Subject'] = SUBJECT

            # 发送邮件
            server = smtplib.SMTP(HOST, 25) # SMTP协议默认端口是25
            #server.ehlo() 
            #server.starttls()  #开启加密传输
            server.set_debuglevel(0)#打印出和SMTP服务器交互的所有信息，不想打印就设置为0
            server.login(FROM,PASSWORD)#登录服务器
            server.sendmail(FROM,To,msg.as_string())
            server.quit()
            print "SMTP OK" 
            return ret
        except Exception,e:
            print e
            print "SMTP False" 
            return False
        return

    def WhitelistSmtpAttach_pyauto(self,vol):
        ret = True
        try:
            HOST = '10.95.41.18'
            SUBJECT = '张秀昌发送的带附件的测试邮件'
            FROM = 'dlptest1@dlp.cn'
            PASSWORD = 'Aa123456'
            To = 'dlptest3@dlp.cn'
            msg = MIMEMultipart('related')
            filename1 = u"%s:\\DLP\\file\\tupian.jpg" % vol
            filename2 = u"%s:\\DLP\\file\\tupianfujian.txt" % vol
            # 创建一个用于发送文本的MIMEText对象
            msg_text = MIMEText('<h1 style="text-algin:center">王宝强先生！恭喜您查收到该邮件</h1><span style="color:red">详情如下：</span><br><img src="cid:zg">','html','utf-8')

            msg.attach(msg_text)

            def add_image(path,imgid):

                data = open(path,'rb')
                # 创建MIMEImage对象，读取图片作为imgdata的数据参数
                msg_image = MIMEImage(data.read())
                # 关闭文件
                data.close()
                # 指定图片文件的Content-ID
                msg_image.add_header('Content-ID',imgid)
                return msg_image

            # 添加图片附件
            msg.attach(add_image(filename1,'zg'))

            # 将xls作为附件添加到邮件中
            # 创建MIMEText对象，保存txt文件
            attach = MIMEText(open(filename2,'rb').read(),'base64','utf-8')
            # 指定当前文件格式类型
            attach['Content-type'] = 'application/octet-stream'
            # 配置附件显示的文件名称,当点击下载附件时，默认使用的保存文件的名称
            # gb18030 qq邮箱中使用的是gb18030编码，防止出现中文乱码
            #attach['Content-Disposition'] = 'attachment;filename="我是tupian附件.txt"'.decode('utf-8').encode('gb18030')
            attach['Content-Disposition'] = 'attachment;filename="我是tupian附件.txt"'
            # 把附件添加到msg中
            msg.attach(attach)
            # 设置必要请求头信息
            msg['From'] = FROM
            msg['To'] = To
            msg['Subject'] = SUBJECT

            # 发送邮件
            server = smtplib.SMTP(HOST, 25) # SMTP协议默认端口是25
            #server.ehlo() 
            #server.starttls()  #开启加密传输
            server.set_debuglevel(0)#打印出和SMTP服务器交互的所有信息，不想打印就设置为0
            server.login(FROM,PASSWORD)#登录服务器
            server.sendmail(FROM,To,msg.as_string())
            server.quit()
            print "SMTP OK" 
            return ret
        except Exception,e:
            print e
            print "SMTP False" 
            return False
        return

if __name__ == "__main__":
    app = SMTP()
    def usage():
        print(u'\
        -h or --help：显示帮助信息\n\
        -m ：发送不带附件的邮件\n\
        -v or --version：显示版本\
        ')
    if len(sys.argv) == 1:
        usage()
        sys.exit()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hmsv", ["help", "output="])
    except getopt.GetoptError:
        usage()        

    for cmd, arg in opts:
        if cmd in ("-h", "--help"):
            usage()
        elif cmd in ("-m", "1"):
            app.SMTPTest()
        elif cmd in ("-s", "1"):
            app.SmtpsAttach()       
        elif cmd in ("-v", "--version"):
            print("version 1.0")
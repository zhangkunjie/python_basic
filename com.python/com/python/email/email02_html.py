# -*- coding: UTF-8 -*-
'''
发送txt文本邮件
'''
from email.header import Header
from email.mime.text import MIMEText  
import smtplib  


mailto_list=["zhangkunjie1988@126.com"] 
mail_host="smtp.126.com"  #设置服务器
mail_user="zhangkunjie1988@126.com"    #用户名
mail_pass="PPxy168891"   #口令  #发件箱的后缀
mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>
"""
mail_message = MIMEText(mail_msg, 'html', 'utf-8')
subject = 'Python SMTP 邮件测试'
mail_message['Subject'] = Header(subject, 'utf-8')
server = smtplib.SMTP()  
server.connect(mail_host,25)  
server.login(mail_user,mail_pass)  
server.sendmail(mail_user, mailto_list, mail_message.as_string())  
server.close()    
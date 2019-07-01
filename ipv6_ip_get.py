#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import os
import time
def send_ip_to_my_email(ip):
    ret=True
    my_sender=''    # 发件人邮箱账号
    my_pass = ''              # 发件人邮箱密码
    my_user=''      # 收件人邮箱账号，我这边发送给自己
#    second_user='gengxyzz@163.com'      # 收件人邮箱账号，我这边发送给自己
    try:
        msg=MIMEText(ip,'plain','utf-8')
        msg['From']=formataddr(["XiangweiGeng",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["XiangweiGeng",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="实验室电脑最新ip"                # 邮件的主题，也可以说是标题
 
        server=smtplib.SMTP("smtp.tju.edu.cn", 25)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
#        server.sendmail(my_sender,[second_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret
ip = os.popen('ifconfig | grep -E "enp1s0|inet|ppp0"').readlines()
ip = "\n".join(ip) 
ip_now = ip
while 1:
    if(send_ip_to_my_email(ip)):
        break
time.sleep(5)
while True:
    ip = os.popen('ifconfig | grep -E "enp1s0|inet|ppp0"').readlines()
    ip = "\n".join(ip) 
    if ip==ip_now:
        pass
    else:
        try:
            if(send_ip_to_my_email(ip)):
                ip_now = ip
        except:
            pass
    time.sleep(5)

#!/usr/bin/env python
# -*- encoding=utf-8 -*-

'''mailsend.py
邮件发送模块
'''

import email.mime.multipart
import email.mime.text
import smtplib


class MailSender:
    def __init__(self, server, user, password):
        """初始化
        Args:
            server - str stmp 服务器地址，ip 或者域名
            user - str 发送邮件的 smtp 服务登陆用户名
            password - str 邮箱密码
        """
        self.__mail_server = server
        self.__mail_user = user
        self.__mail_password = password
        self.__mail_from = user

    def send(self, to_addrs, subject, html_txt):
         # 设定root信息
        msg_root = email.mime.multipart.MIMEMultipart('related')
        msg_root['Subject'] = subject
        msg_root['From'] = self.__mail_from
        msg_root['To'] = ', '.join(to_addrs)
        msg_root.preamble = 'This is a multi-part message in MIME format.'

        # Encapsulate the plain and HTML versions of the message body in an
        # ‘alternative’ part, so message agents can decide which they want to display.
        msg_alt = email.mime.multipart.MIMEMultipart('alternative')
        msg_txt = email.mime.text.MIMEText(html_txt, 'html', 'utf-8')
        msg_alt.attach(msg_txt)
        msg_root.attach(msg_alt)

        # 发送邮件
        smtp = smtplib.SMTP()
        # 设定调试级别，依情况而定
        smtp.set_debuglevel(0)
        smtp.connect(self.__mail_server)
        smtp.login(self.__mail_user, self.__mail_password)
        smtp.sendmail(self.__mail_from, to_addrs, msg_root.as_string())
        smtp.quit()


if __name__ == '__main__':
    to_addrs = ['pemakoa@gmail.com']
    subject = '邮件主题'
    html_txt = '<B>HTML正文文本</B><img src="" />'

    ms = MailSender(server='', user='', password="")
    ms.send(to_addrs, subject, html_txt)

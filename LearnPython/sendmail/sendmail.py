#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
通过 smtp 发送邮件的工具
对 python lib 的一些函数的简单封装，只需要调用一个函数即可发送邮件
Create on 2016-10-26
# 注意使用企业邮箱可以直接在html 中嵌入 img=src 具体路径，个人邮箱
# 需要对图片进行 base64编码 放到 html 中，或者把图片作为附件上传

TODO:附件的发送 和 HTML 中图片的发送进行优化
"""

__author__ = ["pemako <pemakoa@gmail.com>"]

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import sys
import os
import time
import smtplib
import __main__


class SmtpEmailTool(object):
    """发送内容格式为 html 的邮件工具"""

    def __init__(self, server, user, password, owner='unknow'):
        """初始化
        Args:
            server - str stmp 服务器地址，ip 或者域名
            user - str 发送邮件的 smtp 服务登陆用户名
            password - str 邮箱密码
        """
        self.mailServer = server
        self.mailUserName = user
        self.mailPassword = password
        self.mailOwner = owner

    def sendEmail(self, toAdd, subject, htmlText, retryCount=3):
        """发送邮件
        Args:
            toAdd - list of email receivers
            subject - str or unicode 邮件标题
            htmlText - unicode 邮件内容
            fromAdd - 发件人的 email地址，为 None 时使用系统配置的值
            retryCount - 重试次数，默认三次; 重试间隔默认五秒，暂不提供配置入口
        """
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = isinstance(
            subject, str) and subject.decode('UTF-8') or subject
        msgRoot['From'] = self.mailUserName
        msgRoot['To'] = ','.join(toAdd)
        msgRoot['X-PEMAKO-OWNER'] = self.mailOwner
        try:
            msgRoot['X-PEMAKO-HOST'] = os.uname()[1]
        except:
            msgRoot['X-PEMAKO-HOST'] = 'unknown'
        try:
            msgRoot['X-PEMAKO-USER'] = os.environ['USER']
        except:
            msgRoot['X-PEMAKO-USER'] = 'unknown'
        try:
            msgRoot['X-PEMAKO-PWD'] = os.environ['PWD']
        except:
            msgRoot['X-PEMAKO-PWD'] = 'unknown'
        try:
            msgRoot['X-PEMAKO-SCRIPT'] = os.path.basename(__main__.__file__)
        except:
            msgRoot['X-PEMAKO-SCRIPT'] = 'unknown'
        msgRoot.preamble = 'This is a multi-part message in MIME format.'

        # Encapsulate the plain and HTML versions of the message body in an
        # ‘alternative’ part, so message agents can decide which they want to display.
        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)

        # 设定HTML信息
        msgText = MIMEText(htmlText, 'html', 'utf-8')
        msgAlternative.attach(msgText)

        # 设定内置图片信息 定义图片 ID 在 html 中引用，如本图片 id=image1
        # 则在 html 中 引用为 <img src="cid:image1">
        #fp = open('test.png', 'rb')
        #msgImage = MIMEImage(fp.read())
        # fp.close()
        #msgImage.add_header('Content-ID', '<image1>')
        # msgRoot.attach(msgImage)

        # 设定附件内容 构造附件1传送当前文件夹下的 a.txt 文件
        #att1 = MIMEText(open('a.txt', 'rb').read(), 'base64', 'utf-8')
        #att1['Content-type'] = 'application/octet-stream'
        # 这里的额 filename 可以任意写，写什么名字，邮件中显示什么名字
        #att1['Content-Disposition'] = 'attachment; filename="a.txt"'
        # msgRoot.attach(att1)

        while retryCount > 0:
            try:
                # 发送邮件
                smtp = smtplib.SMTP()
                # 设定调试级别，依情况而定
                smtp.set_debuglevel(0)  # 0 close debug info
                smtp.connect(self.mailServer)
                smtp.login(self.mailUserName, self.mailPassword)
                smtp.sendmail(self.mailUserName, toAdd, msgRoot.as_string())
                break
            except Exception, e:
                retryCount -= 1
                sys.stderr.write(
                    'error sending mail, retries left: %d, exInfo: %r\n' % (retryCount, e))
                time.sleep(5)
            finally:
                try:
                    smtp.quit()
                except:
                    pass


if __name__ == "__main__":
    toAdd = ['731482121@qq.com']
    subject = u'126邮箱测试'
    htmlText = u'<B>每日笑话</B><div><b>文字笑话</b>%(text)s</div>\
            <div><b>图片笑话</b><img src="https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/logo_white_fe6da1ec.png"></div>'

    emailTools = SmtpEmailTool(
        server='',
        user='',
        password="")

    emailTools.sendEmail(toAdd, subject, htmlText)

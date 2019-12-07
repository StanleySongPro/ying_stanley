#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 15:29:56 2019

@author: olivia
"""

import re
import poplib
import base64
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

def get_mail_content():
    useraccount = 'yanlaile1019@gmail.com'
    password = "odtxybaggivhsmle"
    pop3_server = 'pop.gmail.com'
    
    #开始连接到服务器
    server = poplib.POP3_SSL(pop3_server)
    
    #打开或者关闭调试信息，为打开时，会在控制台打印客户端与服务器的交互信息
    server.set_debuglevel(1) # 1为打开
    
    #打印POP3服务器的欢迎文字，验证是否正确连接到了邮件服务器
    #print(server.getwelcome().decode('utf8'))
    
    #开始进行身份验证
    server.user(useraccount)
    server.pass_(password)
    
    #返回邮件总数和占用服务器的空间大小（字节数），通过stat（）方法
    email_num, email_size = server.stat()
    print("消息的数量:{0},\n消息的总大小:{1}".format(email_num, email_size))
    
    #使用list()返回所有邮件的编号，默认为字节类型的串
    rsp, msg_list, rsp_size = server.list()
    print("服务器的响应:{0},\n消息列表:{1},\n返回消息的大小:{2}".format(rsp, msg_list, rsp_size))
    
    print("邮件总数: {}".format(len(msg_list)))
    
    #单纯获取最新一封的邮件
    total_mail_numbers = len(msg_list)

    rsg, msglines, msgsize = server.retr(total_mail_numbers)
    
    print("服务器的响应: {0},\n原始邮件内容: {1},\n改封邮件所占字节大小:{2}".format(rsp, msglines, msgsize))
    
    msg_content = b'\r\n'.join(msglines).decode('gbk')
    
    msg = Parser().parsestr(text=msg_content)
    print("解码后的邮件信息:\n{}".format(msg))
    
    #关闭服务器的连接，释放资源
    server.close()
    
    return msg

# 用来解析邮件主题
def parser_subject(msg):
    subject = msg['Subject']
    value, charset = decode_header(subject)[0]
    if charset:
        value = value.decode(charset)
    print('邮件主题:{0}'.format(value))
    return value

# 用来解析邮件来源
def parser_address(msg):
    hdr,addr = parseaddr(msg['From'])
    # name 发件人邮箱名称， addr发件人邮箱地址
    name, charset = decode_header(hdr)[0]
    if charset:
        name = name.decode(charset)
        print('发送人邮箱名称:{0}, 发件人邮箱地址:{1}'.format(name, addr))
def parser_content(msg):
    content = msg.get_payload()
    
    #文本信息
    content_charset = content[0].get_content_charset()#获取编码格式
    text = content[0].as_string().split('base64')[-1]
    text_content = base64.b64decode(text).decode(content_charset) # base64解码
    
    # 添加了HTML代码的信息
    content_charset = content[1].get_content_charset()
    text = content[1].as_string().split('base64')[-1]
    html_content = base64.b64decode(text).decode(content_charset,'ignore')
    
    print('文本信息：{0}\n添加了HTML代码的信息:{1}'.format(text_content, html_content))       

def Search_in(keyword, universe):
    return bool(re.search(keyword, universe, re.IGNORECASE))

if __name__ == '__main__':

    # 返回解码的邮件详情
    #msg = get_mail_content()
    # 解析邮件主题
    #parser_subject(msg)
    # 解析发件人详情
    #parser_address(msg)
    # 解析内容
    #parser_content(msg)
    # search specified email
    
#f Search_in("yanlaile1019@gmail.com", parser_address(msg)):
  #  if Search_in("app", parser_subject(msg)):
        
        # 返回解码的邮件详情
        msg = get_mail_content()
        # 解析邮件主题
        parser_subject(msg)
        # 解析发件人详情
        parser_address(msg)
        # 解析内容
        parser_content(msg)
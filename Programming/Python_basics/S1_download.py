#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import smtplib
import ssl
from email.mime.text import MIMEText
from email.header import Header

import imaplib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email
from datetime import datetime
import time
import re
import pandas as pd
import numpy as np
from datetime import date
from datetime import timedelta
from IPython.display import clear_output
from email.mime.application import MIMEApplication
import os, inspect

class ProcessEmail():
    def __init__(self, BASE=None):
        self.BASE = BASE


    def search_in(self, keyword=None, universe=None):
        """
        search 'keyword' from 'universe' to target the wanted email.
        """
        return bool(re.search(keyword, universe, re.IGNORECASE))


    def email_sending(
            self,
            subject = None,
            content = None,
            receivers = ['olivia19931019@gmail.com'],
            cclist = ["360288719@qq.com"],
            sender = 'zhou.yingying@finexisam.com',
            mail_host = 'smtp.office365.com',
            mail_user = 'zhou.yingying@finexisam.com',
            mail_pass = 'FAM@201907',
            port = 587
            ):
        message = MIMEText(content,'plain','utf-8')
        message['Subject'] = Header(subject, 'utf-8')
        message['From'] = Header(sender)
        message['To'] = Header(", ".join(receivers))
        message["Cc"] = Header(", ".join(cclist))

        smtpObj = smtplib.SMTP_SSL(mail_host, port)
        smtpObj.login(mail_user, mail_pass)
        try:
            smtpObj.sendmail(sender, receivers+cclist, message.as_string())
            print("Sent successfully to {}".format(receivers+cclist))
            smtpObj.quit()
        except smtplib.SMTPException as e:
            print("Exception: {}".format(e))
        return smtpObj



    def convert_to_datetime(self, date_str=None):
        """
        convert date from string to datetime format
        """
        if type(date_str) == str:
            try:
                date_str = datetime.strptime(date_str, '%m/%d/%Y')
            except:
                try:
                    date_str = datetime.strptime(date_str, '%Y-%m-%d')
                except:
                    try:
                        date_str = datetime.strptime(date_str, '%d/%m/%Y')
                    except:
                        print(date_str,'cannot convert to datetime')
        return date_str

    def convert_to_str(self, date_time):
        """
        convert datetime format from datetime to str
        """
        if type(date_time) != str:
            try:
                date_time = date_time.strftime("%m/%d/%Y")
            except:
                print(date_time,"cannot convert to str")

        return date_time

    def convert_table_format(self, df):
        df = df.reset_index(drop = True)
        for i in df.index:
            df.loc[i,'Date'] = self.convert_to_str(df.loc[i,"Date"])
        return df


    def email_saving(
            self,
            emailbody=None,
            folder_path=None,
            att_type=[".pdf", ".xls", ".xlsx",".zip"]):
        mail = email.message_from_bytes(emailbody)
        fileName =None

        # retrieve attachment file name
        for part in mail.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get("Content-Disposition") is None:
                continue
            fileName = part.get_filename()
            # decode
#            try:
#                fileName = decode_header(fileName)[0][0].decode(decode_header(fileNmae)[0][1])
#                print (fileName)
#            except Exception as e:
#                print (e)

            # save attachment
            if fileName and any(fileName.endswith(i) for i in att_type):
                filePath = os.path.join(folder_path, fileName)
                if not os.path.isfile(filePath):
                    fp = open(filePath, 'wb')
                    fp.write(part.get_payload(decode = True))
                    fp.close()
                    print("you got new target")
                else:
                    print('Existing File:' + fileName)
                    self.email_sending(subject = "Duplicate" + fileName)
        return fileName


    def checkEmail_FX(
            self,
            first_email_FX = None,
            folder_path = None,
            mail_host = 'smtp.office365.com',
            mail_user = 'zhou.yingying@finexisam.com',
            mail_pass = 'FAM@201907',
            port = 443):

        if not os.path.isdir(folder_path):
            os.makedirs(folder_path)

        file_name = None

        #Inbox Scanning
        server = imaplib.IMAP4_SSL(mail_host)
        server.login(mail_user, mail_pass)
        status, messages = server.select("INBOX")
        print("Status : {}".format(status))

        # Inbox Index
        type, data = server.search(None, 'ALL')
        print(type,data)

        mail_ids = data[0]
        print(mail_ids)

        id_list = mail_ids.split()
        print(id_list)

        latest_email_FX = int(id_list[-1])


        # Email
        for i in range(first_email_FX+1, latest_email_FX+1):
            typ, data = server.fetch(str(i),'(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    email_subject = msg["Subject"]
                    email_from = msg["From"]

                    # Check keywords
                    if (self.search_in("test", email_subject)) and \
                    (self.search_in('file',email_subject)) and \
                    (self.search_in("olivia", email_from)) and \
                    (self.search_in('re', email_subject)==False) and \
                    (self.search_in('fw',email_subject)==False):
                        file_name = self.email_saving(emailbody = data[0][1],folder_path = folder_path)
        return file_name, latest_email_FX


    def FX_FT_process(
            self,
            sender = None,
            receivers = None,
            FX1_record_check = None,
            first_email_FX=None,
            folder_path=None,
            process_time = [[15, 30],[16,30],[17,30]]):

        timeObj = datetime.now()
        date_now = str(timeObj.date())
        week_now = timeObj.weekday()

        time_now = timeObj.time()

        if week_now < 6:   # Weekdays
            if week_now > 0:
                # FX1 processing
                today10am = time_now.replace(hour=process_time[0][0], minute=process_time[0][1], second=0, microsecond=0)
                today1030am = time_now.replace(hour=process_time[1][0], minute=process_time[1][1], second=0, microsecond=0)
                today1130am = time_now.replace(hour=process_time[2][0], minute=process_time[2][1], second=0, microsecond=0)

                if (time_now>today10am) and (time_now<today1030am):
                    print(date_now)
                    file_name, first_email_FX = self.checkEmail_FX(first_email_FX, folder_path)
                    print(file_name)
                    print(first_email_FX)
#                    FX1_record = Record_append_FX1(folder_path, file_name)
#                    generate_upload_file_FX1(folder_path, FX1_record)

#                    time.sleep(60*30)

                # FX1 status check
                elif (time_now>today1030am) and (time_now<today1130am):
                    if (datetime.today()-self.convert_datetime(list(FX1_record_check["Date"])[-1])).days == int(np.where(week_now == 0,3,1)):
                        print("Upload file prepared successfully!")
                        self.Email_sending(content="Upload file prepared successfully!", receivers=receivers, sender=sender)
                    else:
                        print("Problem with upload file, please check!")
                        self.Email_sending(content="Problem with upload file, please check!", receivers=receivers, sender=sender)
                    print("\n")
#                    time.sleep(60*60*4)
                else:
                    pass
            else:
                pass
        else:    # Weekends
            pass

        return first_email_FX
#%%
if __name__ == '__main__':

    BASE = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

    ps = ProcessEmail(BASE=BASE)
    pdf_from_email = os.path.join(BASE, "att_folder", "pdf_from_email")
    pdf_from_email_dcrpt = os.path.join(BASE, "att_folder", "pdf_decrypt")
    if not os.path.isdir(pdf_from_email_dcrpt):
        os.mkdir(pdf_from_email_dcrpt)
    pdf_to = os.path.join(BASE, "att_folder", "pdf_to")
    if not os.path.isdir(pdf_to):
        os.mkdir(pdf_to)

    first_email_FX = 30
    folder_path = pdf_from_email
    sender = 'zhou.yingying@finexisam.com',
            
    receivers = ['olivia19931019@gmail.com', "360288719@qq.com"]

    while True:
        first_email_FX = ps.FX_FT_process(sender=sender, receivers=receivers, first_email_FX=first_email_FX, folder_path=pdf_from_email)
        print(first_email_FX)


    # smtpObj = ps.email_sending(
    #        subject = "testing",
    #        content = "hi there",
    #        receivers = ['olivia19931019@gmail.com', "360288719@qq.com"],
    #        sender = 'yanlaile1019@gmail.com',
    #        mail_host = 'smtp.gmail.com',
    #        mail_user = 'yanlaile1019@gmail.com',
    #        mail_pass = 'odtxybaggivhsmle',
    #        port = 465, # for ssl
    #        )

    # content = [
    # "主耶稣我的牧羊人\n",
    # "你终于寻回了你迷途多年的小羔羊\n",
    # "你于古朴的乡村牧养我\n",
    # "让我闻到初春的芳草香\n",
    # "让我仰视繁星点缀的穹苍\n",
    # "让我沉醉于秋高并气爽\n",
    # "让我历经雨雪和冰霜\n",
    #
    # "\n求学时的快乐和忧愁，你一并赐予给了我\n",
    # "我幼稚的思想在茁壮成长\n",
    # "我的灵却是愚昧，心里从未给你留下落脚的地方\n",
    #
    # "\n我迷失了道路，也听不到你的呼喊\n",
    # "我一次一次与你擦肩而过，却总是遮盖住双眼\n",
    # "我满心的空虚刚硬和忧愁\n",
    # "我周遭满是诱惑\n",
    # "我越走越偏，跌入了泥泞的路，坠入了痛苦的渊\n",
    #
    # "\n主耶稣我的牧羊人\n",
    # "你看我受尽折磨，却又起了恻隐怜爱之心\n",
    # "你原谅了我的桀骜不驯\n",
    # "你原谅了我的愚昧无知\n",
    # "你赦免了我无穷尽的罪孽，又施恩于我\n",
    # "你寻回了我，又大大地医治了我\n",
    #
    # "\n主耶稣我的牧羊人\n",
    # "我是何等的不配，这怜悯，这施恩\n",
    # "高山和低谷，你都不离不弃\n",
    # "你寻回了我，又让我遇见莹莹姊妹\n",
    # "这样的恩典，我去向谁诉说呢\n",
    #
    # "\n主耶稣我的牧羊人\n",
    # "你是我心里的王\n",
    # "我的软弱和忧虑，都有你来担当\n",
    # "我敞开心扉向你祈祷和赞美\n",
    # "你带领我们，在我们前进的方向\n",
    #
    # "\n主耶稣我的牧羊人\n",
    # "你的圣灵来到\n",
    # "我们不再彷徨\n",
    # "直到世界的末了\n",
    # "奉你宝贵的名求，阿门\n",
    # ]
    #
    # smtpObj = ps.email_sending(
    #        subject = "主耶稣我的牧羊人 -- 大卫诗读后感",
    #        content = "".join(content),
    #        )

   # ps.checkEmail_FX(
   #         first_email_FX=7,
   #         folder_path=os.path.join(ps.BASE, "att_folder")
   #         )


   # FX1_record_check = pd.read_excel(os.path.join(folder_path, "FX1 Record", "FX1 Record.xlsx"))


   # first_email_FX = ps.FX_FT_process(
   #         receivers = ['olivia19931019@gmail.com', "luge1123@gmail.com"],
   #         sender = 'yanlaile1019@gmail.com',
   #         FX1_record_check = None,
   #         first_email_FX=None,
   #         folder_path=None,
   #         test_time = [[10, 0],[10,30],[11,30]])



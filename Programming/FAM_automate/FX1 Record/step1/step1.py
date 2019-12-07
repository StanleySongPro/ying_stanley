#!/usr/bin/env python
# coding: utf-8

# # Testing file for step1

# In[5]:


import smtplib
import ssl
from email.mime.text import MIMEText
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
import os
folder_path = r"/Users/olivia/Desktop"
os.chdir(folder_path)


# ### General Functions

# In[49]:


def search_in(keyword, universe):
    """
    search 'keyword' from 'universe' to target the wanted email.
    
    """
    return bool(re.search(keyword, universe, re.IGNORECASE))


# In[30]:


def email_sending(content = None, 
                  recievers = 'olivia19931019@gmail.com',
                  port = 465, # for ssl
                  mail_host = 'smtp.gmail.com',
                  mail_user = 'yanlaile1019@gmail.com',
                  mail_pass = 'odtxybaggivhsmle',
                  sender = 'yanlaile1019@gmail.com'
                 ):
    message = MIMEText(subject,'plain','utf-8')
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = recievers[0]
    
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, port)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, recievers, content)
        smtpObj.quit()
        print ("Sent successfully...")
    except Exception as e:
        print("Exception: {}".format(e))
        
## recievers = 'olivia19931019@gmail.com'
## mail_host = 'smtp.gmail.com',mail_user = 'yanlaile1019@gmail.com',mail_pass = 'odtxybaggivhsmle',sender = 'yanlaile1019@gmail.com'


# In[151]:


# this part is for data format

def convert_to_datetime(date_str):
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

def convert_to_str(date_time):
    """
    convert datetime format from datetime to str
    """
    if type(date_time) != str:
        try:
            date_time = date_time.strftime("%m/%d/%Y")
        except:
            print(date_time,"cannot convert to str")
    
    return date_time

def convert_table_format(df):
    df = df.reset_index(drop = True)
    for i in df.index:
        df.loc[i,'Date'] = convert_to_str(df.loc[i,"Date"])
    return df
# df['Date'].apply(convert_to_str)
##,'Date'


# In[61]:


def email_saving(typ, data, folder_path = r"/Users/olivia/Desktop"):
    folder_record = os.path.join(folder_path, "FX1 Record")
    emailbody = data[0][1]
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
        try:
            fileName = decode_header(fileName)[0][0].decode(decode_header(fileNmae)[0][1])
        except:
            pass
        
        # save attachment
        if (fileName !=None) & ('jpg' not in fileName):
            filePath = os.path.join(folder_record, fileName)
            if not os.path.isfile(filePath):
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode = True))
                fp.close()
            else:
                print('Existing File:' + fileName)
                email_sending("Duplicate" + fileName, ['olivia19931019@gmail.com'])
    return fileName        


# In[181]:


def checkEmail_FX(first_email_FX = int(), 
                  folder_path = r"/Users/olivia/Desktop", 
                  mail_host = "smtp.gmail.com",
                 mail_user = "yanlaile1019@gmail.com",
                 mail_pass = 'odtxybaggivhsmle'):
    
    file_name = None
    
    # Email Login
    smtpObj = smtplib.SMTP(mail_host, 25) #???
    smtpObj.connect(mail_host, 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.ehlo()
    smtpObj.login(mail_user, mail_pass)
    
    #Inbox Scanning
    server = imaplib.IMAP4_SSL(mail_host)
    server.login(mail_user, mail_pass)
    status, messages = server.select("INBOX")
    
    # Inbox Index
    type, data = server.search(None, 'ALL')
    #print(type,data)
    mail_ids = data[0]
    #print(mail_ids)
    id_list = mail_ids.split()
    #print(id_list)
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
                if (search_in("Summary", email_subject)) & (search_in('Account',email_subject)) & (search_in("olivia", email_from))                        & (search_in('re', email_subject)==False) & (search_in('fw',email_subject)==False):
                    file_name = email_saving(typ, data,folder_path)
                    
    return file_name, latest_email_FX


# In[182]:


checkEmail_FX(first_email_FX = 7)


# In[183]:


def process_time(first_email_FX, folder_path, path_IB):
    time_now = str(datetime.now())[11:16]
    date_now = str(datetime.now())[:10]
    week_now = datetime.now().weekday()
    
    if week_now < 6: #Weekdays
        # FX1 processing
        if (time_now > "19:00") & (time_now < '19:30'):
            print(date_now)
            file_name, first_email_FX = checkEmail_FX()
            print(file_name)
            print(first_email_FX)
            #FX1_record = Record_append_FX1(folder_path, file_name)
            #generate_upload_file_FX1(folder_path, FX1_record)
            #time.sleep(6*3)
            
        # FX1 status check
        elif (time_now > "19:30") & (time_now < "20:00"):
            FX1_record_check = pd.read_excel(folder_path + '/FX1 Record/DailyBAL_consolidated.xls')
            if (datetime.today() - convert_to_datetime(list(FX1_record_check["Business Date"])[-1])).days == int(np.where(week_now == 0,3,1)):
                print("Upload successfully")
                email_sending("upload successfully!",'olivia19931019@gmail.com')
            else:
                print("Problem with uploading file, pls check")
                email_sending("Problem with uploading file, pls check",'olivia19931019@gmail.com')
            print("\n")
            #time.sleep(10*10*2)
        else:
            pass
    else:  # weekends
        pass
    
    return first_email_FX
    


# In[184]:


process_time(first_email_FX, folder_path, path_IB=None)


# In[185]:


while True:
    first_email_FX = process_time(first_email_FX, folder_path,path_IB=None)
    print(first_email_FX)
    #time.sleep(20*60)


# #### folder_path
# 

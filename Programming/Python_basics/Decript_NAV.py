# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 10:12:48 2019

@author: FAM01
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import shutil
from PyPDF2 import PdfFileReader, PdfFileWriter
import os, inspect
from datetime import datetime
from zipfile import ZipFile
from zipfile import ZIP_DEFLATED, ZIP_STORED, ZIP_BZIP2, ZIP_LZMA
import sys
import win32com.client


#%%
class DecryptAtt():
    def __init__(self, BASE=None):
        self.BASE = BASE

    def decrypt_xls(self,):
        pass


    def excel_decrypt(self, src_file=None, out_file=None, password=None):
        xlapp = win32com.client.Dispatch("Excel.Application")
        wb = xlapp.Workbooks.Open(
            Filename=src_file, 
            UpdateLinks=False, 
            ReadOnly=True, 
            Format=None, 
            Password=password)
##        xlapp.DisplayAlerts = False
        xlapp.DisplayAlerts = True
        obj = xlapp.ActiveWorkbook.SaveAs
        xlapp.ActiveWorkbook.SaveAs(
            Filename=out_file,
            FileFormat=None,
            Password="",
            WriteResPassword="")
        wb.Close()
        xlapp.Quit()
        print("decrypt success![%s]" % password)


  

    def current(self):
        result = datetime.now()
        return result


    def getDateStr(self, d=None, format_str='%Y-%m-%d_%H-%M-%S'):
        return datetime.strftime(d,format_str)


    def currentStr(self):
        return self.getDateStr(d=self.current())


    def mypath(self, file=None):
        return os.path.dirname(os.path.abspath(file))


    def printfilename(self, file= None):
        print("---------------------------------------------")
        print("path : {}".format(os.path.abspath(file)))
        print("file_name : {}".format(os.path.basename(file)))


    def walkdir(self, path=None, func=None):
        for root,dirs,files in os.walk(path):
            for file in files:
                func(file)

#    def walkdir(self, path=None, func=None):
#        mylst = [func(file) for _, _, files in os.walk(path) for file in files]



    
  


  
#%%
if __name__ == '__main__':

    BASE = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    decryptAtt = DecryptAtt(BASE=BASE)
    
    pdf_from_email = os.path.join(BASE, "att_folder", "pdf_from_email")
    pdf_from_email_dcrpt = os.path.join(BASE, "att_folder", "pdf_decrypt")
    if not os.path.isdir(pdf_from_email_dcrpt):
        os.mkdir(pdf_from_email_dcrpt)
    pdf_to = os.path.join(BASE, "att_folder", "pdf_to")
    if not os.path.isdir(pdf_to):
        os.mkdir(pdf_to)

    
    src_file = os.path.join(pdf_to, "DailyBAL_211391500.xls")
    out_file = os.path.join(pdf_from_email_dcrpt, "DailyBAL_211391500.xls")
    password = "123"    
    obj = decryptAtt.excel_decrypt(src_file=src_file, out_file=out_file, password=password)
        

    print(help(obj))



#######################################################################################
##
##
##    # 1. 解压解密 pdf_from_email
##    filename = os.path.join(pdf_from_email, "testfile.zip")
##    pwd=b'123456'
##    decryptAtt.unzip(filename = filename, path = pdf_to, pwd=pwd)
##
##    # Step 1 and 2之间未来需要衔接
##    # 2. decrypt pdf_to 里面的所有的 pdf
##    # 3. 文件保存在pdf_dcrpt
##
##    pdf_files = list(i for i in os.listdir(pdf_to) if i.endswith(".pdf"))
##    pdf_file_paths = list(os.path.join(pdf_to, i) for i in pdf_files)
##    output_file_paths = list(os.path.join(pdf_from_email_dcrpt, i) for i in pdf_files)
##    password = b'123456'
##
##    for i, input_file_path in enumerate(pdf_file_paths):
##        decryptAtt.decrypt_pdf(
##                input_file_path=input_file_path,
##                output_file_path=output_file_paths[i],
##                password=password)
##########################################################################################
#    input_file_path = os.path.join(BASE, 'test encrypted.pdf')
#    output_file_path = os.path.join(BASE, 'decrypted.pdf')
#
#    password = '123456'
#    decryptAtt.decrypt_pdf(
#            input_file_path=input_file_path,
#            output_file_path=output_file_path,
#            password=password)

#    print(decryptAtt.mypath(file=output_path))
#    print(decryptAtt.printfilename(file=output_path))

#    start = datetime.now()
#    print(decryptAtt.walkdir_1(path=BASE, func=decryptAtt.printfilename))
#    end = datetime.now()
#    time1 = end - start
#
#
#    start = datetime.now()
#    print(decryptAtt.walkdir(path=BASE, func=decryptAtt.printfilename))
#    end = datetime.now()
#    time2 = end - start
#
#    print("Time taken : {}".format(time1))
#    print("Time taken : {}".format(time2))

#    filename = os.path.join(BASE, "att_folder", "testfile.zip")
#    filedir = os.path.join(BASE, "att_folder")
#    pwd = "123456"
#    decryptAtt.unzip(filename=filename, path=filepath, pwd=pwd)


#    zipname = os.path.join(BASE, "att_folder", "pdfs.zip")
#    logdir = os.path.join(BASE, "att_folder", "pdfs")
#    pwd = "123456"
#    zipf = decryptAtt.zipdir(logdir=logdir, zipname=zipname, pwd=pwd)

#    tempdir = decryptAtt.currentStr()


#    logdir = pdf_from_email
#    zipname = os.path.join(BASE, "att_folder", "pdf_from_email.zip")
#    pwd = "yingying"
#    decryptAtt.zipdir(logdir=logdir, zipname=zipname, pwd=pwd)

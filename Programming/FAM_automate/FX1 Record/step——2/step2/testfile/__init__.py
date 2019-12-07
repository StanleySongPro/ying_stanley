from zip import unzip, zipdir
from path import mypath
import os
from removeZipPassword import removeZipPassword
from file import walkdir
from date import currentString

current_path = mypath(__file__)

filename = 'protect.zip'
filename = current_path+'/' + 'protect.zip';
tempdir = currentString()

# un zip filename with password 123456 and save to temp dir
unzip(filename,tempdir,b'123456')


# # zipdir(temp_folder,'noprotect.zip')
# 
# removeZipPassword(filename,'noprotectaaaa.zip',b'123456')

def printfilename(file):
    print(os.path.abspath(file),os.path.basename(file))
    
walkdir(tempdir,printfilename)


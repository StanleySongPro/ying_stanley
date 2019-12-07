import os
from date import currentString
from zip import unzip, zipdir
import shutil
# from com.finexisam.utils.path import mypath

def removeZipPassword(filename,saveas,pwd):
    tempdir = currentString()
#     
    savepath = os.path.dirname(saveas)
    savename = os.path.basename(saveas)
    
    os.mkdir(tempdir)
    unzip(filename,tempdir,b'123456')
    zipdir(tempdir,saveas)
    shutil.rmtree(tempdir)

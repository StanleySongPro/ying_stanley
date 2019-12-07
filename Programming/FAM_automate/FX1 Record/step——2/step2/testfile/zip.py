from zipfile import ZipFile,ZIP_DEFLATED
import os

    
    
def unzip(filename,path=None,pwd=None,):
    with ZipFile(filename) as zf:
        zf.extractall(path,pwd=pwd)
    
def zipdir(path,filename,pwd=None):
    zipf = ZipFile(filename, 'w', ZIP_DEFLATED)
    for root, dirs, files in os.walk(path):
        for file in files:
            zipf.write(os.path.join(root, file))
    if (pwd):
        zipf.setpassword(pwd)
    zipf.close()
    

if __name__ == '__main__':
    pass
    
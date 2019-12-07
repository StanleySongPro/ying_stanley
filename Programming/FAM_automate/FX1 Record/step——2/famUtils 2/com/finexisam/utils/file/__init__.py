import os
def walkdir(path,func):
    for root, dirs, files in os.walk(path):
        for file in files:
            func(file)
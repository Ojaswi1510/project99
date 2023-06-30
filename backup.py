import os
import shutil

source=input('enter the source folder path')
destination=input('enter the destination folder path')

source=source+'/'
destination=destination+'/'

list_files=os.listdir(source)
for file in list_files:
    shutil.copy((source+file),destination)
    
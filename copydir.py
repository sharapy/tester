# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 20:12:42 2015
Author: Sharad Talekar
Purpose: Program to create backup of files in some folder
"""
import os
import time
import shutil

source = "C:\\GAME\\Py"
#str(source)

target_dir = "C:\\GAME\\Sharad\\Programs"

target_dir = str(target_dir) + os.sep + time.strftime('%Y%m%d%H%M%S')

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    
copy_command = "copy {0} {1}".format(source,target_dir)


print("Copy command is")
print(copy_command)
print("Running:")
if os.system(copy_command) == 0:
        print("Successful backup to",target_dir)
else:
        print("Backup Failed")

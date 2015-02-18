# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 20:12:42 2015
Author: Sharad Talekar
Purpose: Program to create backup of files in some folder
"""
import os
import time

source = "C:\\GAME\\Py"
#str(source)

target_dir = "C:\\GAME\\Sharad\\Programs"

target = str(target_dir) + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    
zip_command = "zip -r {0} {1}".format(target,''.join(source))


print("Zip command is")
print(zip_command)
print("Running:")
if os.system(zip_command) == 0:
        print("Successful backup to",target)
else:
        print("Backup Failed")

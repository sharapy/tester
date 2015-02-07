# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 22:36:34 2015
@author: SharadTalekar
"""
count = int(input("Enter the no of samples: "))
interval = int(input("Enter the sample interval in seconds: "))
import psutil, time, csv
i=0
with open('CPU1.csv','w', newline ='') as csvfile:
    cpuwriter = csv.writer(csvfile)
    while i <= count:
        cpuvalue = psutil.cpu_percent(interval=0)        
        cpuwriter.writerow([cpuvalue])
        i = i + 1
        time.sleep(interval)
csvfile.close()

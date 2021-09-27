# Nanruan_Killer Python Edition
# Version 1.01
# Author: zhouxuanyi
# License: MIT
# 2021/9/27 22.47

import os
import sys

def pssuspend():
    print("使用pssuspend挂起进程")
    print(pssuspend)
    path = sys.path[1]
    print(path)
    pssuspendfile = path + "\pssuspend.exe"
    pssuspendfile = pssuspendfile + " StudentMain.exe"
    print(pssuspendfile)
    os.system("chcp 65001")
    os.system(pssuspendfile)
    
def taskkill():
    print("使用任务管理器结束进程")
    os.system("taskkill /F /T /IM StudentMain.exe")

def pskill():
    print("使用pskill结束进程")
    pskill = sys.path[1]
    pskill = pskill + "\pskill.exe"
    pskill = pskill + " -t StudentMain.exe"
    os.system("chcp 65001")
    os.system(pskill)




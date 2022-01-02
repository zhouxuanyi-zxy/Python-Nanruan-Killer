# Nanruan_Killer Python Edition
# Version 1.03
# Author: zhouxuanyi
# License: MIT
# 2021/9/27 22.47
# 2021/10/2 14:46
# 2021/12/11 11:34

import os
import sys
import os.path

def file():
    if os.path.isfile("pssuspend.exe"):
        if os.path.isfile("pskill.exe"):
            if os.path.isfile("ntsd.exe"):
                print("文件检测完毕！")
            else:
                print("缺少ntsd.exe!")
                exit()
        else:
            print("缺少pskill.exe!")
            exit()
    else:
        print("缺少pssuspend.exe！")
        exit()

def pssuspend():
    os.system("chcp 65001")
    print("使用pssuspend挂起进程")
    pssuspendfilepath = sys.path[0]
    #pssuspendfile = path + "\pssuspend.exe"
    #pssuspendfile = pssuspendfile + " StudentMain.exe"
    pssuspendfile = pssuspendfilepath + r"\pssuspend.exe StudentMain.exe"
    print(pssuspendfile)
    os.system(pssuspendfile)
    
def taskkill():
    print("使用任务管理器结束进程")
    os.system("taskkill /F /T /IM StudentMain.exe")

def pskill():
    os.system("chcp 65001")
    print("使用pskill结束进程")
    pskill = sys.path[0]
    #pskill = pskill + "\pskill.exe"
    #pskill = pskill + " -t StudentMain.exe"
    pskill = pskill + r"\pskill.exe -t StudentMain.exe"
    print(pskill)
    os.system(pskill)

def ntsd():
    os.system("chcp 65001")
    print("使用ntsd结束进程")
    ntsd = sys.path[0]
    ntsd = ntsd + r"\ntsd.exe -c q -pn StudentMain.exe"
    print(ntsd)
    os.system(ntsd)


print("------ by zhouxuanyi_zxy ------")
file()
pssuspend()
taskkill()
pskill()
ntsd()
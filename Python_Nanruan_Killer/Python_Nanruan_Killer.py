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

from win32con import SW_HIDE

try:
    import win32gui
    import win32con
except:
    os.system("pip install pywin32")
    os.system("python Python_Nanruan_Killer.py")
    exit()


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


# toplist = []
# winlist = []
# def enum_callback(hwnd, results):
    #winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

# def minimize():
    # '''
    # fuc:♾️循环最小化窗口
    # by：麒麟编程黄老师
    # time: 2022.01.13
    # '''
    #global toplist, winlist
    #while True:
        #win32gui.EnumWindows(enum_callback, toplist)
        #firefox = [(hwnd, title) for hwnd, title in winlist if 'studentmain.exe' in title.lower()]
        # 获取首个窗口句柄
        #firefox = firefox[0]
        # 最小化窗口
        #win32gui.ShowWindow(firefox[0], win32con.SW_MINIMIZE)

def studentmain_small():
    while True:
        handle = win32gui.FindWindow(None,"TDDesk Render Window")
        title = win32gui.GetWindowText(handle) # 标题
        clsname = win32gui.GetClassName(handle) # 类名
        print(title,clsname)
        studentmain = win32gui.FindWindow(clsname,title)
        print(studentmain)
        win32gui.ShowWindow(studentmain,win32con.SW_HIDE)
    
print("------ by zhouxuanyi_zxy ------")
# file()
# pssuspend()
# taskkill()
# pskill()
# ntsd()
# -- 只最小化，已注释其他功能
# TDDesk Render Window 测试时的标题
# Afx:02330000:b:00000000:00000006:0004032F 测试时的类名
studentmain_small()
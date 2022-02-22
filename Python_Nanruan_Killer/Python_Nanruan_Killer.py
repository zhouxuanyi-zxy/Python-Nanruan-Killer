# Nanruan_Killer Python Edition
# Version 1.06-pre2
# Author: zhouxuanyi
# License: MIT
# 2021/9/27 22.47
# 2021/10/2 14:46
# 2021/12/11 11:34
# 2022/1/14 23:48
# 2022/2/22 22:51

import os
import sys

try:
    import win32gui
    import win32con
except:
    os.system("pip install pywin32")
    os.system("python Python_Nanruan_Killer.py")
    exit()

def kill():
    file()
    taskkill()
    pskill()
    ntsd()
    pssuspend()

def hide():
    studentmain_hide()

def show():
    studentmain_show()

def start():
    print("*"*40)
    print("1、直接杀死南软进程\n")
    print("2、最小化南软窗口(演播室)\n")
    print("3、重新启动南软(需输入路径)\n")
    print("4、取消演播室最小化\n")
    print("*"*40)
    user_select = int(input())
    if user_select == 1:
        kill()
    elif user_select == 2:
        hide()
    elif user_select == 3:
        kill_path = str(input("请输入南软的路径(不能有空格,路径有空格请在那一部分打上''):"))
        os.system(kill_path)
    elif user_select == 4:
        studentmain_show()
    else:
        exit()

def file():
    if os.path.isfile("pssuspend.exe"):
        if os.path.isfile("pskill.exe"):
            if os.path.isfile("ntsd.exe"):
                print("文件检测完毕!")
            else:
                print("缺少ntsd.exe!")
                exit()
        else:
            print("缺少pskill.exe!")
            exit()
    else:
        print("缺少pssuspend.exe")
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

# def minimize():
    # '''
    # fuc:♾️循环最小化窗口
    # by：麒麟编程黄老师
    # time: 2022.01.13
    # '''
    #global toplist, winlist
    # toplist = []
    # winlist = []
    # def enum_callback(hwnd, results):
        #winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
    #while True:
        #win32gui.EnumWindows(enum_callback, toplist)
        #firefox = [(hwnd, title) for hwnd, title in winlist if 'studentmain.exe' in title.lower()]
        # 获取首个窗口句柄
        #firefox = firefox[0]
        # 最小化窗口
        #win32gui.ShowWindow(firefox[0], win32con.SW_MINIMIZE)

def studentmain_hide():
    while True:
        #handle = win32gui.FindWindow(None,"TDDesk Render Window") 极域窗口名称
        handle = win32gui.FindWindow(None,"屏幕演播室窗口") # 南软演播室窗口名称,目前还在寻找"保持安静"的窗口
        title = win32gui.GetWindowText(handle) # 标题
        clsname = win32gui.GetClassName(handle) # 类名
        print(title,clsname)
        studentmain = win32gui.FindWindow(clsname,title)
        print(studentmain)
        win32gui.ShowWindow(studentmain,win32con.SW_HIDE)

def studentmain_show():
    while True:
        #handle = win32gui.FindWindow(None,"TDDesk Render Window") 极域窗口名称
        handle = win32gui.FindWindow(None,"屏幕演播室窗口") # 南软演播室窗口名称
        title = win32gui.GetWindowText(handle) # 标题
        clsname = win32gui.GetClassName(handle) # 类名
        print(title,clsname)
        studentmain = win32gui.FindWindow(clsname,title)
        print(studentmain)
        win32gui.ShowWindow(studentmain,win32con.SW_SHOW)
    
print("------ by zhouxuanyi_zxy ------")

start()

# TDDesk Render Window 极域测试时的标题
# Afx:02330000:b:00000000:00000006:0004032F 极域测试时的类名
# 屏幕演播室窗口 南软测试时的标题
# Afx:00400000:3:00000000:00000006:001300F9 南软测试时的类名
# Nanruan_Killer Python Edition
# Version 1.06
# Author: zhouxuanyi
# License: MIT
# 2021/9/27 22.47
# 2021/10/2 14:46
# 2021/12/11 11:34
# 2022/1/14 23:48
# 2022/2/22 22:51
# 2022/6/26 19:52
# 2024/2/9 21:21

import os
import sys
import winreg
import ctypes
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

# def hide():
#     studentmain_hide()

# def show():
#     studentmain_show()

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

def find_program_path():
    reg = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)
    reg = winreg.OpenKey(reg,r"SOFTWARE\TopDomain\e-Learning Class Standard\1.00")
    studentmain_path = winreg.QueryValueEx(reg,"TargetDirectory")
    studentmain_path = studentmain_path[0]
    print("南软(极域)路径为:",studentmain_path)
    winreg.CloseKey(reg)
    ''' 
    以下为删除南软(极域)的注册表(WIP)
    删除后可无密码卸载
    '''
    # try:
    #     reg = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)
    #     reg = winreg.OpenKey(reg,r"SOFTWARE\TopDomain")
    #     # reg = winreg.EnumKey(reg,0)
    #     # winreg.DeleteKey(reg,"1")
    #     for i in range(114514):
    #         try:
    #             keys = winreg.EnumKey(reg,i)
    #             print(keys)
    #             reg1 = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)
    #             reg1 = winreg.OpenKey(reg1,r"SOFTWARE\TopDomain\{}".format(keys))
    #             keys_in = winreg.QueryValue(reg1,"1")
    #             print(keys_in)
    #             # winreg.DeleteKey(reg,keys)
    #         except OSError:
    #             break;
    #     print(keys)
    #     winreg.DeleteKey(reg,r"TopDomain")
    #     print("现在已删除其的注册表,你也可以直接卸载了")
    #     return studentmain_path
    # except:
    #     return studentmain_path
    return studentmain_path
    
def rename_eXchange20_dll():
    studentmain_path = find_program_path()
    try:
        os.rename(studentmain_path+"eXchange20.dll",studentmain_path+"eXchange20.dll.1")
    except:
        pass
    # print("是否注销?")
    # shutdown_l = int(input())
    shutdown_l = 0 # 考虑到真实环境中并不见得有机会做这个选择
    if shutdown_l == 1:
        os.system("shutdown /l")

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

print("is_admin =",ctypes.windll.shell32.IsUserAnAdmin())
if ctypes.windll.shell32.IsUserAnAdmin() == 0:
    ctypes.windll.shell32.ShellExecuteW(None,"runas",sys.executable,__file__,None,1)
    # print(ctypes.windll.shell32.IsUserAnAdmin())
    # os.system("python Python_Nanruan_Killer.py")
else:
    rename_eXchange20_dll()
    find_program_path()
    taskkill()
    pskill()
    ntsd()
    os.system("pause")
# 回退了 Pre-2 中的选择界面
# TDDesk Render Window 极域测试时的标题
# Afx:02330000:b:00000000:00000006:0004032F 极域测试时的类名
# 屏幕演播室窗口 南软测试时的标题
# Afx:00400000:3:00000000:00000006:001300F9 南软测试时的类名

# Python-Nanruan-Killer

[![License](https://img.shields.io/badge/license-MIT-svg)](https://github.com/zhouxuanyi-zxy/Python-Nanruan-Killer/blob/master/LICENSE)

一个让老师无法控制你的小软件，使用pssuspend挂起进程、taskkill结束进程、pskill结束进程、ntsd结束进程、win32gui和win32con最小化窗口。（ntsd在Windows 10 21H2无法使用，但在Windows 7 可以使用）已开发完成，后续会继续保持更新。

## 使用说明
请下载**pssuspend.exe**和**pskill.exe**和**ntsd.exe**及**程序主文件**    
之后在信息课拼手速插U盘点开程序即可破解  
**此软件所有版本都可以保证进程被结束，因为pskill我在2021/10/16已经测试通过，可以结束进程；也可以保证进程可以被挂起**  ![Windows 7 x64-2021-10-16-14-06-51](https://user-images.githubusercontent.com/69704410/137575937-a9a2ee5e-91f3-465f-8eed-709ee8e551dd.png)

如果无法访问[GitHub](https://github.com/zhouxuanyi-zxy/Python-Nanruan-Killer)，也可以访问[Gitee的地址](https://gitee.com/zhouxuanyi/Python-Nanruan-Killer),(gitee上不更新，只有结束进程需要的文件)

### 最后的话
最后，祝各位可以在信息课上玩的开心。

### 版本更新历史
v1.01 (2021.9.27-2021.10.2)、1.02(2021.10.4)
首个版本
+ pssuspend挂起进程
+ taskkill结束进程
+ pskill结束进程

v1.03 (2021/12/11)
+ 自动下载文件 (download.py)

v1.04 (2022/1/2)
+ 在 Python_Nanruan_Killer.py 中增加文件完整性检测

v1.05 (2022/1/2)

重要更新
+ ntsd 强制结束进程
+ 自动下载ntsd (download.py)

v1.06 Pre1 (2022/1/14)

重大更新

+ 使用pywin32中的win32gui和win32con来最小化极域的演示和黑屏

- 暂时关闭了所有结束进程和挂起进程的功能

+ 预计1.06 Pre2会改回来

v1.06 Pre2 (2022/2/22)

+ 开始执行程序时的选择
+ 支持把演播室的画面重新显示
+ 修改了南软演播室的标题

请注意：

1、极域和南软几乎一致，在此程序中只有窗口标题不一致，可自行取消注释

2、在输入路径时，如果路径中有空格，请用''包裹整个路径(如：C:\Program Files\12345.exe,在输入时输入: 'C:\Program Files\123456.exe')

3、此版本bug可能比较多，请谅解
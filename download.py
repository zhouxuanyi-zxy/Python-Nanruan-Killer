# Nanruan_Killer Python Edition
# Version 1.03
# Author: zhouxuanyi
# License: MIT
# 2021/12/11 11:23

import requests
import os

print ("Downloading Pskill")
# pskillurl = 'https://github.com/zhouxuanyi-zxy/Python-Nanruan-Killer/raw/master/pskill.exe'  # GitHub源
pskillurl = 'https://gitee.com/zhouxuanyi/Python-Nanruan-Killer/raw/master/pskill.exe' # Gitee源
r = requests.get(pskillurl)
with open("pskill.exe", "wb") as code:
  code.write(r.content)

print ("Downloading Pssuspend")
# pssuspendurl = 'https://github.com/zhouxuanyi-zxy/Python-Nanruan-Killer/raw/master/pssuspend.exe  # GitHub源
pssuspendurl = 'https://gitee.com/zhouxuanyi/Python-Nanruan-Killer/raw/master/pssuspend.exe' # Gitee源
r = requests.get(pssuspendurl)
with open("pssuspend.exe", "wb") as code:
  code.write(r.content)

print ("Downloading .....")
killerurl = 'https://raw.githubusercontent.com/zhouxuanyi-zxy/Python-Nanruan-Killer/master/Python_Nanruan_Killer/Python_Nanruan_Killer.py' 
r = requests.get(killerurl)
with open("Python_Nanruan_Killer.py", "wb") as code:
  code.write(r.content)

os.system("python Python_Nanruan_Killer.py")

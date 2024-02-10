# Nanruan_Killer Python Edition Python x86 Downloader
# Version 1.06-pre1
# Author: zhouxuanyi
# License: MIT
# -*- coding: utf-8 -*-

import requests
import os
import sys

print ("Downloading Python 3.8.6")
pythonurl = 'https://www.python.org/ftp/python/3.8.6/python-3.8.6.exe' 
r = requests.get(pythonurl)
with open("python-3.8.6.exe", "wb") as code:
  code.write(r.content)

python = sys.path[0]
python = python + r"\python-3.8.6.exe /passive CompileAll=1"

os.system(python)

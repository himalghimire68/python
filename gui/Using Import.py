'''from file1 import *
print(name,",",age,",",place)
'''
'''
import datetime as dt
import time

print(dt.date.today())
print("Formatted Time:",time.asctime())

'''
'''
import webbrowser
a=input("Search Video:")
print("Opening Browser")
webbrowser.open_new_tab('https://youtube.com/search?q=%s'%a)
'''

import os
print("My current Working directory:",os.getcwd())
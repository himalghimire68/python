'''from file1 import *
print(name,",",age,",",place)
'''

#Date Time Functions
'''
import datetime as dt
import time

print(dt.date.today())
print("Formatted Time:",time.asctime())

'''
#opening Link
'''
import webbrowser
a=input("Search Video:")
print("Opening Browser")
webbrowser.open_new_tab('https://youtube.com/search?q=%s'%a)
'''

#Current Working Directory
'''
import os
print("My current Working directory:",os.getcwd())

'''

#Mathematical Functions
'''
import math
num=int(input("Enter a num:"))
print("Factorial:",math.factorial(num))
'''

#Putting Color on output texts
'''
from termcolor import colored

print(colored("hello","blue","on_grey"),colored('World','green','on_red'))

text= colored('color look nice!!!','blue', attrs=['reverse','blink'])
print(text)
'''

input_email=input("Enter Email address:")
input_pass=input("Input Password:")

def valid(input_email,input_name):
    if re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z", input_email, re.IGNORECASE) and input_name.isalpha()==False:
        print("valid")
    else:
        print("Email is invalid")





from tkinter import *
import re

spy = Tk()
spy.geometry("300x300")

# user_name= StringVar()
# pass_word = StringVar()
# e_mail = StringVar()
# Label(spy,text="Username").grid()
# input_name = Entry(spy,textvariable=user_name).grid(row=0,column=1)
# Label(spy,text="Password").grid()
# input_pass = Entry(spy,textvariable=pass_word).grid(row=1,column=1)
# Label(spy,text="Email").grid()
# input_email = Entry(spy,textvariable=e_mail).grid(row=2,column=1)
#
# submit= Button(spy,text="Submit",command=lambda :valid(input_email,input_name)).grid(row=4,column=1)

spy.mainloop()
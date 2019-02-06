from tkinter import *

root=Tk()
root.geometry("400x400")
#root.title()
title= Label(root,text='First', font=("",32))
title.pack()
name=StringVar()
age=StringVar()
Label(root, text="Name:").pack()
name=Entry(root,textvariable=name,)
name.pack(padx=(10),pady=(10))
Label(root, text="Enter Age")
age=Entry(root,textvariable=age)
age.pack(padx=(10))
out=Label(root,text=" ")
out.pack()



sub=Button(root,text="Submit",command=lambda : print(name.get(),age.get()))
sub.pack()

root.mainloop()

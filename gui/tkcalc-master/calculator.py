from tkinter import *


cal=Tk()
cal.title("Simple Calculator")
cal.geometry("500x500")
'''
result_box_label = StringVar()
result_box = Label(cal)
result_box.grid(row=0, column=0)
result_box.config(width=20, height=3, textvariable=result_box_label, justify="right", font=("Helvetica", 13, "bold"))
insert_box_label = StringVar()
insert_box =Label(cal)
insert_box.grid(row=1, column=0)
insert_box.config(width=20, height=3, textvariable=insert_box_label, justify="right")
'''
name= StringVar
Label(cal, text="Name:").grid(row=1,column=1)
name=Entry(cal,textvariable=name)
name.grid(row=1,column=3,padx=(10),pady=(10))


#First Row

sub=Button(cal,text="1",padx=20,pady=15)
sub.grid(row=3,column=2)
sub=Button(cal,text="2",padx=20,pady=15)
sub.grid(row=3,column=3)
sub=Button(cal,text="3",padx=20,pady=15)
sub.grid(row=3,column=4)
sub=Button(cal,text="-",padx=20,pady=15,font=("Helvetica", 13, "bold"))
sub.grid(row=3,column=5)

# Second Row
sub=Button(cal,text="4",padx=20,pady=15)
sub.grid(row=4,column=2)
sub=Button(cal,text="5",padx=20,pady=15)
sub.grid(row=4,column=3)
sub=Button(cal,text="6",padx=20,pady=15)
sub.grid(row=4,column=4)
sub=Button(cal,text="*",padx=20,pady=15,font=("Helvetica", 13, "bold"))
sub.grid(row=4,column=5)

#Third Row
sub=Button(cal,text="7",padx=20,pady=15)
sub.grid(row=5,column=2)
sub=Button(cal,text="8",padx=20,pady=15)
sub.grid(row=5,column=3)
sub=Button(cal,text="9",padx=20,pady=15)
sub.grid(row=5,column=4)
sub=Button(cal,text="/",padx=20,pady=15,font=("Helvetica", 13, "bold"))
sub.grid(row=5,column=5)

#Furth Roow
sub=Button(cal,text=".",padx=20,pady=15,font=("Helvetica", 13, "bold"))
sub.grid(row=6,column=2)
sub=Button(cal,text="0",padx=20,pady=15)
sub.grid(row=6,column=3)
sub=Button(cal,text="+",padx=20,pady=15,font=("Helvetica", 13, "bold"))
sub.grid(row=6,column=4)
sub=Button(cal,text="=",padx=20,pady=15,font=("Helvetica", 13, "bold"))
sub.grid(row=6,column=5)




cal.mainloop()








'''
inp_in()=StringVar()
operator=""

def click(numbers):
    glbal operator
    operator = operator+str(numbers)
    inp_in.set(operator)

def equal():
    global operator
    add=str(eval(operator))
    inp_in.set(add)
    operator=''

def equal():
    global operator
    add=str(eval(operator))
    inp_in.set(sub)
    operator=''


'''
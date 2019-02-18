


from tkinter import *

root=Tk()
root.geometry("400x400")
#root.title()
title= Label(root,text='First', font=("",32))
title.pack()
name=StringVar()
age=StringVar()
Label(root, text="Name:").pack()
name=Entry(root,textvariable=name)
name.pack(padx=(10),pady=(10))
Label(root, text="Enter Age")
age=Entry(root,textvariable=age)
age.pack(padx=(10))
#out=Label(root,text=" ")
#out.pack()



sub=Button(root,text="Submit",command=lambda : print(name.get(),age.get()))
sub.pack()

root.mainloop()













'''
    This script was written in python 3.x.
    In order to run this script, please make sure your python version is 3.x or above.
    How to run:
        python App.py
    or if it doesn't work use this one:
        python3 App.py
    Author: Udin <just.udin@yahoo.com>
'''

'''
from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Frame, Label, Entry

class App(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Calculator by Udin")
        self.pack(fill=BOTH, expand=True)
        global value
        value = 0
        global num1
        num1 = StringVar()
        global num2
        num2 = StringVar()
        global res
        res = StringVar()

        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Input Number 1 :", width=15)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        entry1 = Entry(frame1,textvariable=num1)
        entry1.pack(fill=X, padx=5, expand=True)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Input Number 2 :", width=15)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        entry2 = Entry(frame2,textvariable=num2)
        entry2.pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=X)

        btnplus = Button(frame3, text="+", width=8, command=self.plus)
        btnplus.pack(side=LEFT, anchor=N, padx=5, pady=5)

        btnminus = Button(frame3, text="-", width=8, command=self.minus)
        btnminus.pack(side=LEFT, anchor=N, padx=5, pady=5)

        btnmul = Button(frame3, text="*", width=8, command=self.mul)
        btnmul.pack(side=LEFT, anchor=N, padx=5, pady=5)

        btndiv = Button(frame3, text="/", width=8, command=self.div)
        btndiv.pack(side=LEFT, anchor=N, padx=5, pady=5)

        frame4 = Frame(self)
        frame4.pack(fill=X)

        lbl3 = Label(frame4, text="Result :", width=10)
        lbl3.pack(side=LEFT, padx=5, pady=5)

        result = Entry(frame4,textvariable=res)
        result.pack(fill=X, padx=5, expand=True)

    def errorMsg(self,msg):
        if msg == 'error':
            tkinter.messagebox.showerror('Error!', 'Something went wrong! Maybe invalid entries')
        elif msg == 'divisionerror':
            tkinter.messagebox.showerror('Division Error', 'The value of input number 2 is 0. No dividing by 0')

    def plus(self):
        try:
            value = float(num1.get()) + float(num2.get())
            res.set(self.makeAsItIs(value))
        except:
            self.errorMsg('error')

    def minus(self):
        try:
            value = float(num1.get()) - float(num2.get())
            res.set(self.makeAsItIs(value))
        except:
            self.errorMsg('error')

    def mul(self):
        try:
            value = float(num1.get()) * float(num2.get())
            res.set(self.makeAsItIs(value))
        except:
            self.errorMsg('error')

    def div(self):
        # checks if user is trying to divide by zero
        if num2.get() == '0':
            self.errorMsg('divisionerror')
        elif num2.get() != '0':
            try:
                value = float(num1.get()) / float(num2.get())
                res.set(self.makeAsItIs(value))
            except:
                self.errorMsg('error')

    def makeAsItIs(self, value):
        if (value == int(value)):
            value = int(value)
        return value

def main():
    root = Tk()
    root.geometry("300x140")
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()
'''


'''
import tkinter as tk

root = tk.Tk()
colour = 'cyan'
root.configure(background=colour, width=70)
button_width = 7
button_height = 3
first_number = 0
operator = ""


"""insert box & result box"""
result_box_label = tk.StringVar()
result_box = tk.Label(root)
result_box.grid(row=0, column=0)
result_box.config(width=30, height=3, background=colour, textvariable=result_box_label, justify="right", font=("Helvetica", 13, "bold"))
insert_box_label = tk.StringVar()
insert_box = tk.Label(root)
insert_box.grid(row=1, column=0)
insert_box.config(width=30, height=3, background=colour, textvariable=insert_box_label, justify="right")


def convertstr(s):
    """Convert string to either int or float."""
    try:
        result = int(s)
    except ValueError:
        result = float(s)
    return result


def add():
    b = result_box_label.get()
    a = insert_box_label.get()
    if (a != '' and b == '') or (a != '' and b != ''):
        result_box_label.set('')
        globals()["first_number"] = a
        globals()["operator"] = "+"
        insert = a+"+"
        result_box_label.set(insert)
        insert_box_label.set('')


def substract():
    b = result_box_label.get()
    a = insert_box_label.get()
    if (a != '' and b == '') or (a != '' and b != ''):
        result_box_label.set('')
        globals()["first_number"] = a
        globals()["operator"] = "-"
        insert = a + "-"
        result_box_label.set(insert)
        insert_box_label.set('')


def multiply():
    b = result_box_label.get()
    a = insert_box_label.get()
    if (a != '' and b == '') or (a != '' and b != ''):
        result_box_label.set('')
        globals()["first_number"] = a
        globals()["operator"] = "*"
        insert = a + "*"
        result_box_label.set(insert)
        insert_box_label.set('')


def divide():
    b = result_box_label.get()
    a = insert_box_label.get()
    if (a != '' and b == '') or (a != '' and b != ''):
        result_box_label.set('')
        globals()["first_number"] = a
        globals()["operator"] = '/'
        insert = a + "/"
        result_box_label.set(insert)
        insert_box_label.set('')


def result_of_operation():
    b = result_box_label.get()
    a = insert_box_label.get()
    if a != '' and b != '':
        second_number = a
        #second_number = second_number[0:-1]
        if operator == '+':
            result = convertstr(first_number)+convertstr(second_number)
        elif operator == '-':
            result = convertstr(first_number) - convertstr(second_number)
        elif operator == '*':
            result = convertstr(first_number) * convertstr(second_number)
        elif operator == '/' and second_number == "0":
            result = "you can not divide by zero"
        else:
            result = convertstr(first_number)/convertstr(second_number)
        result1 = str(first_number)+operator+str(second_number)+'='+str(result)
        result_box_label.set('')
        insert_box_label.set('')
        result_box_label.set(result1)


def clear():
    insert_box_label.set('')
    result_box_label.set('')


def ce():
    insert_box_label.set('')


def back():
    a = insert_box_label.get()
    a = a[0:-1]
    insert_box_label.set(a)


def insert_zero():
    ins = insert_box_label.get() + '0'
    insert_box_label.set(ins)


def insert_one():
    ins = insert_box_label.get() + '1'
    insert_box_label.set(ins)


def insert_two():
    ins = insert_box_label.get() + '2'
    insert_box_label.set(ins)


def insert_three():
    ins = insert_box_label.get() + '3'
    insert_box_label.set(ins)


def insert_four():
    ins = insert_box_label.get() + '4'
    insert_box_label.set(ins)


def insert_five():
    ins = insert_box_label.get() + '5'
    insert_box_label.set(ins)


def insert_six():
    ins = insert_box_label.get() + '6'
    insert_box_label.set(ins)


def insert_seven():
    ins = insert_box_label.get() + '7'
    insert_box_label.set(ins)


def insert_eight():
    ins = insert_box_label.get() + '8'
    insert_box_label.set(ins)


def insert_nine():
    ins = insert_box_label.get() + '9'
    insert_box_label.set(ins)


def coma():
    a = insert_box_label.get()
    # a = a[0:-1]
    print('a=', a)
    if a == '':
        insert_box_label.set('0.')
    elif '.' not in insert_box_label.get():
        insert_box_label.set(a+'.')


def pm():
    a = insert_box_label.get()
    if a != '':
        a = convertstr(a)
        print(a > 0)
        if a > 0:
            a = '-'+str(a)
        else:
            a = str(abs(a))
        insert_box_label.set(a)


"""buttons"""
child = tk.PanedWindow()
child.grid(row=2, column=0, sticky=tk.N)

# first row of buttons
tk.Button(child, text='CE',command=ce, width=button_width, height=button_height).grid(row=2, column=0)
tk.Button(child, text='C', command=clear, width=button_width, height=button_height).grid(row=2, column=1)
tk.Button(child, text='Back', command=back, width=button_width, height=button_height).grid(row=2, column=2)
tk.Button(child, text='/', command=divide, width=button_width, height=button_height).grid(row=2, column=3)

# second row of buttons
tk.Button(child, text='7', command=insert_seven, width=button_width, height=button_height).grid(row=3, column=0)
tk.Button(child, text='8', command=insert_eight, width=button_width, height=button_height).grid(row=3, column=1)
tk.Button(child, text='9', command=insert_nine, width=button_width, height=button_height).grid(row=3, column=2)
tk.Button(child, text='*', width=button_width, height=button_height, command=multiply).grid(row=3, column=3)

# third row of buttons
tk.Button(child, text='4', command=insert_four, width=button_width, height=button_height).grid(row=4, column=0)
tk.Button(child, text='5', command=insert_five, width=button_width, height=button_height).grid(row=4, column=1)
tk.Button(child, text='6', command=insert_six, width=button_width, height=button_height).grid(row=4, column=2)
tk.Button(child, text='-', width=button_width, height=button_height, command=substract).grid(row=4, column=3)

# fourth row of buttons
tk.Button(child, text='1', command=insert_one, width=button_width, height=button_height).grid(row=5, column=0)
tk.Button(child, text='2', command=insert_two, width=button_width, height=button_height).grid(row=5, column=1)
tk.Button(child, text='3', command=insert_three, width=button_width, height=button_height).grid(row=5, column=2)
tk.Button(child, text='+', width=button_width, height=button_height, command=add).grid(row=5, column=3)

# fifth row of buttons
tk.Button(child, text='+-', width=button_width, height=button_height, command=pm).grid(row=6, column=0)
tk.Button(child, text='0', command=insert_zero, width=button_width, height=button_height).grid(row=6, column=1)
tk.Button(child, text='.', width=button_width, height=button_height, command=coma).grid(row=6, column=2)
tk.Button(child, text='=', width=button_width, height=button_height, command=result_of_operation).grid(row=6, column=3)


root.mainloop()


'''
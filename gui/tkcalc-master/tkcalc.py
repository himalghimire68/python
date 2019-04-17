# from tkinter import *
# import math
#
# class calc:
# 	def getandreplace(self):
# 		"""replace x with * and ÷ with /"""
#
# 		self.expression = self.e.get()
# 		self.newtext=self.expression.replace(self.newdiv,'/')
# 		self.newtext=self.newtext.replace('x','*')
#
# 	def equals(self):
# 		"""when the equal button is pressed"""
#
# 		self.getandreplace()
# 		try:
# 			self.value= eval(self.newtext) #evaluate the expression using the eval function
# 		except SyntaxError or NameErrror:
# 			self.e.delete(0,END)
# 			self.e.insert(0,'Invalid Input!')
# 		else:
# 			self.e.delete(0,END)
# 			self.e.insert(0,self.value)
#
# 	def squareroot(self):
# 		"""squareroot method"""
#
# 		self.getandreplace()
# 		try:
# 			self.value= eval(self.newtext) #evaluate the expression using the eval function
# 		except SyntaxError or NameErrror:
# 			self.e.delete(0,END)
# 			self.e.insert(0,'Invalid Input!')
# 		else:
# 			self.sqrtval=math.sqrt(self.value)
# 			self.e.delete(0,END)
# 			self.e.insert(0,self.sqrtval)
#
# 	def square(self):
# 		"""square method"""
#
# 		self.getandreplace()
# 		try:
# 			self.value= eval(self.newtext) #evaluate the expression using the eval function
# 		except SyntaxError or NameErrror:
# 			self.e.delete(0,END)
# 			self.e.insert(0,'Invalid Input!')
# 		else:
# 			self.sqval=math.pow(self.value,2)
# 			self.e.delete(0,END)
# 			self.e.insert(0,self.sqval)
#
# 	def clearall(self):
# 		"""when clear button is pressed,clears the text input area"""
# 		self.e.delete(0,END)
#
# 	def clear1(self):
# 		self.txt=self.e.get()[:-1]
# 		self.e.delete(0,END)
# 		self.e.insert(0,self.txt)
#
# 	def action(self,argi):
# 		"""pressed button's value is inserted into the end of the text area"""
# 		self.e.insert(END,argi)
#
# 	def __init__(self,master):
# 		"""Constructor method"""
# 		master.title('Calulator')
# 		master.geometry()
# 		self.e = Entry(master)
# 		self.e.grid(row=0,column=0,columnspan=6,pady=3)
# 		self.e.focus_set() #Sets focus on the input text area
#
# 		self.div='÷'
# 		self.newdiv=self.div.decode('utf-8')
#
# 		#Generating Buttons
# 		Button(master,text="=",width=10,command=lambda:self.equals()).grid(row=4, column=4,columnspan=2)
# 		Button(master,text='AC',width=3,command=lambda:self.clearall()).grid(row=1, column=4)
# 		Button(master,text='C',width=3,command=lambda:self.clear1()).grid(row=1, column=5)
# 		Button(master,text="+",width=3,command=lambda:self.action('+')).grid(row=4, column=3)
# 		Button(master,text="x",width=3,command=lambda:self.action('x')).grid(row=2, column=3)
# 		Button(master,text="-",width=3,command=lambda:self.action('-')).grid(row=3, column=3)
# 		Button(master,text="÷",width=3,command=lambda:self.action(self.newdiv)).grid(row=1, column=3)
# 		Button(master,text="%",width=3,command=lambda:self.action('%')).grid(row=4, column=2)
# 		Button(master,text="7",width=3,command=lambda:self.action('7')).grid(row=1, column=0)
# 		Button(master,text="8",width=3,command=lambda:self.action(8)).grid(row=1, column=1)
# 		Button(master,text="9",width=3,command=lambda:self.action(9)).grid(row=1, column=2)
# 		Button(master,text="4",width=3,command=lambda:self.action(4)).grid(row=2, column=0)
# 		Button(master,text="5",width=3,command=lambda:self.action(5)).grid(row=2, column=1)
# 		Button(master,text="6",width=3,command=lambda:self.action(6)).grid(row=2, column=2)
# 		Button(master,text="1",width=3,command=lambda:self.action(1)).grid(row=3, column=0)
# 		Button(master,text="2",width=3,command=lambda:self.action(2)).grid(row=3, column=1)
# 		Button(master,text="3",width=3,command=lambda:self.action(3)).grid(row=3, column=2)
# 		Button(master,text="0",width=3,command=lambda:self.action(0)).grid(row=4, column=0)
# 		Button(master,text=".",width=3,command=lambda:self.action('.')).grid(row=4, column=1)
# 		Button(master,text="(",width=3,command=lambda:self.action('(')).grid(row=2, column=4)
# 		Button(master,text=")",width=3,command=lambda:self.action(')')).grid(row=2, column=5)
# 		Button(master,text="√",width=3,command=lambda:self.squareroot()).grid(row=3, column=4)
# 		Button(master,text="x²",width=3,command=lambda:self.square()).grid(row=3, column=5)
# #Main
# root = Tk()
# obj=calc(root) #object instantiated
# root.mainloop()



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
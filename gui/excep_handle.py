# Zero division Error
'''
try:
    a=int(input("Enter a num:"))
    div=a/0
    print(div)
except ZeroDivisionError:
    print("Nothing could be divided by zero")
except:
    print("some error on your input")

'''



# Raise Error
'''
age = int(input("Enter the age:"))
if age<18:
    raise ValueError
else:
    print("Accepted")
'''

# Creating an Error

class LowAgeError(Exception):
    def __init__(self):
        super(LowAgeError,self).__init__("Age Shoulld be greater than 18")
age = int(input("Enter the age:"))

if age<18:
    raise LowAgeError
else:
    print("Accepted")
#Defining Class
'''

class sample:
    val='himal'

s=sample
print(s.val)
'''

#Calling Constructor

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print ("Name :",self.name)
        print("Age:",self.age)

s1 = student("Himal",22)
s1.display()
s2 = student(s1.name,s1.age)
s2.display()



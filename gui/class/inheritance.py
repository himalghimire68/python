class child:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print ("Name :",self.name)
        print("Age:",self.age)

class student(child):
    def __init__(self,degree,child):
        self.degree=degree
        self.name=child.name
        self.age=child.age

    def details(self):
        print("\n",self.name)
        print("Degree:",self.degree)

s1=child("Aayush",20)
s1.display()
s2=student("Bsc",s1)
s2.details()

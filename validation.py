name = input("Enter your name:")
while name.isalpha() == False or len(name)<3:
    print("Invalid name")
    name= input("Enter your name again:")
print("Welcome",name)

def start_msg():
    print("1. Add\n 2. Subtract \n3.Divide\n 4.Multiply\n5.Exit")
    op = int(input("Enter Your choice in number:"))
    num1 = int(input("Enter First number:"))
    num2= int(input("Enter Second Number:"))
    return op,num1,num2

op, num1, num2= start_msg()


while True:
    if op==1:
        sum=num1+num2
        print("The sum is",sum)
        start_msg()
    elif op==2:
        diff=num1-num2
        print("The Difference is",diff)
        start_msg()
    elif op==3:
        division=num1/num2
        print("The answer is:",division)
        start_msg()
    elif op==4:
        product=num1*num2
        print("The product is ",product)
        start_msg()
    elif op==5:
        print("Exiting")
        break



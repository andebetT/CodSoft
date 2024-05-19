def calculator(number1,number2):
    print("well come")
    print("select 1:for addition")
    print("select 2:for subtraction")
    print("select 3:for division")
    print("select 4:for multiplication")
    choice=input("please select your choice")
    if choice=="1":
        return number1+number2
    elif choice=="2":
        return number1-number2
    elif choice=="3":
        if number2==0:
            raise ValueError('cannot divide by zero')
    elif choice=="4":
        return number1*number2
    else:
        print("enter a valid choice")
number1=int(input("please enter your first number"))
number2=int(input("please enter your second  number"))
print(calculator(number1,number2))


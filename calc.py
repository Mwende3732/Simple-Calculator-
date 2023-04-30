Num1=float(input("Enter the first number: "))
Operator=input("Enter the operator: ")
Num2=float(input("Enter the second number: "))
if Operator=="+":
    print(Num1+Num2)
elif Operator=="-":
    print(Num1-Num2)
elif Operator==("*"):
    print(Num1*Num2)
elif Operator==("/"):
    print(Num1/Num2)
elif Operator==("%"):
    print(Num1%Num2)
elif Operator==("//"):
    print(Num1//Num2)
elif Operator==("**"):
    print(Num1**Num2)
else:
    print("Invalid Input")
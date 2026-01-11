val1=eval(input("Enter a first Number:"))
val2=eval(input("Enter a second Number:"))
oper=input("Enter an operator (+,-,*,/):)")

if oper == "+":
    print("The sum is:",val1+val2)
elif oper =="-":
    print("The difference is:",val1-val2)
elif oper =="*":
    print("The Multiplication is:",val1*val2)
elif oper =="/":
    print("The Division is:",val1/val2)
else:
    print("operator is invalid")
    
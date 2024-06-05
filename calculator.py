#***simple arithmatic operation calculator***

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

print("Enter the operation you want to perform:")
operation=input()

if operation=="1":
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    #addition of two integers.
    print(f"The sum of {num1} + {num2} is:",num1+num2)

elif operation=="2":
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    #subraction of two integers.
    print(f"The difference of {num1} - {num2} is:",num1-num2)

elif operation=="3":
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    #multiplication of two integers.
    print(f"The product of {num1} * {num2} is:",num1*num2)

elif operation=="4":
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    if(num2==0):
    #dividing two integers.
        print("error!!,divisible by zero")
    else:
        print(f"The division of {num1} / {num2} is:",num1/num2)
        
else:
    print("Sorry!, Please enter valid operation!!")
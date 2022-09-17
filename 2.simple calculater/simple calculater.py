x = int(input("Enter first numbers: "))
y = int(input("Enter second number: "))


op = input("enter sign:")

if op == '+':
    print(x+y)
elif op == '-':
    print(x-y)
elif op == '*':
    print(x*y)
elif op =='/':
    print(x/y)
elif  op =='%':
    print(x%y)
else:
    print("invalid Operators signs...")
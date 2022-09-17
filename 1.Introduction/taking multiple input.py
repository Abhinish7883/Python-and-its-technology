# taking two input at a time
x, y = input("Enter two value :").split()
print()
print("first number : ", x, type(x))
print("second number :", y, type(y))

# taking three input at a time
x, y, z = input("Enter three value :").split()
print()
print("first number : ", x, type(x))
print("second number :", y, type(y))
print("third number :", z, type(z))

# taking two input at a time
x, y = input("Enter two value :").split()
print()
print("first number is {} and Second number is {} ".format(x, y))

'''taking multiple input at a time and 
type Casting using list() function.'''
y = list(map(int, input("Enter multiple  value :").split()))
print()
print("list of values : ", y, type(x))

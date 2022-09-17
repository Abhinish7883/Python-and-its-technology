# using for loop with length of string
a = "Abhinish Tiwari"
length = len(a)
print("using for loop with length of string")
for i in range(length):
     print(a[i])
# reverse the string using for loop.
print("Reverse the string.")
for i in range(length-1, -1, -1):
    print(a[i])
# using for loop with string name:
print("using for loop with string name:")
for i in a:
    print(i)

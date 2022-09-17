a = "Abhinish Reema"
print("find():-")
# 1.find() :- return the first index of given substring from left.
print(a.find("A")) # with substring
print(a.find("sh", 3)) # with starting  index and substr.
print(a.find("bh", 2, 7)) # with start and end and sub.
print("rfind():-")
# 2.rfind() : return the first index of given substring from right.
print(a.rfind("A")) # with substring
print(a.rfind("sh", 3)) # with starting  index and substr.
print(a.rfind("bh", 2, 7)) # with start and end and sub.
print("index():-")
print(a.index("A")) # with substring
print(a.index("sh", 3)) # with starting  index and substr.
# print(a.index("bh", 2, 7)) # with start and end and sub.

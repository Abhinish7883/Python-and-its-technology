# return only :- all below function return true and false value.
# 1. isdigit(): true :- if all character in string is digits
#               false :-otherwise : alpha, alphanumeric.
print("isdigit() :-")
a = "2345"
print(a.isdigit())
a = "Abhi123"
print(a.isdigit())
a = "Abhi"
print(a.isalpha())

# 2. isalpha(): true :- if all character in string is alpha
#               false :-otherwise : digit, alphanumeric.
print("isalpha() :-")
a = "2345"
print(a.isalpha())
a = "Abhi123"
print(a.isalpha())
a = "Abhi"
print(a.isalpha())

# 3.isalnum(): true :- if all character in string is alpha , digit and both.
#               false :-otherwise : spacial char.
print("isalnum() :-")
a = "2345"
print(a.isalnum())
a = "Abhi123"
print(a.isalnum())
a = "Abhi"
print(a.isalnum())
a = "Abhinish@123"
print(a.isalnum())

# 4.isdecimal(): true :- if all character in string is decimal.
#               false :-otherwise : spacial char,alpha,alphanum.
print("isdecimal() :-")
a = "23452"
print(a.isdecimal())
a = "Abhi123"
print(a.isdecimal())
a = "Abhi"
print(a.isdecimal())
a = "Abhinish@123"
print(a.isdecimal())





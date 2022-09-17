print("Data types :- \n")
print("1.Number :- ")
print("I. int  :- ")
a = 10
print(a, type(a))
print("II. float :- ")
a = 20.34
print(a, type(a))
print("III. Complex :-")
a = 20 + 20j
print(a, type(a))
print("\n")
print("2.String :- ")
# single line string.
a = "I'm abhi. "
print(a, type(a))
# multi line string.
a = '''
    Hey, my name is abhi.
    i am basically from bihar.
    i am interested in coding.
    '''
print(a, type(a))
a = '10'
print(a, type(a))
print("\n")

print("List :- ")

L = [10, 'ws', 2.5]
print(L, type(L))
# change the value in a particular index of list.
L[2] = 20
print(L, type(L))

print("Tuple :-")
t = (10, 20.5, 2+7j, 'wd')
print(t, type(t))

print("Dictionary :-")
d = {
    1: "Abhi",
    'key': 'value'
}
print(d[1])
print(d, type(d))

print("Set :-")
s = {10, 20, 30, 30}
print(s, type(s))
import re

print(re.match("b[Oo]{2,6}k","bk"))
print(re.match("b[Oo]{2,6}k","bok"))
print(re.match("b[Oo]{2,6}k","book"))
print(re.match("b[Oo]{2,6}k","booook"))
print(re.match("b[Oo]{2,6}k","boooook"))
print(re.match("b[Oo]{2,6}k","boOoOok"))
print(re.match("b[Oo]{2,6}k","boOabcOoOk"))
import re


print(re.match("b[o]*k","bk"))
print(re.match("b[o]*k","bok"))
print(re.match("b[o]*k","book"))
print(re.match("b[o]*k","booook"))
print(re.match("b[o]*k","boOoOok"))
print(re.match("b[o]*k","boOabcOoOk"))
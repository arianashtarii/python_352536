import re

print(re.match("\s"," ")) #space
print(re.match("\d","")) # 0-9
print(re.match("\w","")) #0-9 a-z A-Z _


print(re.match("\S"," ")) #not space
print(re.match("\D","")) #not 0-9
print(re.match("\W","")) #not 0-9 a-z A-Z _
#مثلا 3 تا 30 کاراکتر a تا z مجاز است
# tedad
# * 0...n
# + 1...n
# ? 0...1
# {n} n
# {a,} a...n
# {a,b} a...b

import re


print(re.match("[a-z]{3,30}","alireza"))
print(re.match("[a-z]*","alireza"))
print(re.match("[a-z]+","alireza"))
print(re.match("[a-z]?","alireza"))
print(re.match("[a-z]{3}","alireza"))
print(re.match("[a-z]{3,}","alireza"))
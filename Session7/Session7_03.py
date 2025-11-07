import re
text="book ali boooook reza bOoooOk"
print(re.findall(r"b[oO]{2,10}k",text))
print(re.sub(r"b[oO]{2,10}k","book",text))

import re
text="BOoOoOk"
print(re.match(r"^b[o]{2,}k$",text,re.I))
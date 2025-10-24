import re
print(re.match("[a-z]+","ali123")) #Matched
#میخوایم از اول تا آخر متن باید طبق الگو باشد
print(re.match("^[a-z]+$","ali123")) #Not Matched
# الگو خام regex
#print(re.match(r"^$",""))

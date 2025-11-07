import re
address = "tehran-saadat abad"
print(re.match(r"(tehran|shiraz)-[a-zA-Z\s]{10,}",address))

#mobile
#+989 173215432
#  09173215432
# + تعداد از یک به بالا
# خود علامت + -----> +\
print(re.match(r"(\+989|09)\d{9}","+989173215432"))

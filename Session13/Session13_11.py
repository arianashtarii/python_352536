import re
from platform import android_ver

name_list=["ali","ali2","@#$!","reza","mohsen","ahm@d","omid"]

def name_validator(name):
    return type(name)==str and re.match(r"^[a-zA-Z\s]{3,30}$",name)

javab=list(filter(name_validator,name_list))
print(javab)

import re
def my_function(a,b):
    return a/b

def name_validator(name):
    if not re.match(r"^[a-zA-Z\s]{3,30}$",name):
        raise NameError("Name Error")

def family_validator(family):
    if not re.match(r"^[a-zA-Z\s]{3,30}$",name):
        raise NameError("Family Error")

def age_validator(age):
    if not (type(age) == int and 0<= age <= 150):
        raise ValueError("Invalid age")
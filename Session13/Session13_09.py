name_list=["ahmad","omid","reza","ali","javad","akbar"]

def jensiat(name):
    return name.capitalize()

javab=list(map(jensiat,name_list))
print(javab)

#list , dict , set ,...,object
#mutable in memory
#Call by Reference
def add(x):
    x.append(102)

a=[100,101]
add(a)
print(a) #a=[100,101,102]

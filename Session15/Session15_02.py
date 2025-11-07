#Call By Reference
def test(a):
    a.append(1)
#mutable
#list,set,dict,object
x=[]
test(x)
test(x)
print(x)
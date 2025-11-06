from functools import reduce
numbers=[2,4,2,1,5,2,6]

def zarb(prod,num):
    return prod*num
print(reduce(zarb,numbers))

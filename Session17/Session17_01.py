#stack and heap in python
numbers1=[1,2,3]
numbers2=numbers1
numbers3=numbers2
numbers2.append(4)
numbers3.append(5)
print(numbers1)
print(numbers2)
print(numbers3)
print(id(numbers1)) #آدرس خانه ای که اعداد در حافظه رم قرار دارد
print(id(numbers2))
print(id(numbers3)) #Same id addresses
print(numbers1 is numbers2)
print(numbers2 is numbers3)
print(numbers1 is numbers3)
#----------------------------------------------------------------------

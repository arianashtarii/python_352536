#stack and heap in python
numbers1=[1,2,3,4,5]
numbers2=numbers1.copy()
numbers2.append(400)
numbers1.append(500)
print(numbers1)
print(numbers2)
print(id(numbers1))
print(id(numbers2)) # different id addresses
print(numbers1 is numbers2)
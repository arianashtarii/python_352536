#برای مرتب سازی به ترتیب حروف الفبا یا عدد فقط یک شرط وجود دارد
#داده ها همشون یا رشته باشند یا عدد (اگر داده ها هم اسم باشند هم عدد امکان پذیر نیست)
name_list=["mohsen","ali","ahmad","ali","reza"]
numbers_list=[1,3,2,5,7,8,1,2,3,4,7,6,5,4]
#به روش صعودی Ascending
name_list.sort()
numbers_list.sort()
print(name_list)
print(numbers_list)
#به روش نزولی Descending
name_list.sort(reverse=True)
numbers_list.sort(reverse=True)
print(name_list)
print(numbers_list)
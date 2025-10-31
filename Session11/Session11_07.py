from my_module import *
try:
    name=input("Enter your name: ")
    name_validator(name)
    age=int(input("Enter your age: "))
    age_validator(age)

    print("Hello",name,age)
except Exception as e:
    print("Error:",e)
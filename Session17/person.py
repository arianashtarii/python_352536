class Person:
    def __init__(self,name,family,age):#اختصاص حافظه
        print("Person created...")
        self.name=name
        self.age=age
        self.family=family

    def __del__(self):#حذف در حافظه
        print("Person deleted from memory...")
    def __str__(self):
        print("Person info:",self.name,self.family,self.age)

    def __repr__(self):
        print("Person info:",self.name,self.family,self.age)

person1=Person("John","Mathy","19")
print(person1.name)
print(person1.family)
print(person1.age)
print(id(person1))
del person1 #manual delete person 1
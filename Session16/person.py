#تعریف کلاس
import re
#هر تابعی که در کلاس نوشته میشوند method و property گفته میشود
class Person:
    # donder - magic function
    def __init__(self, id, name,family):
        self.id = id
        self.name = name
        self.family = family
        self.teacher = None
        self.address = None
        self.email = None

    def save(self):
        print("Saved Person...",self.name,self.family)

    def validation(self):
        return re.match(r"^[a-zA-Z]\s{3,30}$",self.name) and re.match(r"^[a-zA-Z]\s{3,30}$",self.family)

    def test(self,a):
        print(a)

    def __repr__(self): #تعریف تابعی که میخوای مقادیر چاپ شوند به جای آدرس
        return f"{self.id}-{self.name:10}-{self.family:10}-{self.address}-{self.teacher}"
#نمونه سازی یا شی سازی
person_1=Person(1,"Arian","Ashtari")
person_1.name="AhmadReza"
person_1.address="Tehran"
person_1.email="AR@gmail.com"
print(person_1)
person_2=Person(2,"Reza","Rezaei")
person_2.address="Tabriz"
person_2.email="RR@gmail.com"
print(person_2)
person_3=Person(3,"Mohsen","Akbari")

#ذخیره سازی
person_1.save()
person_2.save()
person_3.save()

#چاپ حافظه
if person_1.validation():
    person_1.save()
else:
    print("Person 1 validation failed")
if person_2.validation():
    print(person_2)
else:
    print("Person 2 validation failed")
if person_3.validation():
    print(person_3)
else:
    print("Person 3 validation failed")

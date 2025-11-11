#برنامه ای بنویسید که اطالاعات 3 نفر را بگیریم و بعد چاپ کنم
from person import Person
person_list=[]
for i in range(3):
    id=int(input("id: "))
    name=input("Enter name: ")
    family=input("Enter family: ")
    new_person=Person(id,name,family)
    person_list.append(new_person)
    print("Saved")
    print("-------------------------------")

for person in person_list:
    print(person)
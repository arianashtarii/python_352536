from person import Person
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
#person_dict_1={"id":person_1.id,"name":person_1.name,"address":person_1.address,"email":person_1.email}
#person_dict_2={"id":person_2.id,"name":person_2.name,"address":person_2.address,"email":person_2.email}
#print(person_dict_1)
#print(person_dict_2)
print(person_1.__dict__)
print(person_2.__dict__)
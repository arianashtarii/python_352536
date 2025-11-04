students=[
    {"id":1,"name":"arian","age":24},
    {"id":2,"name":"reza","age":19},
    {"id":3,"name":"omid","age":22},
    {"id":4,"name":"mohsen","age":17},
]

name_list=[]
for student in students:
    if student["age"]<20:
        name_list.append(student["name"])

print("Under 20 years old:")
print(name_list)
print(students)
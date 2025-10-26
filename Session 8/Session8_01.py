student_list=[]

student1={"name":"ali","age":25,"family":"alipour","average":17}
student2={"name":"reza","age":25,"family":"mohammadi","average":16}
student3={"name":"mohsen","age":25,"family":"yazdi","average":17}

student_list.append(student1)
student_list.append(student2)
student_list.append(student3)

print(student_list)

print(student_list[0]["average"])
print(student_list[1]["name"])
print(student_list[2]["family"])


sum_average = 0
for i in range (0,3):
    sum_average += student_list[i]["average"]
total_average = sum_average / 3
print("total_average=",total_average)

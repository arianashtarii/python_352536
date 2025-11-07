student_list=[]

student1={"name":"ali","age":25,"family":"alipour","average":17}
student2={"name":"reza","age":25,"family":"mohammadi","average":16}
student3={"name":"mohsen","age":25,"family":"yazdi","average":17}

student_list.append(student1)
student_list.append(student2)
student_list.append(student3)
print(student_list)
print(type(student_list))
print(type(student_list[0]))
# به ازای هر کدام از مقادیر داخل لیست ، یکبار حلقه را اجرا کن
#هربار یک عضو را در متغیری به نام دانش آموز به ما تحویل بده
for student in student_list:
    print(f"Student: {student["name"]:10}{student["family"]:10}")
#فرآیند انتخاب واحد
#5 درس شامل اسم درس ، کد درس ، نام استاد ، تعداد واحد
#اینها از کاربر دریافت بشه بعدا به صورت مرتب زیر هم چاپ شود
#فقط با حلقه فور نوشته شود
#result----->lesson name:teacher name(Numbers of units:)
#result----->print("-------------------------------------)
#result----->total units=

lesson_list=[]
for i in range(5):
    lesson_name=input("Enter lesson name: ")
    lesson_code=int(input("Enter lesson code: "))
    lesson_teacher=input("Enter lesson teacher's name: ")
    lesson_unit=int(input("Enter lesson unit: "))

    lesson = {
        "name": lesson_name,
        "code": lesson_code,
        "teacher": lesson_teacher,
        "unit": lesson_unit
    }
    lesson_list.append(lesson)
    print("Lesson Saved!!!")



sum_units=0
print("------------------------------------------------------------------")
for lesson in lesson_list:
    sum_units += lesson["unit"]
    print(f"{lesson['lesson_name']:10}: {lesson['lesson_code']:10}: {lesson['lesson_unit']:10}")
print("--------------------------------------------------------------------")
print("Sum Of Units:",sum_units)


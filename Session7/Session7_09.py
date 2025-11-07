print("Student App")
print("Version 1.0")
print("By Arian Ashtari")
print("Written 23/10/2025")



#فراخوانی کتابخانه ها
import re
import pickle
#تعاریف اولیه
student_list=[]
option=None
#حلقه تکرار نامعین نمایش منو و انجام عملیات ها
while option!="q":
    print("1)Add Student")
    print("2)Save Students")
    print("3)Show Students")
    print("q)Exit")
    #دریافت گزینه مورد نظر کاربر
    option = input("Enter your option:")
    option=option.lower()
    print("--------------------------------------------")
    if option == "1": #گزینه 1 افزودن دانش آموز ها
        name = input("Enter Student Name:")
        if re.match(r"^[A-Za-z\s]{3,30}$", name):
            student_list.append(name)
            print("Student Added")
        else:
            print("Name Invalid!!!")
    elif option == "2": #ذخیره اطلاعات در فایل
        my_file = open("students", "wb")
        pickle.dump(student_list, my_file)
        my_file.close()
        print("Student Saved")
    elif option == "3": #گزینه 3 خواندن اطلاعات دانش آموزان از فایل و نمایش آنها
        my_file = open("students", "rb")
        student_list = pickle.load(my_file)
        my_file.close()
        print(student_list)
    elif option == "q": #گزینه خروج
        print("Goodbye!!!")
    else: #گزینه غیرمجاز
        print("Invalid Option!!!")
    option=input("Enter your option:")
    print("--------------------------------------------")
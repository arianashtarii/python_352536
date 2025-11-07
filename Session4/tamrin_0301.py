#برنامه ای بنویسید که تا وقتی کلمه خروج را وارد نکرده اسم دریافت کند و تعداد کل کاراکتر کلمات را چاپ کند

name=None
name_list=[]
len_list=[]


while name!="quit":
    name=input("enter your name:")
    if name!="quit":
        name_list.append(name)
        len_list.append(len(name))

print(len_list)
print(name_list)
print(sum(len_list))
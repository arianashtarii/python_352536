#برنامه ای بنویسید که تا وقتی کلمه خروج را وارد نکرده اسم دریافت کند و تعداد کل کاراکتر کلمات را چاپ کند

name=None
sum_len=0

while name!="quit":
    name=input("enter your name: ")
    if name!="quit":
        sum_len+=len(name)

print("Sum Characters:",sum_len)
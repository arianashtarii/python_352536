#برنامه اي بنويسيد که تا وقتي کاربر کلمه خروج را وارد نکرده است ، اسم دريافت کند و تعداد کل کاراکتر ها را محاسبه کند
name=[]
total_characters=0
while True:
    name=input("Enter a name:")
    if name.lower()=="quit":
        break
    total_characters=total_characters+len(name)
print("count characters:",total_characters)

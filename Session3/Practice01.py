#برنامه اي بنويسيد تا وقتي کاربر صفر وارد نکرده عدد بگيرد و سپس ميانگين را محاسبه کند
n=None
majmoo=0
count=0
while n!=0:
    n=float(input("Enter a number:"))
    majmoo=majmoo+n
    count=count+1
avg=majmoo/(count-1) #چون صفر هم جز شمارش ها حساب ميشود
print("Avg:",avg)

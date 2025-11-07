#برنامه ای بنویسید که تا وقتی کاربر صفر وارد نکرده عدد دریافت کند و میانگین اعداد را چاپ کند
numbers=None
avg=0
tedad=0
total_sum=0
while True:
    numbers=float(input("Enter a number: "))
    if numbers==0:
        break
    else:
        total_sum=total_sum+numbers #total_sum+=numbers
        tedad+=1
        avg=total_sum/tedad
print("Avg:",avg)
print("Tedad:",tedad)
print("Total_sum:",total_sum)
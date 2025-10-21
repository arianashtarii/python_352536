#برنامه اي بنويسيد که تا کاربر صفر وارد نکرده باشد عدد دريافت کند و ميانگين اعداد را چاپ کند


# ايجاد شرط اينکه صفر وارد نکرده

sum_num=0

num=None

while True:
    if num!=0:
        num=int(input("enter a num:"))
        sum_num+=num
        count+=1
    elif num==0:
        break

count-=1
    
avg=sum_num/count
print("avg:",avg)   
    



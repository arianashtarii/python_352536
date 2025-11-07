#برنامه ای که کاربر تا وقتی صفر وارد نکرده عدد دریافت کند ، در خروجی لیست اعداد بزرگتر از میانگین و کوچک تر از میانگین را چاپ کند

num_list=[] #تعریف لیست اعداد
upper_list=[] #تعریف لیست بزرگتر از میانگین
lower_list=[] #تعریف لیست کوچکتر از میانگین
avg=0 #مقدار اولیه میانگین


while True: #شرط همیشه برقرار
    num=int(input("Enter a number: ")) #دریافت اعداد از کاربر
    num_list.append(num) #هر بار اضافه کردن اعداد به لیست اعداد
    if num==0: #ایجاد شرط صفر
        num_list.remove(0) #حذف عدد صفر از لیست قبل از بریک
        break

avg=sum(num_list)/len(num_list) #محاسبه میانگین

for num in num_list:
    if num>avg:
        upper_list.append(num)
    elif num<avg:
        lower_list.append(num)

print("num_list=",num_list)
print("upper_list=",upper_list)
print("lower_list=",lower_list)
print("avg=",avg)
print("sum=",sum(num_list))
print("len=",len(num_list))
print("max=",max(num_list))
print("min=",min(num_list))





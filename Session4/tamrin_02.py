#برنامه ای بنویسید که تا وقتی صفر وارد نکرده عدد بگیرد و جمع و میانگین و ماکزیمم و مینیمم و تعداد را چاپ کند
#نوشتن کد با تعریف لیست خالی از اعداد

numbers_list=[]

while True:
    numbers=float(input("Enter a number: "))
    numbers_list.append(numbers)
    if numbers==0:
        numbers_list.remove(0)
        break



print(numbers_list)
print("Minimum number:", min(numbers_list))
print("Maximum number:", max(numbers_list))
print("Average number:", sum(numbers_list)/len(numbers_list))
print("Count of numbers:", len(numbers_list))
print("Sum of numbers:", sum(numbers_list))

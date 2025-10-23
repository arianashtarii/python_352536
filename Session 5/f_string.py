name_1="arian"
family_1="ashtari"
age_1=24


name_2="mohammad"
family_2="rezaei"
age_2=25


print(name_1,family_1,age_1)
print(name_2,family_2,age_2)
#arian ashtari 24
#mohammad rezaei 25

#متغیر ها در براکت ها
#براکت هایی که به عنوان متغیر نوشته شده اند ، اجازه داریم به آنها فرمت دهیم که با : مشخص میکنیم
#10 خانه به طور مثال برای اسم و فامیل در نظر میگیریم
#به طور پیش فرض به سمت چپ می چسباند
print(f"{name_1:10}{family_1:10}{age_1:2}")
print(f"{name_2:10}{family_2:10}{age_2:2}")

#کد زیر به سمت چپ می چسباند
#چپ چین
print(f"{name_1:<10}{family_1:<10}{age_1:<2}")
print(f"{name_2:<10}{family_2:<10}{age_2:<2}")


#کد زیر به سمت راست می چسباند
#راست چین
print(f"{name_1:>10}{family_1:>10}{age_1:>2}")
print(f"{name_2:>10}{family_2:>10}{age_2:>2}")


#کد زیر به سمت وسط چینش میکند
print(f"{name_1:^10}{family_1:^10}{age_1:^2}")
print(f"{name_2:^10}{family_2:^10}{age_2:^2}")

#هر چیزی بیرون آکولاد باشد خودش چاپ میشود و شامل فرمت نیست


#f{value:format}
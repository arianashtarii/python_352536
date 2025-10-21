#برنامه اي بنويسيد که از کاربر قد به سانتي متر
# و وزن به کيلوگرم دريافت کند و بي ام آي را با رقم اعشار چاپ کند


user_height_cm=float(input("enter your height in cm:"))#دريافت قد به سانتي متر
user_weight_kg=float(input("enter your weight in kg:"))#دريافت وزن به کيلوگرم
user_height_m=user_height_cm/100 #تبديل قد به متر
user_bmi=user_weight_kg/(user_height_m)**2 #محاسبه بي ام آي
print("your bmi is:",round(user_bmi,2))#چاپ بي ام آي با 2 رقم اعشار



#bmi<18.5 ----> under weight
#18.5<=bmi<25 ----> normal
#25<=bmi ----> over weight

if user_bmi<18.5:
    print("The user is underweight")

elif 18.5<=user_bmi<25:
    print("The user is normal")

elif 25<=user_bmi:
    print("The user is overweight")

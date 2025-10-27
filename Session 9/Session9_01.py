#برنامه ای که دیتا 5 ماشین را بگیرد و ذخیره کند
# شامل رنگ و برند و سال ساخت باشد
#برنامه غیر ساخت یافته
#غیر حرفه ای
import pickle
import re
car_list=[]
for i in range(5):
    name=input("Enter your car brand: ")
    color= input("Enter your car color: ")
    year= int(input("Enter your car year: "))
    if re.match(r"^[a-zA-Z\s]{3-20}$",name) and color in ["red","blue","black"] and 1990<year<2025 :
        car={"name":name,"color":color,"year":year}
        car_list.append(car)
        file=open("car_list.dat","wb")
        pickle.dump(car_list,file)
        file.close()
        print("car saved...")
        print("------------------------------------------")
    else:
        print("invalid data car")
for car in car_list:
    print(f"{car['name']:8}-({car['color']})-{car['year']}")
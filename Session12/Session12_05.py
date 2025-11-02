# ** هم تعداد نامشخص و هم واسه هر کدومش میتونی اسم بذاری
# ** ----> 0...n   k:v
# مرسوم است kwargs**
def car(**option):
    print("Option:",option)


car(car_color = "white",interior_color = "red",panel_color = "black")
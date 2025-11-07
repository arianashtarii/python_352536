#نسخه def فایل 1 سشن 9
#Session9_04
from Session9_04_module import *
for i in range(5):
    car=get_data()
    if car != None:
        car_list.append(car)
        save_to_file(car_list)
        print("car saved...")
    print("------------------------------------------")
show_data(car_list)
import pickle
import re
car_list = []

def save_to_file(car_list):
    file = open("car_list.dat", "wb")
    pickle.dump(car_list, file)
    file.close()


def data_validation(name,color,year):
   if re.match(r"^[a-zA-Z\s]{1-20}$", name) and color in ["red", "blue", "black"] and 1990 < year < 2025:
       return True
   else:
       return False



def show_data(car_list):
    for car in car_list:
        print(f"{car['name']:8}-({car['color']})-{car['year']}")


def get_data():
    name = input("Enter your car brand: ")
    color = input("Enter your car color: ")
    year = int(input("Enter your car year: "))
    if data_validation(name, color, year):
        car = {"name": name, "color": color, "year": year}
        return car
    else:
        print("invalid data car")
        return None



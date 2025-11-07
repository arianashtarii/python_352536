print("Numbers App")
print("Version 1.0")
print("By Arian Ashtari")
print("Written 23/10/2025")

import re
import pickle

my_number_list = []

while True:
    print("\n1) Add Numbers")
    print("2) Min/Max Numbers")
    print("3) Sum/Average Numbers")
    print("4) Save Numbers")
    print("5) Show Numbers")
    print("6) Exit...")

    option = input("Enter your option: ")

    if option == "1":
        numbers = input("Enter a Number: ")
        if re.match(r"^\d+$", numbers):
            my_number_list.append(int(numbers))
            print("Number Added")
        else:
            print("Invalid Number")

    elif option == "2":
        if my_number_list:
            print("Min:", min(my_number_list))
            print("Max:", max(my_number_list))
        else:
            print("No numbers")

    elif option == "3":
        if my_number_list:
            total = sum(my_number_list)
            print("Sum:", total)
            print("Average:", total / len(my_number_list))
        else:
            print("No numbers")

    elif option == "4":
        my_numbers_file = open("numbers", "wb")
        pickle.dump(my_number_list, my_numbers_file)
        my_numbers_file.close()
        print("Numbers saved")

    elif option == "5":
        print("Numbers:", my_number_list)

    elif option == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option")

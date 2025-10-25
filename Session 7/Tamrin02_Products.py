print("Products App")
print("Version 1.0")
print("By Arian Ashtari")
print("Written 23/10/2025")

import re
import pickle

my_products_list = []

while True:
    print("\n1) Add Product")
    print("2) Show All")
    print("3) Save to File")
    print("4) Read from File")
    print("5) Show Counts")
    print("0) Exit")

    option = input("Enter your option: ")

    if option == "1":
        product_name = input("Enter product name: ")
        if re.match(r"^[a-zA-Z0-9\s]{3,30}$", product_name):
            my_products_list.append(product_name)
            print("Product Added")
        else:
            print("Invalid Product Name - Must be 3-30 characters (letters, numbers, spaces only)")

    elif option == "2":
        if my_products_list:
            print("All Products:")
            for product in my_products_list:
                print(f"- {product}")
        else:
            print("No products")

    elif option == "3":
        if my_products_list:
            my_products_file = open("products", "wb")
            pickle.dump(my_products_list, my_products_file)
            my_products_file.close()
            print("Products saved to file")
        else:
            print("No products to save")

    elif option == "4":
        my_products_file = open("products", "rb")
        my_products_list = pickle.load(my_products_file)
        my_products_file.close()
        print("Products loaded from file")

    elif option == "5":
        print("Total products:", len(my_products_list))

    elif option == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid option")
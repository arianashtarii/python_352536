#اطلاعات 3 کالا شامل اسم کالا ، تعداد ، قیمت دریافت کند و تک تک چاپ کند
#لیستی از کالاها داریم
# یک لیست است که خانه های آن دیکشنری است
product_list=[]
for i in range(3):
    esm=input("Enter product name:")
    tedad=int(input("Enter product quantity:"))
    gheymat=int(input("Enter product price:"))
    product={"name":esm,"quantity":tedad,"price":gheymat}
    product_list.append(product)
    print("-------------------------------------------------------")
print(product_list)

total=0
for product in product_list:
    sum_item=product["quantity"]*product["price"]
    total=total+sum_item
    print(product["name"],sum_item)
print("------------------------------------------------------------")
print("total:",total)
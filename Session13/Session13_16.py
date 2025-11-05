from itertools import product

product_list=[
    {"id":1,"name":"mobile","quantity":5,"price":400},
    {"id":2,"name":"laptop","quantity":5,"price":800},
    {"id":3,"name":"speaker","quantity":11,"price":700},
    {"id":4,"name":"monitor","quantity":3,"price":600},
    {"id":5,"name":"mouse","quantity":6,"price":350},
    {"id":6,"name":"keyboard","quantity":4,"price":200},
    {"id":7,"name":"touch","quantity":9,"price":800},
]
#map/filter/zip/enumerate
#اجازه استفاده از for نداریم

#اضافه کردن قیمت کل به هر دیکشنری
def total_price(product):
    product["total price"]=product["price"]*product["quantity"]
    return product
javab=list(map(total_price,product_list))
print(javab)
# capitalize کردن تمامی اسامی
def capitilize_names(product):
    product["name"]=product["name"].capitalize()
    return product
#جمع کل فاکتور
def total_prices(product):
    return product["price"]*product["quantity"]
print(list(map(total_prices,product_list)))
#لیست اسم کالا های با مجموع کمتر از 5000
def lower_5000(product):
    return product["total price"]<5000
print(list(filter(lower_5000,product_list)))

#لیست اسم کالا های با مجموع بیشتر از 5000
def upper_5000(product):
    return product["total price"]>=5000
print(list(filter(upper_5000,product_list)))
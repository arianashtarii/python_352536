from functools import reduce
product_list=[
    {"id":1,"name":"mobile","quantity":3,"price":800},
    {"id":2,"name":"speaker","quantity":2,"price":400},
    {"id":3,"name":"adapter","quantity":1,"price":200},
    {"id":4,"name":"laptop","quantity":3,"price":2500},
]
#میخوام این لیست دیکشنری که دارم بر اساس اسم کالا مرتب شود
sorted_product_list=sorted(product_list, key=lambda k: k["name"])
print(sorted_product_list)

#جمع کل فاکتور

print(reduce(lambda jam, product: jam + product["quantity"] * product["price"], product_list, 0))

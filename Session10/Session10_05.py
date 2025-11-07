#میخوایم سقف خرید 10000 باشد
order_list=[]
total=0
while total<10000:
    name=input("Enter name: ")
    price=int(input("Enter price: "))

    if total+price>10000:
        print("Too much price...")
        break
    total+=price

order={"name":name,"price":price}
order_list.append(order)

for order in order_list:
    print(f"{order['name']}:10 {order['price']}")
print("---------------------------------------------")

print(f"total:{total}")
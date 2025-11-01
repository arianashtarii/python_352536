from tkinter import *
from tkinter import messagebox
from Supermaket_Module import *

Supermarket_list = []


def save():
    try:
        name_validator(name.get())
        id_validator(id.get())
        brand_validator(brand.get())
        quantity_validator(quantity.get())
        price_validator(float(price.get()))
        expire_validator(expire_date.get())

        Supermarket_dict = {"id:": id.get(), "name:": name.get(), "brand:": brand.get(), "quantity:": quantity.get(),
                            "price:": price.get(), "expire date:": expire_date.get()}
        Supermarket_list.append(Supermarket_dict)
        messagebox.showinfo("Saved", "Saved Successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def total():
    try:
        total_price = 0
        for item in Supermarket_list:
            total_price += float(item["price:"])
        messagebox.showinfo("Total", f"Total Price: {total_price}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


window = Tk()
window.title("Supermarket Arian")
window.geometry("500x500")

Label(window, text="id:").place(x=10, y=10)
id = IntVar()
Entry(window, textvariable=id, bg="lightblue").place(x=50, y=10)
id.set(1)

Label(window, text="Name:").place(x=10, y=40)
name = StringVar()
Entry(window, textvariable=name, bg="lightblue").place(x=50, y=40)
name.set("")

Label(window, text="brand:").place(x=10, y=70)
brand = StringVar()
Entry(window, textvariable=brand, bg="lightblue").place(x=50, y=70)
brand.set("")

Label(window, text="quantity:").place(x=0, y=100)
quantity = IntVar()
Entry(window, textvariable=quantity, bg="lightblue").place(x=50, y=100)

Label(window, text="price:").place(x=10, y=130)
price = StringVar()
Entry(window, textvariable=price, bg="lightblue").place(x=50, y=130)

Label(window, text="expire date:").place(x=10, y=160)
expire_date = StringVar()
Entry(window, textvariable=expire_date, bg="lightblue").place(x=80, y=160)

Button(window, text="Total", command=total).place(x=150, y=200, width=100, height=100)
Button(window, text="Save", command=save).place(x=10, y=200, width=100, height=100)
window.mainloop()
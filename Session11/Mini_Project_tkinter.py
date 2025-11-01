from tkinter import *
from tkinter import messagebox
from my_module import *
#int   IntVar()
#float   DoubleVar()
#str StringVar()
#bool BooleanVar()

person_list=[]
def save():
    try:
        name_validator(name.get())
        family_validator(name.get())
        person={"id":id.get(),"name":name.get(),"family":family.get()}
        person_list.append(person)
        messagebox.showinfo("Saved","Saved Successfully")
        id.set(0) #بعد از سیو کردن مقدار اتوماتیک صفر شود
        name.set("") #بعد از سیو کردن مقدار خالی شود
        family.set("") #بعد از سیو کردن مقدار خالی شود
    except Exception as e:
        messagebox.showerror("Error",f"Error: {e}")
window = Tk() #پنجره خالی
#window.config(background="black")

window.title("Program Name") #اسم برنامه
window.geometry("400x400") #اندازه برنامه

#Id
Label(window,text="Id:").place(x=10,y=10) #id default=0
id=IntVar()
Entry(window,textvariable=id,bg="lightblue").place(x=50,y=10)

#Name
Label(window,text="Name:").place(x=10,y=40)
name=StringVar()
Entry(window,textvariable=name,bg="lightblue").place(x=50,y=40)
name.set("Arian")

#Family
Label(window,text="Family:").place(x=10,y=70)
family=StringVar()
Entry(window,textvariable=family,bg="lightblue").place(x=50,y=70)
family.set("Ashtari") #یه مقدار ثابت پیش فرض میفرسته روی پنجره

#Save Button
Button(window,text="Save",command=save).place(x=10,y=100,width=100,height=100)

window.mainloop() #برنامه تا زمانی که بسته نشده است ادامه دارد
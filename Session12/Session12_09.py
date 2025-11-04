#تابع تعریف میکنیم ولی صداش نمیکنیم
#callback function
#بدون ورودی
from tkinter import *
from my_module import *

win = Tk()

Button(win,text="test",command=test).place(x=20,y=20) #اسم تابع در دستور command


win.mainloop()
#یه مثال از لیستی که در آن دیکشنری نیست
number=[10,12,4,15,7,6,13,9,10]


pass_list=[]
#تابعی بنویس که یک ورودی دارد و شرط را در تابع قرار بده

def check(num):
    return num>=10

pass_list=list(filter(check,number))
print(pass_list)
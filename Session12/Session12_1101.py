#global scope
# برای دسترسی به متغیر های داخل تابع در برنامه اصلی از دستور global استفاده میکنیم
def test_3(): #a,b در حوزه 1
    global a,b
    a = 1
    b = 2
    return a,b

def test_4(): #a,b در حوزه 2
    a = 3
    b = 4
a = 100 # a=1
b = 200 # b=2
test_3()
print(test_3())
print(a,b)

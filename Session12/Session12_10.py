#Error
#تابع یک سرزمین مستقل برای خودش است
#و هیچکس به چیزای داخل تابع دسترسی ندارد
#Scope حوزه
def test_3(): #a,b در حوزه 1
    a = 1
    b = 2
    return a,b

def test_4(): #a,b در حوزه 2
    a = 3
    b = 4

test_3()
print(test_3())
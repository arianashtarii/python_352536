def test_1():
    print("Test 1")

def test_2():
    print("Test 2")

def test_3():
    print("Test 3")

def ejra_konande(tabe):
    try:
        print("Running:",tabe.__name__)
        tabe()
        print("Ok!!!")
    except Exception as e:
        print(f"Khata: {e}")
#Call Back
ejra_konande(test_1)
ejra_konande(test_2)
ejra_konande(test_3)

#یک ترای اکسپت در یک تابع نوشتیم و همه تابع ها را روش اجرا کنیم
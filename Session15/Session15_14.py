#Decorator
#تابع تو در تو
def exeption_handling_and_log(tabe):
    def dakheli(*args,**kwargs):
        try:
            print("\nRunning:", tabe.__name__,"Input",args)
            tabe(*args,**kwargs)
            print("Run Ok and output is{output}\n")
        except Exception as e:
            print(f"Khata: {e}")
    return dakheli


@exeption_handling_and_log
def test_1(a,b,c):
    return "Test 1"
@exeption_handling_and_log
def test_2(a):
    return "Test 2"
@exeption_handling_and_log
def test_3(x,y):
    return "Test 3"

test_1(1,2,3)
test_2(2)
test_3(4,5)
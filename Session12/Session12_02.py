#print()
#print(1)
#print(12,3,4,5,4)
#print(21,3,4,5,6,"ali",True)
# *a   0...n parameters
# def test (*args) پارامتر با تعداد متغیر مرسوم است
def test(*a):
    print("A:",a)

test(20)
test("test")
test("test a" , "test b")
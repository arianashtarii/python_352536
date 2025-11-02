def test(a,b):
    pass #تابع خالی یعنی بعدا بهش رسیدگی میکنم




def test_2(a,b,c=1):
    pass
test_2(1,2) #c=1 default
test_2(3,4,5)



def test_3(*args):
    pass
test_3()
test_3(1)
test_3("ali","mohsen")
test_3(1,2,3)






def test_4(**kwargs):
    pass
test_4()
test_4(x=2)
test_4(x=3,y=4)
test_4(x=4,y=5,z="ali")
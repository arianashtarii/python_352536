def test(a,b,*args,x=3,y=4):
    print("A:",a)
    print("B:",b)
    print("args:",args)
    print("x:",x)
    print("y:",y)


#test() #خطا میدهد چون آ و ب نداریم
test(1,2)
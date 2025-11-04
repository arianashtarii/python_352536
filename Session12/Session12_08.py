def test(a,b,*args,**kwargs):
    print("A:",a)
    print("B:",b)
    print("args:",args)
    print("kwargs:",kwargs)




test(1,2,3,5,6,7,8,x=10 , z=20 )
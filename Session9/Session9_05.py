#تابع تشخیص عدد اول
def is_prime(number):
    count=0
    for i in range(1,number+1):
        if number%i==0:
            count=count+1
        if count==2:
            return True
        else:
            return False


#main
for i in range(1,1001):
    if is_prime(i):
        print(i)
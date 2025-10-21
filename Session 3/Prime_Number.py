# عدد اول = Prime Number

n=int(input("Enter a num:")) #دريافت عدد از کاربر

count=0 #تعريف شمارنده اوليه برابر با صفر

for i in range(1,n+1,1):
    if n%i==0:
        print(i)
        count+=1 #count=count+1

print("count:",count)

if count==2:
    print("This is a prime number")

else:
    print("This is not a prime number")
        

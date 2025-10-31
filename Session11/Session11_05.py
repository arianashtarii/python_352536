#چه خطا داد چه خطا ندهد در اکسپت فایل را میبندم
# finally----> چه خطا بدهد چه ندهد اجرا میشود
import pickle
file=open("abc.txt","wb")

try:
    print(a)
    pickle.dump(a,file)
except ZeroDivisionError:
    print("Can't divide by zero")
except FileNotFoundError:
    print("File not found")
except NameError:
    print("Name error")
except:
    print("Other errors")
finally: #در هر صورت اجرا میشود
    file.close()
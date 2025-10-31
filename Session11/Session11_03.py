print("Start")
#ValueError
try:
    a=int(input("a="))
    b=int(input("b="))
    print(a/b)
except ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError:
    print("ValueError")
except:
    print("Unknown Error")
print("End")

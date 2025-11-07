import re
#data validation
#اعتبار سنجی
#a-z A-Z space {3,30}
name = input("Enter your name: ")
if re.match(r"^[a-zA-Z\s]{3,30}$",name):
    print("Your name is valid")
else:
    print("Your name is not valid")
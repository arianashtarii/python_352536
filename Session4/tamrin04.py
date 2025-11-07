#یافتن اعداد مفقوده دریافتی از کاربر
num_list_input=[]
num_list_missing=[]



while True:
    num=int(input("Enter a number: "))
    num_list_input.append(num)
    if num==0:
        num_list_input.remove(0)
        break

for num in range(min(num_list_input),max(num_list_input)+1,1):
    if num not in num_list_input:
        num_list_missing.append(num)

print("Missing numbers=",num_list_missing)
print("Input list numbers=",num_list_input)
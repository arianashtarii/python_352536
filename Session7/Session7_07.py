# 3 مرحله اساسی
import pickle

#باز کردن فایل
#write binary
my_file=open("student","wb")
#عملیات روی فایل
#نوشتن در فایل
name_list=["ahmad","ali","reza"]
pickle.dump(name_list,my_file)
#بستن فایل
my_file.close()
students=[
    {"id":1,"name":"arian","age":24},
    {"id":2,"name":"reza","age":19},
    {"id":3,"name":"omid","age":22},
    {"id":4,"name":"mohsen","age":17},
]
#به جای فور و ایف میتوان تابع نوشت
def under_20(std):
    return std["age"] < 20

under_list=list(filter(under_20,students))
print("Under 20:",under_list)
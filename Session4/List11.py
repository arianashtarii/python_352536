#linear search جستجو خطی
#Case insensitive search
name_list=["ali","mohsen","ahmad","omid","reza"]
search_name="ahMad"


for name in name_list:
    if search_name.lower()==name.lower():
        print("Found it...")

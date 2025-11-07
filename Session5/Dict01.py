city_codes={"Tehran":11,"Ahvaz":14,"Isfahan":13,"Mashhad":12}
#افزودن عضو جدید
city_codes["Shiraz"]=63
print(city_codes)
#ویرایش عضو = نوشتن عضو و قرار دادن مقدار جدیدش
city_codes["Tehran"]=21
print(city_codes)

#حذف با کلید
city_codes.pop("Tehran")
print(city_codes)
import datetime
birth_date=datetime.date.today()
print(birth_date.weekday())
print(datetime.datetime.now())
birth_date_1=birth_date.year
print(birth_date)
print(birth_date_1)

my_time=datetime.time(15,36,32,43)
print(my_time)
print(type(my_time))

doc_date_time=datetime.datetime(2025,10,4,14,42,21,23)
print(doc_date_time)


alan=datetime.datetime.now()
print(alan)
print(alan.year)
print(alan.month)
print(alan.day)
print(alan.hour)
print(alan.minute)
print(alan.second)

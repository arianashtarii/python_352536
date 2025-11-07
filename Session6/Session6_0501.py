import datetime
borrow=datetime.date.today()
print(borrow + datetime.timedelta(days=29))

#برای تعیین مهلت
end_time=datetime.datetime(2025,11,25)
alan=datetime.datetime.now()
print(end_time - alan)
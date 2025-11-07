import datetime
#اختلاف زمان
borrow_date=datetime.date(2025,9,8)
print(borrow_date + datetime.timedelta(days=15,hours=8,minutes=43))
print(borrow_date - datetime.timedelta(days=15,hours=8,minutes=43))


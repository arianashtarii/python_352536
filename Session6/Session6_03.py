#تبدیل رشته به تاریخ
import datetime
# %Y تاریخ چهار رقمی
# %y تاریخ دو رقمی
# %m month
# %d day
# %H hour
# %M minute
# %S second
my_date=datetime.datetime.strptime("2001/6/23", "%Y/%m/%d")
print(my_date)
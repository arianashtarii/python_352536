import datetime

borrow_book_date=datetime.datetime(2025,9,8,15,23,23)
return_book_date=datetime.datetime(2025,10,2,16,21,11)
print(return_book_date - borrow_book_date)
print(borrow_book_date < return_book_date)
# < past
# > future
# -
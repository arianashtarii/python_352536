import re
import datetime

def id_validator(id):
    if not(type(id) == int):
        raise ValueError("Invalid id!!!")
    else:
        return id

def name_validator(name):
    if not (type(name) == str) or not re.match(r"^[a-zA-Z\s]{3,30}$", name):
        raise ValueError("Invalid name!!!")
    else:
        return name

def brand_validator(brand):
    if not (type(brand) == str) or not re.match(r"^[a-zA-Z\s]{3,30}$", brand):
        raise ValueError("Invalid brand!!!")
    else:
        return brand

def price_validator(price):
    if not (type(price) == float):
        raise ValueError("Invalid price!!!")
    else:
        return price

def expire_validator(expire_date):
    if not (expire_date > datetime.date.today()):
        raise ValueError("Invalid expire date!!!")
    else:
        return expire_date

def quantity_validator(quantity):
    if not (type(quantity) == int):
        raise ValueError("Invalid quantity!!!")
    else:
        return quantity
# الگوی خام f-string با دیکشنری

# نمونه دیکشنری
my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

# 1. چاپ کلید و مقدار با متن ثابت
print(f"Key: key1 - Value: {my_dict['key1']}")

# 2. چاپ چندین کلید و مقدار
print(f"Key1: {my_dict['key1']} - Key2: {my_dict['key2']} - Key3: {my_dict['key3']}")

# 3. چاپ تمام کلیدها و مقادیر با حلقه
for key, value in my_dict.items():
    print(f"Key: {key} - Value: {value}")

# 4. چاپ با فرمت دلخواه
print(f"{my_dict['key1']} | {my_dict['key2']} | {my_dict['key3']}")
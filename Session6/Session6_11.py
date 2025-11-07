import re

#به انگلیسی
# حروف کوچک ، حروف بزرگ ، همه اعداد 0 تا 9 و آندرلاین مجاز باشد
# \w -----> [a-zA-Z0-9_]
# \d ------> [0-9]
# \s ------> space
print(re.match("[a-zA-Z0-9_]{3,30}","alireza123_"))
print(re.match(r"\w{3,30}","alireza123_"))
print(re.match(r"\d{3,30}","1234234324"))
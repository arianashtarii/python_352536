# 5 عدد خط فاصله باشد 0 یا 1 و دوباره 5 عدد
import re

code_1="1234512345"
code_2="12345-12345"


print(re.match(r"^\d{5}-?\d{5}$",code_1))
print(re.match(r"^\d{5}-?\d{5}$",code_2))
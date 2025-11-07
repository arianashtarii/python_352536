# نقطه یعنی هر کاراکتری
# خود کاراکتر نقطه .\
import re
print(re.match(r".","adasad"))
print(re.match(r"[a-zA-Z][a-zA-Z0-9_\.]{1,30}@(gmail|yahoo|msn)\.com","arian.ashtari11@gmail.com"))

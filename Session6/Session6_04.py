import datetime
birth_date=input("Enter Your birthdate (year/month/day): ")
birth_date=birth_date.replace("/", "-")
birth_date=datetime.datetime.strptime(birth_date, "%Y-%m-%d")
print(birth_date.date())
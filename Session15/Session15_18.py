#Match---->Case
#به جای ایف و الیف
#if...elif...
#در تمام شرط ها فقط یک متغیر چک شده است
#مقایسه فقط == باشد
print("1)Add")
print("2)Edit")
print("3)Delete")
print("4)Find")
print("0)Exit")
option = input("Enter your choice: ")
match option:
    case 1:
        print("1)Add...")
    case 2:
        print("2)Edit...")
    case 3:
        print("3)Delete...")
    case 4:
        print("4)Find...")
    case _:
        print("Exit...")



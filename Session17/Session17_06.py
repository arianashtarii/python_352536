#قابل پیمایش
# میتوان for زد
#iterable
#list , set , tuple , str , range
# output map and filter
numbers=[1,2,3,4,5]
print("Len of Numbers:",len(numbers))

#for number in numbers:
  #  print(number)


def tavan_2(x):
    return x**2


print(list(map(tavan_2, numbers)))

for t in map(tavan_2, numbers):
    print(t)

#x=abs(-10)
#print(x)

#تعریف قدر مطلق
def ghadere_motlagh(number):
    if number>=0:
        return number
    else:
        return -number

x=ghadere_motlagh(-10)
print(x)
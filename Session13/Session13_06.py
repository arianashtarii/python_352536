numbers=["1","2","3","4","5","6"]

def cast_to_int(num):
    return int(num)
num_list=(list(map(cast_to_int,numbers)))




print("Sum of Num list:",sum(num_list))
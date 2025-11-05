#میخوایم در دیکشنری جای کلید و ولیو عوض شود
my_dict = {"a":1,"b":2,"c":3}
print(dict(zip(my_dict.values(),my_dict.keys()))) #change
print(dict(zip(my_dict.keys(),my_dict.values())))
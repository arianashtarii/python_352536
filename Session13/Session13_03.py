name_list=["ahmad","omid","reza","ali","javad","akbar"]

#for name in name_list:
  #  if name.startswith("a"):
   #     print(name)

def shoroo_ba_a(name):
    return name.startswith("a")

javab=list(filter(shoroo_ba_a,name_list))
print(javab)
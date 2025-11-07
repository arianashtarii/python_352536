import pickle
my_file=open("student","rb")
my_list=pickle.load(my_file)
print(my_list)

my_file.close()
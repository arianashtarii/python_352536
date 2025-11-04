students=[
    {"id":1,"name":"arian","family":"ashtari","age":24},
    {"id":2,"name":"reza","family":"rezaii","age":19},
    {"id":3,"name":"omid","family":"ahmadi","age":22},
    {"id":4,"name":"mohsen","family":"akbari","age":17},
]

full_names=[]

def full_names(std_dict):
    return std_dict["name"].capitalize().strip()+""+std_dict["family"].capitalize().strip()

print(list(map(full_names,students)))
class MyClass: #Auto Closable Class
    def __enter__(self):
        print("Opened")
    def __exit__(self,*args):
        print("Closed")

obj = MyClass()

with obj:
    print("Salam")

print("Continue...")
# __magic function__
#__init__ , __repr__
#life cycle
#create/delete
#print
#cast int / float
# len / index
# for
# ** * / // % + -
# == != > < >= <=
#with open/close

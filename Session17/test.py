class Tavan2: #iterable class
    #__init,__str,__repr__,__iter__,__next__,__new__,__class__,__eq__,
    #__gt__,__lt__ are important
    def __init__(self):
        self.n=1
        self.max=100
    def __iter__(self):
        return self
    def __len__(self):
        return 100
    def __next__(self):
        print("printing loop")
        if self.n>self.max:
            raise StopIteration
        else:
            result=self.n**2
            self.n+=1
            return result

tavan2 = Tavan2()
print(len(tavan2))

for item in tavan2:
    print(item)
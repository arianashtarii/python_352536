class Nomre:
    def __init__(self, number):
        if 0<=number<=20:
            self.number=number
        else:
            print("Number out of range...")

    def __add__(self,other):
        print("جمع شد...")

    def __sub__(self,other):
        print("تفریق شد...")

    def __eq__(self,other):
        print("داری == را چک میکنی")

    def __gt__(self, other):
        print("داری بزرگ تر را چک میکنی")

    def __lt__(self, other):
        print("داری کوچکتر را چک میکنی")
    def __bool__(self):
        print("تبدیل به بولین")

    def __int__(self):
        print("تبدیل به عدد صحیح")
nomre_1=Nomre(10)
nomre_2=Nomre(20)
nomre_3=Nomre(15)
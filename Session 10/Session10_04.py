#آرگومان های تابع
def test(a,b,c=1,d=2):
    return a+b+c+d

print(test(1,2,3,4)) #answer--->10
print(test(1,2,3,)) #answer--->8
print(test(1,2)) #answer--->6
print(test(1,2,d=3)) #answer--->7
#recursive function
def loop(n):
    print(n)
    if n == 1:
        return 1
    return loop(n - 1)

loop(10)
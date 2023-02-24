import random as r

n = int(input('Enter the number of coins: '))
a = ''
def Coins(a):
    for i in range(n):
        a += str(r.randint(0, 1))

    def Counter(a):
        count = 0
        for i in range(n):
            if int(a[i]) == 0:
                count += 1
        if count > (n - count):
            return n - count
        else:
            return count
    print(a)
    print(Counter(a))

Coins(a)
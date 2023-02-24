n = int(input('Enter the power of 2: '))
num = 2
def Exponentiation(n):
    i = 0
    while num ** i <= n:
        print(num ** i, end=' ')
        i += 1

Exponentiation(n)
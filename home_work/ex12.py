q = int(input('Enter the sum: '))
p = int(input('Enter the product of num: '))
def KatyaNum(q, p):
    flag = True
    while flag:
        x1 = int(input('Enter x1 = '))
        x2 = int(input('Enter x2 = '))
        if (x1 + x2 == q) and (x1 * x2 == p):
            print(f'Hidden numbers: {x1}, {x2}')
            flag = False
        else:
            print('Try again')

KatyaNum(q, p)


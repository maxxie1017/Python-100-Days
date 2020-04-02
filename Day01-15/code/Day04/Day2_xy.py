import numpy as np

"""
a = np.random.randint(100)
counter = 0
i = -1
while i != a:
    counter += 1
    i=int(input('Please guess:'))
    if i<a:
        print('small guess')
    elif i>a:
        print('too large')
    else:
        print('you get right!')
print('you get the answer in %d guesses' % counter)
"""


def judgement(a):
    final = True
    for k in range(2, a):
        if a % k == 0:
            final = False
            break
    if final and a != 1:
        print('%d is a sushu' % a)
    else:
        print('%d is not a sushu' % a)


a = int(input('please input an int'))
b = int(input('please input another int'))


def gcd(a, b):  # 最大公约数计算
    small = min(a, b)
    for k in range(small, 0, -1):
        if a % k == 0 and b % k == 0:
            gcd = k
            break
    return gcd


g = gcd(a, b)
print('The greatest common divisor of %d and %d is %d' % (a, b, g))

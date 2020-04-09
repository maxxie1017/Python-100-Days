"""
daffodils = []
for k in range(100,1000):
    print(k)
    unit = k%10
    ten = (k-unit)%100/10
    hundred = (k-ten*10-unit)/100
    print(hundred, ten, unit)
    if k == unit**3+ten**3+hundred**3:
        daffodils.append(k)
print(daffodils)
"""


#CRAPS
"""
money = 1000
import random
def compare(last, now, money, debt):
    over = False
    while not over:
        if now == last:
            money += debt
            over = True
        elif now == 7:
            money -= debt
            over = True
        else:
            last = now
            now = random.randint(1,6)+random.randint(1,6)
            print('new dice is %d' % now)
    return money


while money>0:
    print('you have %d now' % money)
    debt = int(input('your debt: '))
    first_dice = random.randint(1,6)+random.randint(1,6)
    print('dice this time is: %d' % first_dice)
    if first_dice == 7 or first_dice == 11:
        money += debt
    elif first_dice == 2 or first_dice == 3 or first_dice == 12:
        money -= debt
    else:
        second_dice = random.randint(1,6)+random.randint(1,6)
        print('the new dice is: %d' % second_dice)
        money = compare(first_dice, second_dice, money, debt)
print('you have lose all money, game over')
"""


# Fibonacci sequence
'''k=[1]*20
for i in range(2, 20):
    k[i] = k[i-1]+k[i-2]
print(k)'''


# Perfect number
perfect = []
for num in range(1, 10000, 1):
    sum = 0
    for k in range(1, num, 1):
        if num%k == 0:
            sum += k
    if sum == num:
        print('%d is perfect' %num)
        perfect.append(num)
print(perfect)



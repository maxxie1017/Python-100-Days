# 字符串表达
"""
a, b = 5, 10
print('{0} * {1} = {2}'.format(a, b, a * b))
print(f'{a}*{b}={a*b}')
"""

# list: remove, extend, pop
'''list = [1,2,3,4,5,6,7,8,9,0,1091]
if 1 in list:
    list.remove(1)
list.extend([1000,3000])

print(list)'''

# 反向切片，::-1, 从头到尾，并反向
"""
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
# 列表切片
fruits2 = fruits[::-1]
print(fruits2)
"""


# sorted不会对原有list进行修改，sort会
"""
fruits.sort(reverse=True)
print(fruits)
"""
# 生成器、生成式
"""
import sys
#f = [x ** 2 for x in range(1, 1000)]
f = (x ** 2 for x in range(1, 1000))
print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
print(f)
"""

# 利用yield将函数包装成生成器
"""
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)
    print(fib(20))


if __name__ == '__main__':
    main()
"""
#tuple is smaller in memory than list
"""
a=[1,2,3,4,5]
b=tuple(a)
import sys
print(sys.getsizeof(a))
print(sys.getsizeof(b))
"""

# exercise1:
import os
import time


def zoumadeng():
    content = '北京欢迎你为你开天辟地…………'
    num = len(content)
    while True:
        os.system('cls')
        print(content)
        content = content[1:]+content[0]
        time.sleep(0.3)

def yanzhengma(l=4):
    import random
    import string
    str = ''
    for i in range(l):
        s = string.ascii_letters+string.digits
        str = str + random.choice(s)
    print(str)
    return str

def suffix(filename):
    file = filename.split('.', -1)
    return file[-1]

def getnums(l):
    l.sort()
    return l[-1], l[-2]

def caldate(year, month, day):
    def is_leap_year(year):
        leap = False
        if year%4 == 0 and year%100 != 0 and year%400 == 0:
            leap =True
        return leap
    days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]
    days = 0
    for m in range(month-1):
        days += days_in_months[m]
    days += day
    if is_leap_year(year):
        days +=1
    return days

def yanghui(lines):
    last_line = [1]
    for l in range(1, lines, 1):
        new_line = [1]*(l+1)
        for k in range(1,l,1):
            new_line[k]=last_line[k-1]+last_line[k]
            print(new_line[k],end='\t')
        print('\n')
        #print('\t\t\t\t',new_line,'\n')
        last_line = new_line

def main():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()

from random import randrange, randint, sample


def display(balls):
    """
    输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main_balls():
    n = int(input('机选几注: '))
    for _ in range(n):
        display(random_select())

"""
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，
有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。
由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
"""
def main():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end='')


if __name__ == '__main__':
    main()




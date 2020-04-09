class Student(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self._gender = gender

    def __bar(self):
        print(self.__gender)
        print('__bar')

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看大电影.' % self.name)


class Clock(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def run(self):
        self.second += 1
        if self.second == 60:
            self.minute += 1
            self.second = 0
            if self.minute == 60:
                self.hour += 1
                self.minute = 0
                if self.hour == 60:
                    self.hour = 0

    def showtime(self):
        string = 'Now the time is %02d:%02d:%02d' % (self.hour, self.minute, self.second)
        print(string)
        return string


def main_clock():
    import time
    clock = Clock(12, 23, 45)
    while True:
        clock.run()
        clock.showtime()
        time.sleep(1)

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def caldistance(self, other):
        from math import sqrt
        d = sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return d


def distance(p1, p2):
    from math import sqrt
    d = sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)
    return d


def main():
    p1 = Point()
    p2 = Point(1, 3)
    p1.move(2, 5)
    d = distance(p1, p2)
    d2 = p1.caldistance(p2)
    print('distance between point (%s, %s) and (%s, %s) is %.2f' %(p1.x, p1.y, p2.x, p2.y, d2))


if __name__ == '__main__':
    main()


from typing import Any, Union


class Person(object):

    __slots__ = ('name', '_age', '_gender')  # slots has no effect on subclasses

    def __init__(self, name, age=0, gender='male'):
        self._age = age
        self.name = name
        self._gender = gender

    @property
    def age(self):
        return self._age

    @property
    def gender(self):
        return self._gender

    @age.setter
    def age(self, age):
        self._age = age

    @gender.setter
    def gender(self, gender):
        self._gender = gender

    def play(self):
        print('%s is playing happily' % self.name)

    def watch_tv(self):
        if self._age >= 18:
            print('%s is watching terrible movies' % self.name)
        else:
            print('%s is watching animation' % self.name)


class Student(Person):

    def __init__(self, name, age=0, grade=100, gender='male'):
        super().__init__(name, age, gender)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s is learning %s' %(self.name, course))

    def __info(self):
        self.__info = self._grade

    def game(self):
        if self._age <= 10:
            print('The game is not for %s' % self.name)
        else:
            print('%s, let\'s play!' % self.name)

    @staticmethod
    def is_a_student(age):
        if age >= 18 or age < 6:
            return False
        else:
            return True

    @classmethod
    def me(cls, myname, myage, mygrade, mygender):
        return cls(myname, myage, mygrade, mygender)


class Teacher(Person):

    def __init__(self, name, age=30, title='Professor', gender='male'):
        super().__init__(name, age, gender)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s is teaching %s' % (self.name, course))

    def __info(self):
        self.__info = self._title


def main_property():
    student = Student('mikkel', 23, 10, 'male')
    student.study('compiling')
    print(student.gender)
    student.gender = 'female'
    print(student.gender)
    student.game()
    student.age = 5
    student.game()
    # if added __slots__, no additional attribute could be added
    # student.height = 180
    # print(student.height)


def main_static_class():
    persondata = ('mikkel', 25, 10, 'male')
    if Student.is_a_student(persondata[1]):
        it = iter(persondata)
        astudent = Student(next(it))
        print(astudent.name)
        astudent.game()
    else:
        print('the person is not a student')
    Student.me('Xuyun', 27, 11, 'female').game()  # 无需实例化


def main_parent_subclass():
    stu = Student('王大锤', 15, '初三')
    stu.study('数学')
    stu.watch_tv()
    t = Teacher('骆昊', 38, '砖家')
    t.teach('Python程序设计')
    t.watch_tv()


from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        pass


class Dog(Pet):

    def make_voice(self):
        print('%s: wong, wong!' % self._nickname)


class Cat(Pet):
    def make_voice(self):
        print('%s: meo, meo!' % self._nickname)


def main_override():
    pets = [Dog('taylor'), Cat('Kitty')]
    for pet in pets:
        pet.make_voice()


class Employee(object, metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def salary(self):
        pass


class Manager(Employee):

    def __init__(self, name):
        super().__init__(name)

    def salary(self):
        print('The salary of manager %s is 15000rmb.' % self.name)
        return 15000


class Programmer(Employee):

    def __init__(self, name):
        super().__init__(name)

    def salary(self, workhour):
        salary = workhour*150
        print('The salary of programmer %s is %s rmb' % (self.name, salary))
        return salary


class Salesman(Employee):

    def __init__(self, name):
        super().__init__(name)

    def salary(self, sales):
        salary = sales*0.05 + 1200
        print('The salary of salesman %s is %s rmb' % (self.name, salary))
        return salary


def main_employee():
    manager = Manager('mike')
    programmer = Programmer('mikkel')
    salesman = Salesman('joo')
    manager.salary()
    programmer.salary(200)
    salesman.salary(20000)


if __name__ == '__main__':
    main_employee()

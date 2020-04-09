class Student(object):

    def __init__(self, name, age=0, grd=1, gender='male'):
        self._age = age
        self.name = name
        self.grd = grd
        self._gender = gender


    def study(self,course):
        print('%s is learning %s' %(self.name, course))

    def __info(self):
        self.__info = str(self._age) + self._gender
        print(self.__info)

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

    def game(self):
        if self._age<=10:
            print('The game is not for %s' % self.name)
        else:
            print('%s, let\'s play!' % self.name)


def main_property():
    student = Student('mikkel', 23, 10, 'male')
    student.study('compiling')
    print(student.gender)
    student.gender = 'female'
    print(student.gender)
    student.game()
    student.age = 5
    student.game()


if __name__ == '__main__':
    
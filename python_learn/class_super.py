# -*- coding:utf-8 -*-


class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print(self.name, f' is now eating {food}.')


class YellowPerson(Person):

    def __init__(self, name, age, weight):
        self.weight = weight
        super().__init__(name, age)

    def print_some(self):
        print(self.name, f' is {self.age} years old. {self.weight} pounds')


xz = YellowPerson('xz', 18, 63)
xz.print_some()


class YellowPeopleFather(Person):
    
    def play(self):
        print('method of yellow people')

    def eat(self, food):
        print(self.name, f' is eating father {food}.')


class WhitePeopleMother(Person):
    
    def say(self):
        print('method of white people')

    def eat(self, food):
        print(self.name, f' is eating mother {food}.')


class Son(YellowPeopleFather, WhitePeopleMother):
    pass


xw = Son('xw', 18)
xw.play()
xw.say()
xw.eat('apple')
print(Son.__mro__)



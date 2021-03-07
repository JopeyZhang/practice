# -*- coding:utf-8 -*-


class Person():
    attr = 'qwer'  # common variable

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def say(self, something):
        return f'{self.name} said {something}'

    def eat(self, food):
        return f'{self.name} ate {food}'


xz = Person('xz', 18, 'male')
xw = Person('xw', 18, 'female')
print(xz.name)
print(xz.age)
print(xz.gender)
print(xw.name)
print(xw.gender)
print(xz.attr)
print(xw.attr)
print(xz.eat('orange'))
print(xz.say('orange is good'))


class YellowPerson(Person):

    def sing(self, song):
        return f'{self.name} is singing {song}'


xl = YellowPerson('xl', 18, 'male')
print(xl.name)
print(xl.sing('"trouble is a friend"'))


# super()
class Father():
    attr1 = '666'
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Son(Father):
    def print_some(self):
        print("Son calls Fathers'attr1:", super().attr1)


xzz = Son('xzz', 18)
xzz.print_some()


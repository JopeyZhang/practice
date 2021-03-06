# -*- coding:utf-8 -*-


# func1
age1 = 18 # global variable

def my_func1():
    name = "xz" # local variable
    print(name)

    global age1 # add "global" before global variable, then you can call it in a func.
    age1 += 1
    print(age1)

my_func1()


# func2
age2 = 28

def my_func2():
    age2 = 66
    def my_inner_func():
        nonlocal age2
        age2 += 1
        print(age2)

    my_inner_func()

my_func2()





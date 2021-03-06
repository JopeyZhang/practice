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


# func3
mylist1 = [1, 2, 3, 4]

def change_list1(list1):
    list1[1] = 'number'

    return list1

change_list1(mylist1)
print(mylist1)


# func4
mylist2 = [5, 6, 7, 8]

def change_list2(list2):
    list2 = [9, 10, 11, 12]

    return list2

change_list2(mylist2)
print(mylist2)

# func5
def get_sum(a, b=2):
    sum = a + b
    return sum

value = get_sum(2)
print(value)


# func6
def print_some(name, *age):  # *age→(1,2,3,4); **age→(age=1, age2=2, age3=3, age4=4)
    print('name:', name)
    print(age)  # tuple
    print('age:', age)

print_some('xz', 1,2,3,4)  # *age→(1,2,3,4); **age→('age':1, 'age1':2, 'age3':3, 'age4':4)




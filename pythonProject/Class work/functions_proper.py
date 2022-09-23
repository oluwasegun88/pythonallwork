# name= "Hadiza"
# print(globals())
#
# def func(num):
#     print(locals())
#
# func(15)


# a = 5
# def func1():
#     global a
#     a += 7
#     print(a)
#
# func1()
#
# a += 8
# func1()


a = 5


def func1():
    b = 10

    def inner_func():
        nonlocal b
        global a
        b += 2
        print(b)

    inner_func()
    print(b)


func1()


def func(*args):
    print(args)


func(1, 2, 3, 4, 5)


def func(*args):
    total = 0
    for arg in args:
        total += arg
    print(total)


func(1, 2, 3, 4, 5, 6)


# Dictionary
def func1(**kwargs):
    print(kwargs)


func1(a=1, b=2, c=3, d=4, e=5)

# unpacking
lst = [3, 1, 7, 4, -3, 4]
func(*lst)


# Dict Unpacking
def func1(**kwargs):
    for k, v in kwargs.items():
        print(kwargs)


dict_ = {"a": 2, "b": 6, "c": 7}
func1(**dict_)


def func_again(a, b, /, c, *, d):
    print(a, b, c, d)


func_again(1, 2, c=6, d=4)

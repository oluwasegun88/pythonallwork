# def add(a:int, b:int) -> int:
#     """Adds two numbers"""
#
#     return a+b
#
# print(add.__name__)
# print(add.__doc__)
# print(add.__annotations__)
#
#
# def operate(x,y,func):
#      return func(x,y)
# #print(operate(2, 3,add))
#
# def sub(x,y):
#     return y-x

# print(operate(5,8, sub))


# def multiply(a):
#     def by(b):
#         return  a*b
#     return by
#
# multiply_by_five = multiply(5)
#
# print(multiply_by_five(6))

# LAMBDAS

# add = lambda a, b: a + b
# print(add.__name__)
# print(add(10,9))
# print(operate(2,3,add))
# print(operate(2,3,lambda a,b:a+b))
# print(operate(2,3,lambda a,b:b-a))
# print(operate(2,3,lambda w,y:w*y))


# import builtins
# print(abs(-1))
#
# print(round(56.67854,2))
# print(round(56.67854,-1))
#
# arr=[1,6,4,7,2]
# print(sum(arr, 100))
#
# arr=[1,6,4,7,2]
# print(sum((2,3,4), 100))
#
#
# letters = [['a'], ['b', 'c'], ['d'],['e','f']]
# print(sum(letters,[]))
# print(max([1,2,3,4,5,6]))
# print(min([1,2,3,4,5,6]))
#
#fruits = "apple pear cucumber mango grape melon".split()
# print(max(fruits,key=len))
# print(min(fruits, key=len))
# print(max(fruits,key=lambda x:x[-1]))
# print(max(fruits,key=lambda x:x[-3:]))

# def last_three(x):
#     return x[-3]
#
# print(max(fruits,key=))

# iterable1 =(1,2,3,4)
# iterable2 =('hello', 'how', 'are', 'you')
# print(list(zip(iterable2,iterable1)))
# print(dict(zip(iterable2,iterable1)))
# print(sorted('helloAZ'))
# print(sorted('helloAZ', reverse=True))

#fruits = "apple pear cucumber mango grape melon".split()
#fruits = "apple pear cucumber mango grape melon"
# print(sorted('fruits'))
# print(sorted(fruits, key=len))
# print(sorted(fruits, key=lambda x: x[-1]))
# print(sorted('fruits', reverse=True))


# NOT SAME LENGHT
# iterable1 =(1,2,3,)
# iterable2 =('hello', 'how', 'are', 'you')
# print(list(zip(iterable2,iterable1)))
# print(dict(zip(iterable2,iterable1, strict=True)))

# print(map(lambda x:x ** 2,[1,2,3,4,5]))

lst =[1,2,3,4,5]
# print(list(map(lambda x:x ** 2,lst)))
# print([x**2 for x in lst])

# print(list(map(str.upper, fruits)))
# print(list(map(lambda x:x.upper(), fruits)))
# fruits.append('Agbado')
#
# print(list(filter(str.istitle, fruits)))
# print(list(filter(lambda x: not x.istitle(), fruits)))
#
# print([x for x in fruits if not x.istitle()])
# print([x.upper() for x in fruits if not x.istitle()])


# from functools import reduce
#
#
#
# def reduce_func(acc, item):
#     print(f"acc-> {acc} <> item -> {item} ")
#     return acc + item
#
#
# print(lst)
#
# print(reduce(reduce_func, lst, 100))
#
# from math import prod
#
# print("\n##################### Reduce ##########################\n")
#
# # print(reduce(lambda acc, item: acc + item,lst))
#
#
# print(sum(lst, 100))
# print(prod(lst, start=100))
# print(reduce(lambda acc, item: acc if acc > item else item, lst))
# print(reduce(lambda acc, item: acc if acc > item else item, lst))
#
# print(max(lst))
# #print(reduce(max_func, fruits))
#
# print("############# match #################")
#
# num = int(input("Enter a number:"))

# match num:
#     case 1:
#         print(1)
#     case 2:
#         print(2)
#     case _:
#         print("Don't know you")


# match num:
#     case _ as x if 1 <= x  <= 10:
#         print(x)
#     case _ as x if 11 <= x  <= 20:
#         print(x)
#     case _:
#         print("Don't know you")

# match num:
#     case _ as x if 11 <= x  <= 20:
#         print(x)
#     case 30 | 40 | 50:
#         print(x)
#     case _:
#         print("Don't know you")

#lst = [20,13,16]

# match lst:13
#
#     case[i1,i2,i3]:
#         print(i3,i2,i1)
#     case _:
#         print("Nothing matched")

# match lst:
#
#     case[x,y,int(z)]:
#         print(x,y,z)
#     case _:
#         print("Nothing matched")
#
# match lst:13
#
#     case[i1,i2,i3]:
#         print(i3,i2,i1)
#     case _:
#         print("Nothing matched"



# def fizzbuzz(num):
#     three = num % 3
#     five = num % 5
#     match(three, five):
#         case(0,0):
#             return "FIZZBUZZ"
#         case(0, _):
#             return "FIZZ"
#         case(_, 0):
#             return "BUZZ"
#         case _:
#             return num
#
# for i in range(1,101):
#     print(fizzbuzz(i))
#
#
# def summing_list(list_: list[int]) -> int | None:
#     match list_:
#         case []:
#             return 0
#         case[first_value, *another_list]:
#             return first_value + summing_list((another_list))
#         case _:
#             print("Can only accept an int")
#             return None
#
# print(summing_list([1,2,3,4,5]))


import itertools
# itertools.zip_longest([1,2],[3,4,5],fillvalue=0)
print(list(itertools.zip_longest([1,2],[3,4,5], fillvalue=0)))

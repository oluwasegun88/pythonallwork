import doctest




# def add(x, y):
#     assert isinstance(x, (int, float)) and isinstance(y, (int, float)), "Only int or float can be added"
#     assert x > 0 and y > 0, "numbers cannot be negative"
#     return x + y
#
#
# assert [1, 2, 3] == [1, 2, 3]
# print(add("2", "3"))

# print(add(-2,3))



# def sum_list(lst):
#     assert isinstance(lst,list),"This Function Takes Only a List"
#     return sum(lst)
#
# new_turple=(1,2,3,4,5)
# print(sum_list(new_turple))
#
# new_list=[1,2,3,4,5]
# print(sum_list(new_list))

class MyCustomException:
    pass


def add(x, y):
    """  adds two numbers
    >>>  add(5,5)
    10
    >>>  add(2,-6)
    -4
    >>>  add(2,"hi") # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'

    """
    if x > y:
        raise MyCustomException("Just fooling around")
    return x + y


print(add(5, 5))
if __name__ == "__main__":
    doctest.testmod(verbose=True)

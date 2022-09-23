##help(s.find)
# from this import


# name = "BANKE OWOLABI"
# print(name.lower())
# name.capitalize()
# print(name.capitalize())
# print(name.swapcase())
# print(name.title())
# name ="Banke"
# name.casefold
# print(name.casefold())
# name: str = "Banke"
# name.startswith('b')
# print(name.startswith())
# name = Str ="Banke"
# print(name.ljust(20))
from this import s

# name = 'BANKE OWOLABI'
# print(name.count('B'))
# print(name.find("OWO"))
# print(name.find('B',2))
# print(name.index('B',2))
# print(name.rindex('B'))
# print(name.replace('OWOLABI','OLAYEMI'))
# print(name)
# print(name.replace('B','@', 1))
# print(name.replace('B','@'))

# #help(s.replace)

# name: str = "    Banke Owolabi\n\t"
# # print(name.strip())

# name = name.strip()
# print(name)

# help(s.zfill)

# '10'.zfill(3)
# print('10'.zfill(3))

#name = 'Banke Owolabi'
# print(name)
# print(name.split())

# binary = "1011001001"
# print(binary.replace('0', '1'))
# print(binary.replace('1', "0"))
# print(binary.replace('1', '#').replace('0', '1').replace('#', '0'))
#
# binary.translate(str.maketrans('01', '10'))
# print(binary.translate(str.maketrans('01', '10')))

# name.translate(str.maketrans('b', 'B', 'oaw'))
# print(name.translate(str.maketrans('b', 'B', 'oaw')))
#
# "12301203450123".translate((str.maketrans('012','109','3')))
# print("12301203450123".translate(str.maketrans('012','109','3')))


# import string
#
# abc = string.ascii_lowercase
#
# word = "love"
# k=5
#
# encoded = word.translate(str.maketrans(abc[:-5],abc[5:]))
# print(word.translate(str.maketrans(abc[:-5],abc[5:])))

def f(qty, item,price):
    print(f'{qty} {item} cost $ {price:2f}')
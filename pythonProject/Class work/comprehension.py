# cont = []
# for i in range(1,11):
#     cont.append(i)

    # squares = []

    # for i in range(1,11):
    #     squares.append(i ** 2)

# cont = [num   for num in range(1, 11)]
# primeNumbers = [num   for num in range(1, 11) if num % num!=0]
# squares = [num ** 2 for num in range(1, 11)]
# evenNumbers = [num   for num in range(1, 11) if num % 2 !=0]
# even_squared_odd_cubed = [num ** 2 if num % 2 ==0 else num ** 3 for num in range(1,11)]
#
# print(even_squared_odd_cubed)
# print(cont)
# print(primeNumbers)
# print(squares)
# print(evenNumbers)

# names = ['bimpe', 'Banke',' abimbola','Kelechi','James', 'Olalekan', 'Racheal']
# my_names = [name for name in names if name.istitle()]
# print(my_names)
#
#
# names = ['bimpe', 'Banke',' abimbola','Kelechi','James', 'Olalekan', 'Racheal']
# my_names = [name for name in names if name.istitle()]
# number_of_times = int(input('how many times do you want to enter your name?'))
# input_names=[input(f"{i+1}.Name?") for i in range(number_of_times)]
# print(number_of_times)
#
#
# names = ['bimpe', 'Banke',' abimbola','Kelechi','James', 'Olalekan', 'Racheal']
# my_names = [name for name in names if name.istitle()]
# input_names = [input(f"{i+1}.Name?") for i in range(5)]
# print(input_names)

# my_names = []
# for name in names:
#     if name.istitle():
#         my_names.append(name)

# x_and_y = []
# for x in range(1,5):
#      for y in range(1,5):
#          x_and_y.append((x,y))
#          print(x_and_y)

# x_and_y = [(x,y) for x in range (1,6) for y in range (1,6)]
# print(x_and_y)
#SET COMPREHENSION
# x_and_y = {(x,y) for x in range (1,6) for y in range (1,6)}
# print(x_and_y)

listcomp = [num % 3 for num in range(1,10)]
setcomp = {num % 3 for num in range(1,10)}
dictcomp = {k: v for k, v in enumerate(range(11,16))}
genexp = (num for num in range(1,6))

print(type(listcomp),listcomp)
print(type(setcomp),setcomp)
print(type(dictcomp),dictcomp)
print(type(genexp), genexp)

print(next(genexp))
print(next(genexp))
print(next(genexp))
print(list(genexp))

# print((i for i in range(10_000_000_000)))
# genexp([i for i in range(10_000_000_000)])
# for i in genexp:
#     print(i)
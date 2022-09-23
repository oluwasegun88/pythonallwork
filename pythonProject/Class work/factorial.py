num = int(input("Enter any number:"))


def cal_factorial(num):
    factorial = 1
    if num == 0:
        return 1
    for i in range(1, num + 1):
        factorial = factorial * i
    return factorial


output = cal_factorial(num)
print('factorial of number', num, ' is:', output)

import random

guess_number = random.randint(1, 100)
count = 0

while count < 3:

    number = int(input("Enter a number"))

    if number > guess_number:
        print("number too high")

    elif number < guess_number:
        print("number too low")

    else:
        print("try again")
        break
    count += 1
if number != guess_number:
    print("Maximum Trials Exceeded")



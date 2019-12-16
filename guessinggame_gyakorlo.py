import math
import random

a = [random.randint(1,99) for x in range(10)]
b = [random.randint(1,49) for x in range(10)]

def check_good_number(list, to):
    if to == 1:
        max = 99
    else:
        max = 49
    for i in range(10):
        guessed_number = int(input(f"Enter an integer from 1 to {max}: "))
        while list[i] != guessed_number:
            if (guessed_number) < list[i]:
                print("guess is low")
                guessed_number = int(input(f"Enter an integer from 1 to {max}: "))
            elif guessed_number > list[i]:
                print("guess is high")
                guessed_number = int(input(f"Enter an integer from 1 to {max}: "))
            else:
                break
        print("you guessed it!")

check_good_number(a, 1)
check_good_number(b, 2)

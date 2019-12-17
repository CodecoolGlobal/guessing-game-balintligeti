import math
import random

one_to_99 = [random.randint(1,99) for x in range(10)]
one_to_49 = [random.randint(1,49) for x in range(10)]

def guess_a_num(to):
   guess = int(input(f"Enter an integer from 1 to {to}: "))
   return guess

def check_good_number(list, to):
    for i in range(10):
        (guessed_number) = guess_a_num(to)
        while list[i] != guessed_number:
            if (guessed_number) < list[i]:
                print("guess is low")
                guessed_number = guess_a_num(to)
            elif guessed_number > list[i]:
                print("guess is high")
                guessed_number = guess_a_num(to)
            else:
                break
        print("you guessed it!")

check_good_number(one_to_99,99)
check_good_number(one_to_49,49)

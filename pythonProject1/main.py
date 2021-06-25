
import random

print("--------------GAME----------------")

def guess(a):
    number=random.randint(1,a)
    guess=0
    while guess != number:
        num=int(input("Enter you guess:  "))
        if num < number:
            print("You are one unlucky bastard Try again,Guess is too low")
        elif num > number:
            print("unlucky bastard Try again,Guess is too high")
        else:
            print("Winner Winner chicken dinner")
guess(10)
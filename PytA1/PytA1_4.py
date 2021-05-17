from random import randint
def guess():
    guessed = int(input("Adivide el numero entre 0 - 10: "))
    toguess = randint(0,10)
    return guessed == toguess

print(guess())
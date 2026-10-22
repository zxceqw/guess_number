from random import randint
number = randint(1, 100)
guess = int(input())
while guess != number:
    if guess > number:
        print('Ваше число больше загаданного')
        guess = int(input())
    elif guess < number:
        print('Ваше число меньше загаданного')
        guess = int(input())    
print('Отличная интуиция! Вы угадали число :)')

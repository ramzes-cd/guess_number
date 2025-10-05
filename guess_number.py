# Импорт функции  для генерации случайного числа
from random import randint

# Создаём случайное число и помощаем его значение в переменную
number = randint(1, 100)
print('Guess integer 1-100')

# Вывод после угадывани числа
while True:
    guess = int(input('Enter your number: '))

    # Условия для выхода из цикла
    if guess > number:
        print('You number is too big')
    elif guess < number:
        print('You number is too small')
    elif guess == number:
        print("You win!!!")
        break
    else:
        print("Uncorrection enter")

print("All right!")

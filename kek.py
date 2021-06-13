import random
#Угадайка!
a = int(input(' Угадайка число!(Введите цифру от 1 до 5) '))
b = random.randint(1, 5)

if a == b:
    print('Вы угадали!')
elif a > b:
    print('Увы, Ваше число было больше загаданного!')
elif a < b:
    print('Увы, Ваше число было меньше загаданного!')
else:
    print('Шо?')

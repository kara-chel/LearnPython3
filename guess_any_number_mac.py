#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# import random

# the_number = random.randint(1, 100)

min_num = 1
max_num = 100

print('Загадайте число от 1 до 100, а я попробую его угадать.')
num = 0
count = 0
while (num < min_num or num > max_num or count == 0):
    if count > 0:
        print('Не верный диапазон, число болжно быть в пределах от ',
              min_num, ' до ', max_num, ' включительно!')
    count += 1
    num = int(input('Введите число: '))

count = 0
while True:
    count += 1
    avr_num = int(min_num + (max_num - min_num) / 2)
    print ('Среднее число между ', min_num, ' и ', max_num, ' = ', avr_num)
    if avr_num == num:
        print('Вы загадали число: ', avr_num)
        print('Я отгадал с ', count, ' попытки.')
        break
    elif avr_num < num:
        min_num = avr_num
        print('Загаданное число больше чем ', avr_num)
    elif avr_num > num:
        max_num = avr_num
        print('Загаданное число меньше чем ', avr_num)
print('Спасибо за игру!')

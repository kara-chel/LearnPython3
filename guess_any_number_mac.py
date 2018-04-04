#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# import random

# the_number = random.randint(1, 100)

print('Загадайте число от 1 до 100, а я попробую его угадать.')
num = 0
count = 0
while (num < 1 or num > 100 or count == 0):
    if count > 0:
      print('Не верный диапазон, число болжно быть в пределах от 1 до 100 включительно!')
    count += 1
    num = int(input('Введите число: '))

min_num = 1
max_num = 100
count = 0
while True:
    count += 1
    avr_num = int(min_num + (max_num - min_num) / 2)
    print ('Среднее число между ', min_num, ' и ', max_num, ' = ', avr_num)
    if avr_num == num:
        print('Вы загадали число: ', avr_num)
        print('Я отгадал с попытки: ', count)
        break
    elif avr_num < num:
        min_num = avr_num
        print('Загаданное число больше чем ', avr_num)
    elif avr_num > num:
        max_num = avr_num
        print('Загаданное число меньше чем ', avr_num)
print('Спасибо за игру!')

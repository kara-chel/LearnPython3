#!/usr/bin/python3
# -*- coding: utf-8 -*-

min_num = 1
max_num = 1000

print('Загадайте число от ', min_num, ' до ', max_num,
      'а я попробую его угадать.')
num = 0
count = 0
while (num < min_num or num > max_num or count == 0):
    if count > 0:
        print('Не верный диапазон, число болжно быть в пределах от ',
              min_num, ' до ', max_num, ' включительно!')
    count += 1
    num = int(input('Введите число: '))

count = 0
# max_num += 1
while True:
    count += 1
    print(count)
    avr_num = int(min_num + (max_num - min_num + 1) / 2)
    # avr_num = int(round(min_num + (max_num - min_num) / 2))
    print ('Среднее число между ', min_num, ' и ', max_num, ' = ', avr_num)
    if avr_num == num:
        print('Вы загадали число: ', avr_num)
        print('Я отгадал с ', count, ' попытки.')
        break
    elif avr_num < num:
        min_num = avr_num + 1
        print('Загаданное число больше чем ', avr_num)
    elif avr_num > num:
        max_num = avr_num - 1
        print('Загаданное число меньше чем ', avr_num)
print('Спасибо за игру!')

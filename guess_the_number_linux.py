#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random

the_number = random.randint(1, 100)

print('Я загадал число, попробуй отгадай с 6 попыток.')
attempt = 0
while True:
    attempt += 1
    print('Попытка ', attempt, '. Введите число: ')
    num = int(input())
    if num == the_number:
        print('Вы отгадали!')
        break
    elif num > the_number:
        print('Я загадал число меньше чем ', num)
    elif num < the_number:
        print('Я загадал число больше чем ', num)
    if attempt >= 6:
        print('У вас кончились попытки, я загодал число: ', the_number)
        break

#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

#import random

#the_number = random.randint(1, 100)

print('Загадайте число от 1 до 100')
num = 0
count = 0
while (num < 1 or num > 100 or count == 0):
    if count > 0:
        print('Не верный диапазон, число болжно быть в пределах от 1 до 100 включительно!')
    count += 1
    num = int(input('Введите число: '))

print('Вы ввели: ', num)

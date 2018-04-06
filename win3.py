#!/usr/bin/python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

# Функция для отображения
def func(x):
   return [i**2 for i in x]

if __name__ == '__main__':
   # Значения по X
   x = [i for i in range(-100, 100)]
   # Значения по Y
   y = func(x)

   plt.title("X^2 plot")
   plt.xlabel("X")
   plt.ylabel("Y")
   # представляем точки (х,у) кружочками диаметра 10
   plt.scatter(x, y, edgecolors='r', s=10)

   # Сетка на фоне для улучшения восприятия
   plt.grid(True, linestyle='-', color='0.75')

   plt.show()


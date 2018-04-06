#!/usr/bin/python3
# -*- coding: utf-8 -*-

n = 0.1
for x in range(1, 100):
    print('int(', n, ') = ', int(n))
    print('round(', n, ') = ', int(round(n)))
    n += 0.1

# -*- coding: utf-8 -*-

x = int(input())
y = int(input())

if x < y:
    for number in range(x + 1, y):
        if number % 5 == 2 or number % 5 == 3:
            print(number)
else:
    for number in range(y + 1, x):
        if number % 5 == 2 or number % 5 == 3:
            print(number)

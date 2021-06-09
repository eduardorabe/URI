# -*- coding: utf-8 -*-

number = -1

while number != 0:
    number = int(input())
    for x in range(1, number + 1):
        if x < number:
            print(x, end=" ")
        else:
            print(x)

# -*- coding: utf-8 -*-

test_ammount = int(input())

for _ in range(test_ammount):
    number = int(input())
    eh_primo = 0
    for test in range(1, number + 1):
        if number % test == 0:
            eh_primo += 1
    if eh_primo > 2:
        print(f"{number} nao eh primo")
    if eh_primo == 2:
        print(f"{number} eh primo")

# -*- coding: utf-8 -*-

x = 1

while x == 1:
    score_num = 0
    score_total = 0
    while score_num < 2:
        score = float(input())
        if 0 <= score <= 10:
            score_total += score
            score_num += 1
        else:
            print("nota invalida")
    print(f"media = {(score_total / 2):.2f}")

    x = int(input("novo calculo (1-sim 2-nao)\n"))
    while x != 1 and x != 2:
        x = int(input("novo calculo (1-sim 2-nao)\n"))

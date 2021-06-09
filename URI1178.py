# -*- coding: utf-8 -*-

X = float(input())
N = list()
N.append(X)

while len(N) != 100:
    N.append(X / 2)
    X /= 2

i = 0
for number in N:
    print(f"N[{i}] = {number:.4f}")
    i += 1

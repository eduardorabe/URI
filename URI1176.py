# -*- coding: utf-8 -*-

fibonacci = [0, 1, 1, 2]

num_test_cases = int(input())

for _ in range(num_test_cases):
    case = int(input())
    if case < len(fibonacci):
        print(f"Fib({case}) = {fibonacci[case]}")
    else:
        for x in range(len(fibonacci), case + 1):
            fibonacci.append(fibonacci[x - 1] + fibonacci[x - 2])
        print(f"Fib({case}) = {fibonacci[case]}")

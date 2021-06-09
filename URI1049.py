# -*- coding: utf-8 -*-

primeiro = input()
segundo = input()
terceiro = input()

if primeiro == "vertebrado":
    if segundo == "ave":
        if terceiro == "carnivoro":
            print("aguia")
        elif terceiro == "onivoro":
            print("pomba")
    elif segundo == "mamifero":
        if terceiro == "onivoro":
            print("homem")
        elif terceiro == "herbivoro":
            print("vaca")
elif primeiro == "invertebrado":
    if segundo == "inseto":
        if terceiro == "hematofago":
            print("pulga")
        elif terceiro == "herbivoro":
            print("lagarta")
    elif segundo == "anelideo":
        if terceiro == "hematofago":
            print("sanguessuga")
        elif terceiro == "onivoro":
            print("minhoca")

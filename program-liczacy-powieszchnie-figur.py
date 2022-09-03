import math

print("Welcome! This is program for counting the field of geometric figures.\n 1- kwadrat, 2-prostokąt, 3-koło, 4-trójkąt, 5-trapez, 6-wyjdź")

while True:
    wybor = int(input("What u want to do?: "))

    if wybor == 1:
        a = int(input("Podaj dłg boku kwadratu: "))
        def pole_kwadratu(a):
            return a * a
        print(pole_kwadratu(a))
    elif wybor == 2:
        a = int(input("Podaj dłg boku prostokąta: "))
        b = int(input("Podaj dłg boku prostokąta: "))
        def pole_prostokata(a, b):
            return a * b
        print(pole_prostokata(a, b))
    elif wybor == 3:
        r = int(input("Podaj dłg promienia koła: "))
        def pole_kola(r):
            return math.pi * r ** 2
        print(pole_kola(r))
    elif wybor == 4:
        a = int(input("Podaj dłg podstawy trójkąta: "))
        h = int(input("Podaj dłg wysokości trójkąta: "))
        def pole_trojkata(a, h):
            return 0.5 * a * h
        print(pole_trojkata(a, h))
    elif wybor == 5:
        a = int(input("podaj dłg podstawy trapezu: "))
        b = int(input("Podaj dłg podstawy trapezu: "))
        h = int(input("POdaj dłg wysokości trapezu: "))
        def pole_trapezu(a, b, h):
            return (a + b) / 2 * h
        print(pole_trapezu(a, b, h))
    elif wybor == 6:
        break 
            

import figury
from enum import IntEnum 

Menu_Figury = IntEnum('Menu_figury', {'Kwadrat': 1, 'Prostokąt': 2, 'Koło': 3, 'Trójkąt': 4, 'Trapez': 5})

print("Witam w programie liczącym pole figur!")

while True:
    wybor = int(input("""Wybierz figurę której pole chcesz obliczyć
    1. Kwadrat
    2. Prostokąt
    3. Koło
    4. Trójkąt
    5. Trapez
    """))

    if (wybor == Menu_Figury.Kwadrat):
        a = float(input("Podaj dłg boku kwadratu: "))
        print("Pole kwadratu wynosi: ", figury.pole_kwadratu(a))   
    elif (wybor == Menu_Figury.Prostokąt):
        a = float(input("Podaj dłg boku prostokąta: "))
        b = float(input("Podaj dłg boku prostokąta: "))
        print("Pole prostokąta wynosi: ", figury.pole_prostokata(a, b))
    elif (wybor == Menu_Figury.Koło):
        r = int(input("Podaj dłg promienia koła: "))
        print("Pole koła wynosi: ", figury.pole_kola(r))
    elif (wybor == Menu_Figury.Trójkąt):
        a = float(input("Podaj dłg podstawy trójkąta: "))
        h = float(input("Podaj dłg wysokości trójkąta: "))
        print("Pole trójkąta wynosi: ", figury.pole_trojkata(a, h))
    elif (wybor == Menu_Figury.Trapez):
        a = float(input("podaj dłg podstawy trapezu: "))
        b = float(input("Podaj dłg podstawy trapezu: "))
        h = float(input("POdaj dłg wysokości trapezu: "))
        print("Pole trapezu wynosi: ", figury.pole_trapezu(a, b, h))
    

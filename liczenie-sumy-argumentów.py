""":
def sumuj(*liczby):
    suma = 0
    wynik = [*liczby]
    for liczba in liczby:
        suma = suma + liczba
    print("Wynik sumy liczb:", wynik)
    return suma

print(sumuj(2,4,1,2,4,5,10))
"""
def lista_liczb(ile):
    lista = []
    print("Podaj", ile, "liczb: ")
    for liczba in range(0, ile):
        x = int(input())
        lista.append(x)
    print("podane liczby:", lista)
    return lista

def sumuj(func, ile):
    lista2 = func(ile)
    sum = 0
    for i in lista2:
        sum = sum + i
    print("Suma liczb wynosi: ")
    return sum

print(sumuj(lista_liczb,5))

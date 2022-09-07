import time

#sumujDo1
def sumuj_do(liczba):
    suma = 0

    for liczba in range (1, liczba+1):
        suma = suma + liczba
    return suma

#sumujDo2
def sumuj_do2(liczba):
   return sum([liczba for liczba in range(1, liczba+1)])

#sumujDo3
def sumuj_do3(liczba):
   return sum({liczba for liczba in range(1, liczba+1)})

#sumujDo4
def sumuj_do4(liczba):
   return sum((liczba for liczba in range(1, liczba+1)))

#sumujDo5
def sumuj_do5(liczba):
   return(1 + liczba) / 2 * liczba

# przekazywanie funkcji 

def function_performance (func, arg, how_many_times = 1):
    sum = 0

    for i in range (0, how_many_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sum = sum + (end - start)

    return sum

def show_message(message):
    print(message) 

print(function_performance(sumuj_do, 5000, 25))
print(function_performance(sumuj_do2, 5000))
print(function_performance(sumuj_do3, 5000))
print(function_performance(sumuj_do4, 5000))
print(function_performance(sumuj_do5, 5000))
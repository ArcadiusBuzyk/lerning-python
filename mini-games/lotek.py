import random

def choose_random_numbers(amount, total_amount):
    numbersChoosen = []
    attempt = 0

    while (attempt < 6) :
        number = random.randint(0, total_amount)

        if number in numbersChoosen:
            return 

        else:
            numbersChoosen.append(number)   
            attempt += 1
    
    print("Wylosowane liczby:", numbersChoosen)

choose_random_numbers(6, 49)
# 1


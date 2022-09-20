import random

def choose_random_numbers(amount, total_amount):
    numbersChoosen = []
    attempt = 0
    while (attempt < amount) :
        number = random.randint(0, total_amount)

        if number in numbersChoosen:
            return 

        else:
            numbersChoosen.append(number)   
            attempt += 1
    
    print("Wylosowane liczby:", numbersChoosen)

choose_random_numbers(6, 49)
# 1

def choose_random_numbers2(amount2, total_amount2):
    print("Wylosowane liczby:", random.sample(range(total_amount2 + 1), amount2))

choose_random_numbers2(6, 49)
#2
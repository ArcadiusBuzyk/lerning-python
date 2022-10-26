def number_multiplied_by_itself_generator():
    number = 0
    while True:
        number += 1
        yield number * number


numberGenerator = number_multiplied_by_itself_generator()
generatedNumbers = []

for k in range(20):
    next(numberGenerator)
generatedNumbers.append(next(numberGenerator))

print(generatedNumbers)

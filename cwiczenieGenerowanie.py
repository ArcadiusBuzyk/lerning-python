def number_multiplied_by_itself_generator():
    number = 0
    while True:
        number = number + 1
        yield number * number


generatedNumbers = []

numberGenerator = number_multiplied_by_itself_generator()
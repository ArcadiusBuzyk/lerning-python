evenNumberGenerator = (element for element in range(400)if (element % 2 == 0))


def generate_even_numbers():
    for element in range(400):
        if (element % 2) == 0:
            yield element


a = generate_even_numbers()

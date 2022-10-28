class User:

    def __init__(self, age, name):
        print("jestem inicjalizatorem, który wywołuje sie zawsze podczas konstrukcji obiektu", age, name)

        self.age = age
        self.name = name

    def print_age(self, message):
        print(message, "wiek: ", self.name, self.age, "-", self.information)


user1 = User(22, "Arek")
user2 = User(30, "Mirek")

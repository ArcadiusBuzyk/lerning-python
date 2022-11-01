from random import randint
from math import sqrt


class Rocket:

    def __init__(self, speed=randint(1, 5)):
        self.altitude = 0

        self.speed = speed

        self.x = 0

    def moveUp(self):
        """rakieta porusza się do góry o (altitude) z szybkością speed
        """
        self.altitude += self.speed

    def __str__(self):
        return "Wysokość jaką osiągnęła rakieta: " + str(self.altitude)

    def get_distance(self, rocket):
        ab = (rocket.altitude - self.altitude) ** 2
        bc = (rocket.x - self.x) ** 2
        return sqrt(ab + bc)


class RocketBoard:
    def __init__(self, amountOfRockets=5):
        self.rockets = [Rocket(randint(1, 4)) for _ in range(amountOfRockets)]

        for _ in range(10):
            rocketIndexToMove = randint(0, len(self.rockets) - 1)
            self.rockets[rocketIndexToMove].moveUp()

        rocketList = []

        for rocket in self.rockets:
            print("Wysokość na jaka poleciała rakieta: ", rocket.altitude,
                  "wykonując: ", int(rocket.altitude / rocket.speed),
                  "ruchów, prędkość rakiety: ", rocket.speed)

            rocketList.append(rocket.altitude)

        print("Najwyższa wysokość: ", max(rocketList))

    def __getitem__(self, key):
        return self.rockets[key]

    def __setitem__(self, key, value):
        self.rockets[key].altitude = value

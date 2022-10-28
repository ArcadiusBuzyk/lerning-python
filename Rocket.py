from random import randint


class Rocket:

    def __init__(self, speed):
        self.altitude = 0
        self.speed = speed

    def moveUp(self):
        self.altitude += self.speed


rockets = [Rocket(randint(1, 4)) for _ in range(5)]

for _ in range(10):
    rocketIndexToMove = randint(0, 4)
    rockets[rocketIndexToMove].moveUp()

for rocket in rockets:
    print("Wysokość na jaka poleciała rakieta: ",  rocket.altitude,
          "wykonując: ", int(rocket.altitude/rocket.speed), "ruchów, prędkość rakiety: ", rocket.speed)

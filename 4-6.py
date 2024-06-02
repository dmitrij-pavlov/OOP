class Transport:
    def __init__(self, name):
        self.name = name

class WaterTransport(Transport):
    def __init__(self, name):
        super().__init__(name)

class Aircraft(Transport):
    def __init__(self, name):
        super().__init__(name)

class Aviation(Aircraft):
    def __init__(self, name):
        super().__init__(name)

class Airships(Aircraft):
    def __init__(self, name):
        super().__init__(name)

class Zeppelins(Airships):
    def __init__(self, name):
        super().__init__(name)

class HotAirBalloons(Airships):
    def __init__(self, name):
        super().__init__(name)

class LandTransport(Transport):
    def __init__(self, name):
        super().__init__(name)

class RailwayTransport(LandTransport):
    def __init__(self, name):
        super().__init__(name)

class Automobiles(LandTransport):
    def __init__(self, name):
        super().__init__(name)

class Bicycles(LandTransport):
    def __init__(self, name):
        super().__init__(name)

class AnimalDrawn(LandTransport):
    def __init__(self, name):
        super().__init__(name)

class SpaceTransport(Transport):
    def __init__(self, name):
        super().__init__(name)

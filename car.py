class Car:
    """Represent a Car object."""

    def __init__(self, name, fuel=0):
        """Initialise a Car instance with name and fuel."""
        self.name = name
        self.fuel = fuel
        self._odometer = 0

    def add(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance and return the distance driven."""
        if distance > self.fuel:
            distance_driven = self.fuel
            self.fuel = 0
        else:
            distance_driven = distance
            self.fuel -= distance
        self._odometer += distance_driven
        return distance_driven

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"
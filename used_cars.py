from car import Car


def main():
    """Demo test code to show how to use the Car class."""
    my_car = Car("My Car", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    limo = Car("Limo", 100)  # Step 1
    limo.add(20)         # Step 2
    print(f"Limo has fuel: {limo.fuel}")  # Step 3
    limo.drive(115)           # Step 4
    print(limo)               # Step 7


main()
menu = """C - Celsius to Fahrenheit
F - Fahrenheit to Celsius
Q - Quit
"""


def main():
    print(menu)
    choice = input(f"Choice: ").lower()

    while choice != "q":
        if choice == "c":
            celsius = float(input(f"Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} fahrenheit")
        elif choice == "f":
            fahrenheit = float(input(f"Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} celsius")
        else:
            print(f"Invalid Choice")
        print(menu)
        choice = input(f"Choice: ").lower()
    print(f"Program Ended.")


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()

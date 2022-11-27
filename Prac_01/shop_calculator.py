total = 0

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print(f"Invalid input")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    price = float(input(f"Price of items: "))
    total += price

if total > 100:
    total *= 0.9

print(f"Total price for {number_of_items} items is ${total:.2f}")

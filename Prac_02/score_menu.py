menu = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
score = -1

print(menu)
choice = input("Choice: ").lower()
while choice != "q":
    if choice == "g":
        score = float(input("Score: "))
        print(menu)
        choice = input("Choice: ").lower()
        while score < 0 or score > 100:
            print(f"Invalid score")
            score = float(input("Score: "))

    elif choice == "p":
        if score >= 90:
            print(f"Excellent")
        elif score >= 50:
            print(f"Passable")
        elif score >= 0:
            print(f"Bad")
        else:
            print(f"You have not inputted any number, please input a number at the menu")
        print(menu)
        choice = input("Choice: ").lower()

    elif choice == "s":
        if score == -1:
            print(f"You have not inputted any number, please input a number at the menu")
            print(menu)
        else:
            print(f"{'*' * int(score / 10)}")
            print(menu)
        choice = input("Choice: ").lower()

    else:
        print(f"Invalid Choice")
        print(menu)
        choice = input("Choice: ").lower()


print(f"Finished.")

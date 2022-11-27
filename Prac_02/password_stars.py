MINIMUM_LENGTH = 3


def main():
    password = get_password(MINIMUM_LENGTH)
    print_asterisk(password)


def get_password(MINIMUM_LENGTH):
    password = input(f"Enter password with more than {MINIMUM_LENGTH} characters: ")

    while len(password) <= MINIMUM_LENGTH:
        print("Please enter a password containing more than 3 characters.")
        password = input(f"Enter password with more than {MINIMUM_LENGTH} characters: ")

    return password


def print_asterisk(password):
    print("*" * len(password))


main()

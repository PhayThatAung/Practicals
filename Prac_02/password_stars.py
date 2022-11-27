password = "Password"

input_password = input("Password: ")

while input_password != password:
    print(f"Incorrect Password")
    input_password = input("Password: ")

if input_password == password:
    print(f"Correct Password")

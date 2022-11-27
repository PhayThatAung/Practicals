# Pseudocode:
# get name
# display menu
# get choice
# while choice != Q
#    if choice == H
#        display "hello" name
#    else if choice == G
#        display "goodbye" name
#    else
#        display invalid message
#    display menu
#    get choice
# display finished message

name = str(input("Enter name: "))

menu = """(H)ello
(G)oodbye
(Q)uit"""

print(menu)
choice = str(input(">>> ")).lower()

while choice != "q":
    if choice == "h":
        print(f"Hello {name}")
    elif choice == "g":
        print(f"Goodbye {name}")
    else:
        print(f"Invalid Choice")
    print(menu)
    choice = str(input(">>> ")).lower()

print(f"Finished")

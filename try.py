
import os


def clear():
    # os.system('cls||clear')
    os.system('cls' if os.name == 'nt' else 'clear')


clear()
should_continue = True
while should_continue:
    message = input("type message.  ")
    length = len(message)
    print(message)
    print(length)
    terminate = input("Type 'yes' to continue 'no' to end\n")
    if terminate == "no":
        should_continue = False
    else:
        clear()
print("Good bye")
month_days = [2, 3, 4, 5]
print(len(month_days))

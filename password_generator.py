# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(
    input("Please type in the number of letters you want in the password\n"))
nr_numbers = int(
    input("Please type in the number of numbers you want in the password\n"))
nr_symbols = int(
    input("Please type in the number of symbols you want in the password\n"))
password = ""
for letter in range(1, nr_letters + 1):
    random_letter = random.choice(letters)
    password += random_letter
for number in range(1, nr_numbers + 1):
    random_number = random.choice(numbers)
    password += random_number
for symbol in range(1, nr_symbols + 1):
    random_symbol = random.choice(symbols)
    password += random_letter
print(password)
# password_list = []
# for letter in range(1, nr_letters + 1):
# 	random_letter = random.choice(letters)
# 	password_list += random_letter
# for number in range(1, nr_numbers + 1):
# 	random_number = random.choice(numbers)
# 	password_list += random_number
# for symbol in range(1, nr_symbols + 1):
# 	random_symbol = random.choice(symbols)
# 	password_list += random_letter
# 	random.shuffle(password_list)
# password = ""
# for char in password_list:
# 	password += char
# print(password)

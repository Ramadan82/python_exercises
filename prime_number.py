# Write your code below this line
def prime_checker(number):
    is_prime = True
    for num in range(2, number):
        if num % 2 == 0:
            is_prime = False
    if is_prime:
        print("it's a prime number. ")
    else:
        print("it's not a prime number")

# Write your code above this line


# Do NOT change any of the code below
n = int(input("Check this number: "))
prime_checker(number=n)

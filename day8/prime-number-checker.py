def prime_check(number):
    is_prime = True
    for n in range(2, number):
        if number % n == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

num = int(input("Enter a number: "))
prime_check(number=num)
def is_prime(num):
    if num < 2: return False
    return len([n for n in range(2, num) if num % n == 0]) == 0


print(is_prime(int(input("Check if number is prime: "))))
